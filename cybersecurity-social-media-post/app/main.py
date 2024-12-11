from app.news_fetcher import fetch_cybersecurity_news
from app.post_formatter import format_post
from app.poster import post_to_x
from app.config import API_KEY, API_SECRET_KEY
from app.utils import log_info, log_error

def create_post():
    try:
        log_info("Starting the process to create and post content.")
        
        # Fetch news from API
        news = fetch_cybersecurity_news()
        if not news:
            log_error("No news fetched. Aborting post creation.")
            return
        
        # Format the post content
        post = format_post(news)
        if "Error" in post:
            log_error(f"Post formatting failed: {post}")
            return
        
        # Post the content to X (Twitter)
        post_to_x(post, API_KEY, API_SECRET_KEY)
    
    except Exception as e:
        log_error(f"An error occurred in the main process: {e}")

if __name__ == "__main__":
    create_post()
