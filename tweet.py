import tweepy
import os
from datetime import datetime, date, timezone, timedelta
import time

bearer_token = os.getenv('BEARER_TOKEN')
api_key = os.getenv('API_KEY')
api_key_secret = os.getenv('API_KEY_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

client = tweepy.Client(
    bearer_token=bearer_token,
    consumer_key=api_key,
    consumer_secret=api_key_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

IST = timezone(timedelta(hours=5, minutes=30))

def wait_until_target_ist():
    now = datetime.now(IST)
    target_hour = 21  # 9 PM IST — change to 0 for midnight
    target = now.replace(hour=target_hour, minute=0, second=0, microsecond=0)
    if now >= target:
        target += timedelta(days=1)
    wait_seconds = (target - now).total_seconds()

    if 0 < wait_seconds <= 1800:
        print(f"Waiting {wait_seconds:.1f}s until {target_hour}:00 IST...")
        time.sleep(wait_seconds)
    elif wait_seconds <= 0:
        print("Already past target time, posting now.")
    else:
        print(f"WARNING: Too early ({wait_seconds:.0f}s to target). Posting anyway.")

def tweet_countdown():
    wait_until_midnight_ist()

    today_ist = datetime.now(IST).date()
    releaseDate = date(2026, 4, 7)

    if today_ist <= releaseDate:
        daysLeft = (releaseDate - today_ist).days - 1
        tweet = f"{daysLeft}"
        client.create_tweet(text=tweet)
        print("Tweeted:", tweet)
    else:
        print("No more tweets. The release date has passed.")

tweet_countdown()
