from selenium import webdriver
import time
number_of_drivers = int(input("Drivers : " ))
time_to_refresh = int(input("Refresh: " ))
url = input("URL: " )
drivers =[]
for i in range(number_of_drivers):
    drivers.append(webdriver.Chrome(executable_path = "chromedriver"))
    drivers[i].get(url)
while True:
    time.sleep(time_to_refresh)
    for i in range(number_of_drivers):
        drivers[i].refresh()