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
