import time
import schedule
from chrome import *
import requests
from datetime import datetime, timedelta

def get_time():
    fajr_time = requests.get("https://izr-cloud.online/getPrayers").json()["Fajr"]
    time1 = datetime.strptime(fajr_time,"%H:%M")
    time = time1 - timedelta(minutes=45)
    return time.strftime("%H:%M")

def handle_close_task():
    schedule.clear()
    schedule.every().day.at(get_time()).do(handle_open_task)
    close_browser()
    turn_screen_black()


def handle_open_task():
    turn_screen_on()
    chrome_init()
    open_borwser()




schedule.every().day.at("23:00").do(handle_close_task)


if __name__ == "__main__":
    handle_open_task()
    while True:
        schedule.run_pending()
        time.sleep(1)  # Check for scheduled tasks every second
