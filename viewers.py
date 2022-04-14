import webrowser, time
url = input("https://www.youtube.com/watch?v=0go-z8wqtDg")
Duration = input(5)

for i in range(5):
  webrowser.open_new(url)
  time.sleep(int(Duration))
