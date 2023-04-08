from requests import get, post
from sys import argv
import os
from json import loads
from time import sleep
from notifypy import Notify

API_KEY = os.environ["PUSHOVER_API_KEY"]
USER_KEY = os.environ["PUSHOVER_USER_KEY"]
LOCATIONS: "dict[str, tuple[float, float]]" = {"library": (40.60668, -75.38097),
                                               "home": (40.60713, -75.37456)}
RADIUS = 0.001

if __name__ == "main":
    notification = Notify()
    location: "tuple[float, float]" = LOCATIONS[argv[1]]
    while 1:
        r = get("https://lehigh.doublemap.com/map/v2/buses")
        data = loads(r.text)
        cords = [(bus["lat"], bus["lon"]) for bus in data]
        for bus in cords:
            if bus[0] >= (location[0] - RADIUS) and bus[0] <= (location[0] + RADIUS):
                if bus[1] >= (location[1] - RADIUS) and bus[1] <= (location[1] + RADIUS):
                    print("bus is close")
                    payload = {"title": f"The bus is close to {argv[1]}", "message": "The bus is nearby", "user": USER_KEY, "token": API_KEY }
                    post("https://api.pushover.net/1/messages.json", data=payload, headers={'User-Agent': 'Python'})
                    notification.title = f"The bus is close to {argv[1]}"
                    notification.message = f"The bus is nearby"
                    notification.send()
                    exit()
        sleep(2)
