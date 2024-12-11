import tweepy
from app.utils import log_info, log_error

def post_to_x(post, api_key, api_secret_key):
    try:
        auth = tweepy.OAuthHandler(api_key, api_secret_key)
        api = tweepy.API(auth)

        log_info("Attempting to post to X (Twitter).")
        api.update_status(post)
        log_info("Successfully posted to X.")
    
    except tweepy.TweepError as e:
        log_error(f"Error posting to X: {e.response.text}")
    except tweepy.RateLimitError:
        log_error("Rate limit exceeded. Try again later.")
    except tweepy.TweepyException as e:
        log_error(f"Unexpected error with Tweepy: {e}")
    except Exception as e:
        log_error(f"An unexpected error occurred while posting: {e}")
