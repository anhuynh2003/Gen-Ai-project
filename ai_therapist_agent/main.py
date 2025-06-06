
from dotenv import load_dotenv
import os
from utils.llm_handler import get_llm_response

load_dotenv()

print("🧠 Claude says:")
print(get_llm_response("I feel lost and overwhelmed lately."))

