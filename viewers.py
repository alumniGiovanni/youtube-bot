import webrowser, time

import requests

url = input("https://www.youtube.com/watch?v=0go-z8wqtDg")
Duration = input(5)

for i in range(5):
  webrowser.open_new(url)
  time.sleep(int(Duration))

    # Wanted a date in my titles so added this helper
    DAY = date.today().strftime("%d")
    DAY = str(int(DAY)) + GetDaySuffix(int(DAY))
    dt_string = date.today().strftime("%A %B") + f" {DAY}"


    # Create the movie itself!
    CreateMovie.CreateMP4(redditbot.post_data)

    # Video info for YouTube.
    # This example uses the first post title.
    video_data = {
            "file": "video.mp4",
            "title": f"{redditbot.post_data[0]['title']} - Dankest memes and comments {dt_string}!",
            "description": "#shorts\nGiving you the hottest memes of the day with funny comments!",
            "keywords":"meme,reddit,Dankestmemes",
            "privacyStatus":"public"
    }

    print(video_data["title"])
    print("Posting Video in 5 minutes...")
    time.sleep(60 * 5)
    upload_video(video_data)

    # Sleep until ready to post another video!

