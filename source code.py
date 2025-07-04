import time

from plyer import notification
# install plyer if it not avaliable
def remind_to_drink_water():
    while True:
        notification.notify(
            title="Time to Drink Water",
            message="Stay hydrated—take a sip now!",
           app_icon = "D:\drinking water  remainder\glassofwater_84019 (1).png",
            timeout=10
        )
        time.sleep(60*60)  # waits 1 houror or can change

if __name__ == "__main__":
