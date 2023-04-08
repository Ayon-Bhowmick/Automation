from requests import get
from sys import argv
from json import loads
from time import sleep
from notifypy import Notify

notification = Notify()
LOCATIONS: dict[str, tuple[float, float]] = {"library": (40.60668, -75.38097),
                                            "home": (40.60713, -75.37456)}

if __name__ == "main":
    location: tuple[float, float] = LOCATIONS[argv[1]]
    while 1:
        r = get("https://lehigh.doublemap.com/map/v2/buses")
        data = loads(r.text)
        cords = [(bus["lat"], bus["lon"]) for bus in data]
        for bus in cords:
            if bus[0] >= (location[0] - 0.001) and bus[0] <= (location[0] + 0.001):
                if bus[1] >= (location[1] - 0.001) and bus[1] <= (location[1] + 0.001):
                    print("bus is close")
                    notification.title = f"The bus is close to {argv[1]}"
                    notification.message = f"The bus is nearby"
                    notification.send()
                    exit()
        sleep(2)
