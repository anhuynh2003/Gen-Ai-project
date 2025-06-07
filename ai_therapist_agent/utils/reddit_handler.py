import os
import praw
from dotenv import load_dotenv

load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT")
)

def get_reddit_advice(keyword="dating", subreddit="dating_advice", limit=3):
    posts = reddit.subreddit(subreddit).search(keyword, limit=limit, sort="relevance")
    advice = []

    for post in posts:
        advice.append(f"🧵 **{post.title}**\n{post.selftext[:300]}...\n[Read more →](https://reddit.com{post.permalink})")

    return advice if advice else ["No relevant Reddit posts found."]
