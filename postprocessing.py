from TikTokApi import TikTokApi
import csv
from feedgen.feed import FeedGenerator
from datetime import datetime, timezone

# Normal GitHub Pages URL
# ghPagesURL = "https://conoro.github.io/tiktok-rss-flat/"

# Custom Domain
ghPagesURL = "https://8430177.github.io/TikTokRSS/"
count = 10
with open('subscriptions.csv') as f:
    cf = csv.DictReader(f, fieldnames=['username'])
    for row in cf:
        with TikTokApi() as api:
            user = row['username']
            print ("准备开始!!")
            tiktoks = api.user(username=user)
            print("名字:")
            print (tiktoks)
            for video in user.videos():
                print("视频id")
                print(video.id)
            
            
            
