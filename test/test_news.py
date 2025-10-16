import requests
import json
import random
from datetime import datetime


def get_news(limit=5):
    """Fetch top headlines (default: 5)."""
    import config

    url = f"http://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey={config.NEWS_API_KEY}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        news_dict = response.json()
        return news_dict.get("articles", [])[:limit]
    except Exception as e:
        print(f"Error fetching news: {e}")
        return []


def get_random_news_for_speech():
    """
    Pick one random headline and make it sound natural for TTS/Jarvis.
    Returns a short conversational string.
    """
    articles = get_news(limit=5)

    if not articles:
        return "I couldn't fetch the latest news right now."

    # Randomly choose one news article
    article = random.choice(articles)

    title = article.get("title", "No title available")
    description = article.get("description") or ""

    # Clean up overly long descriptions
    if len(description) > 150:
        description = description.split(".")[0] + "."

    # Try to get the publish time
    published = article.get("publishedAt", "")
    try:
        pub_time = datetime.fromisoformat(published.replace("Z", "+00:00"))
        time_str = pub_time.strftime("%B %d")
    except Exception:
        time_str = "recently"

    # Casual speech template
    openers = [
        "Here’s something from today’s news.",
        "Here's an update you might find interesting.",
        "Just in from the headlines.",
        "Quick news flash.",
        "Here’s what’s going on right now.",
    ]
    opener = random.choice(openers)

    # Make it sound less robotic
    speak_text = f"{opener} {title}. {description} It was published {time_str}."

    return speak_text


if __name__ == "__main__":
    print(get_random_news_for_speech())
