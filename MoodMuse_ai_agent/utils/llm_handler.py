# utils/llm_handler.py

import boto3
import os
import json
from dotenv import load_dotenv

load_dotenv()

def get_bedrock_client():
    return boto3.client(
        "bedrock-runtime",
        region_name=os.getenv("AWS_REGION"),
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY")
    )

def get_llm_response(user_prompt: str, model="anthropic.claude-3-sonnet-20240229-v1:0") -> str:
    client = get_bedrock_client()

    request_body = {
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 300,
        "temperature": 0.7,
        "system": (
            "You are a compassionate and emotionally intelligent AI therapist. "
            "Respond with empathy, validation, and insight based on the user's emotional message."
        ),
        "messages": [
            {"role": "user", "content": user_prompt}
        ]
    }

    response = client.invoke_model(
        modelId=model,
        contentType="application/json",
        accept="application/json",
        body=json.dumps(request_body)
    )

    response_body = json.loads(response["body"].read())
    print("🔍 Raw Response:", json.dumps(response_body, indent=2))

    try:
        return response_body["content"][0]["text"].strip()
    except (KeyError, IndexError):
        return "[Error] Claude response did not contain valid content."
