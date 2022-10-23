import requests as req
import station_finder as sf


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

    return [dep, arr]


def search_solution():
    params = base_info_in()
    print(params)


def is_present():
    print("To be written")
