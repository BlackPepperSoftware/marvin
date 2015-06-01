import time
import random
import os
from apiclient.discovery import build

# Set DEVELOPER_KEY to the "API key" value from the "Access" tab of the
# Google APIs Console http://code.google.com/apis/console#access
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = os.environ.get("MARVIN_GOOGLE_API_KEY")
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
RANDOM_CHANNEL_ID = os.environ.get("MARVIN_SLACK_CHANNEL_ID")
WHATS_GOING_ON_URL = "https://www.youtube.com/watch?v=H-kA3UtBj4M"
outputs = []

def process_message(data):
    channel = data["channel"]
    if channel.startswith(RANDOM_CHANNEL_ID) or channel.startswith("D"):
        if "text" in data:
            text = data["text"]
            if "What's going on?".lower() in text.lower():
                outputs.append([channel, WHATS_GOING_ON_URL])
            elif any(music in text.lower() for music in ("music", "song", "love", "dance", "mood")):
                outputs.append([channel, youtube_search("Marvin Gaye -ft -feat", 25)])
            elif "play some" in text.lower():
                queryString = text.lower().split("play some",1)[1]
                outputs.append([channel, youtube_search(queryString, 25)])

def youtube_search(query, maxResults):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)

    search_response = youtube.search().list(
        q=query,
        part="id",
        maxResults=maxResults,
        order="viewCount",
        type="video",
        videoDuration="short"
    ).execute()

    videos = []

    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            videos.append("https://www.youtube.com/watch?v=%s" % search_result["id"]["videoId"])

    return random.choice(videos)
