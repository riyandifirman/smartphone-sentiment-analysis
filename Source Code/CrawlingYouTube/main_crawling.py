from youtube_comment_scraper_python import *
import pandas as pd

link = input("Youtube links: ")
saved = input("Output name: ")
youtube.open(link)

all_data = []
for i in range(0, 30): # It will scroll 10 times
    response = youtube.video_comments()
    data = response['body']
    all_data.extend(data)

df = pd.DataFrame(data)
df.to_csv(saved)