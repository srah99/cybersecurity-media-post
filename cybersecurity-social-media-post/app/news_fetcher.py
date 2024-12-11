import requests
from app.utils import log_error, log_info
from app.config import NEWS_API_KEY

def fetch_cybersecurity_news():
    url = f"https://newsapi.org/v2/everything?q=cybersecurity&apiKey={NEWS_API_KEY}"

    try:
        log_info("Fetching cybersecurity news from NewsAPI.")
        response = requests.get(url, timeout=10)  # Set a timeout to avoid hanging requests

        # Check if the response status is OK (200)
        if response.status_code == 200:
            news_data = response.json()
            articles = news_data.get('articles', [])
            log_info(f"Successfully fetched {len(articles)} articles.")
            return articles
        else:
            log_error(f"Failed to fetch news. Status code: {response.status_code}")
            return []
    except requests.exceptions.Timeout:
        log_error("Request timed out while fetching news.")
        return []
    except requests.exceptions.RequestException as e:
        log_error(f"An error occurred while fetching news: {e}")
        return []
