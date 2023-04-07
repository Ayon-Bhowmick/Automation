from requests import get
from sys import argv
from json import loads
from time import sleep

ALUMNI_BUILDING = (40.60668, -75.38097)

if argv[1] == "library":
    while 1:
        r = get("https://lehigh.doublemap.com/map/v2/buses")
        data = loads(r.text)
        cords = [(bus["lat"], bus["lon"]) for bus in data]
        print(cords)
        for bus in cords:
            if bus[0] >= (ALUMNI_BUILDING[0] - 0.001) and bus[0] <= (ALUMNI_BUILDING[0] + 0.001):
                if bus[1] >= (ALUMNI_BUILDING[1] - 0.001) and bus[1] <= (ALUMNI_BUILDING[1] + 0.001):
                    print("bus is close")
                    exit()
        sleep(2)
