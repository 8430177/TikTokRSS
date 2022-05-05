from TikTokApi import TikTokApi
import csv
from feedgen.feed import FeedGenerator
from datetime import datetime, timezone

# Normal GitHub Pages URL
# ghPagesURL = "https://conoro.github.io/tiktok-rss-flat/"

# Custom Domain
ghPagesURL = "https://8430177.github.io/TikTokRSS/"
count = 10
with TikTokApi() as api:
    print("准备开始!!!!")
    user = api.user(username="therock")
    print(user)
    for video in user.videos():
        print("video.id")
        print(video.id)
    print("中间进行!!!!")
    for liked_video in api.user(username="public_likes").videos():
        print("liked_video.id")
        print(liked_video.id)
          
