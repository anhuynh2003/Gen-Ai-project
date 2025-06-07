import os
import praw
from dotenv import load_dotenv

load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT")
)

def get_reddit_advice(keyword="life advice", subreddits=["lifeadvice", "DecidingToBeBetter", "GetDisciplined"], limit=3):
    advice = []

    for subreddit in subreddits:
        posts = reddit.subreddit(subreddit).search(keyword, limit=limit * 2, sort="relevance")
        
        for post in posts:
            advice.append(f"🧵 **{post.title}**\n{post.selftext[:300]}...\n[Read more →](https://reddit.com{post.permalink})")
            
            if len(advice) >= limit:
                return advice

    return advice if advice else ["🛑 No relevant Reddit posts found."]
