import json
import requests as req
import station_finder as sf

URL = "https://www.lefrecce.it/Channels.Website.BFF.WEB/website/ticket\
/solutions"
HEADER = {"Content-Type": "application/json"}


def help():
    print("""tfi: Train Finder Italy

tfi [option]

Options:
    --help, -h: show this page
    --search-solution -s: search for a solution
    --is-present -p [id#]: checks whether a train (with id: id#) is present \
in a solution
    """)


def base_info_in():
    dep = sf.find_d()
    arr = sf.find_a()

    date = input("Insert the date (in the format YYYY-MM-DD): ")
    time = input("""Insert the time (in the format HH:MM, please use UTC)\
 zone: """)

    return [dep, arr, date, time]


def search_solution():
    params = base_info_in()
    pl = f"""
{{
    "departureLocationId": {params[0]},
    "arrivalLocationId": {params[1]},
    "departureTime": "{params[2]}T{params[3]}:00.000+00:00",
    "adults": 1,
        "children": 0,
        "criteria": {{
            "frecceOnly": false,
            "regionalOnly": false,
            "noChanges": false,
            "order": "DEPARTURE_DATE",
                "limit": 10,
            "offset": 0
        }},
        "advancedSearchRequest": {{
            "bestFare": false
        }}
}}
"""

    payload = json.loads(pl)
    r = req.post(URL, headers=HEADER, json=payload)
    with open("res.json", "w") as f:
        f.write(r.text)


def is_present():
    print("To be written")
