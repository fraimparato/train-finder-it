import json
import requests as req

MAX_R = 5


def find_d():
    dep_st = input("\nInsert the city (or station name) of departure: ")

    STF_URL = f"""https://www.lefrecce.it/Channels.Website.BFF.WEB/website/\
locations/search?name={dep_st}&limit={MAX_R}"""

    r = req.get(STF_URL)
    data = json.loads(r.text)

    for i in range(min(5, len(data))):
        print(f"{i+1}: {data[i]['displayName']}")

    code = int(input("\nSelect the number of the station you want: "))

    return data[code-1]['id']


def find_a():
    dep_st = input("\nInsert the city (or station name) of arrive: ")

    STF_URL = f"""https://www.lefrecce.it/Channels.Website.BFF.WEB/website/\
locations/search?name={dep_st}&limit={MAX_R}"""

    r = req.get(STF_URL)
    data = json.loads(r.text)

    for i in range(min(5, len(data))):
        print(f"{i+1}: {data[i]['displayName']}")

    code = int(input("\nSelect the number of the station you want: "))

    return data[code-1]['id']
