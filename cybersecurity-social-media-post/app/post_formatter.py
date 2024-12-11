from app.utils import log_error

def format_post(news_articles):
    try:
        if not news_articles:
            raise ValueError("No articles available to format.")

        article = news_articles[0]
        title = article.get('title', 'No Title')
        url = article.get('url', '#')
        description = article.get('description', 'No Description')[:200]  # Shorten if necessary

        post = f"{title} - {description} {url}"
        return post
    except Exception as e:
        log_error(f"Error formatting post: {e}")
        return "Error: Could not generate post content."
