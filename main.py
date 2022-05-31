import requests
import datetime
import time
from plyer import notification

while(True):
    notification.notify(
        title="Break Notification : {}".format(datetime.date.today()),
        message="You have been working for last two hours. So please take a break for 10 minutes, take a tea and keep " 
                "yourself fresh and active",
        timeout=50
    )
    # Set Timer to show notification after 2 hours
    time.sleep(60*60*2)
