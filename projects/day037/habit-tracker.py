from datetime import datetime

import random
import requests

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
PIXELA_WEBSITE = "https://pixe.la"

username = ""
token = ""
graphid = ""

leave = False


def setleave():
    global leave
    leave = True


def createuser():
    global username, token
    u = input("Username: ")
    t = input("Token (Password): ")
    endpoint = PIXELA_ENDPOINT
    params = {
        "username": u,
        "token": t,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }
    response = requests.post(url=endpoint, json=params)
    rjson = response.json()
    if rjson["isSuccess"] == "true":
        username = u
        token = t
    print(rjson["message"])


def loaduser():
    global username, token, graphid
    username = input("Username: ")
    token = input("Token: ")


def changeuser():
    global username, token, graphid
    username = ""
    token = ""


def userurl():
    print(f"{PIXELA_WEBSITE}/@{username}")


def creategraph():
    global graphid
    i = input("Unique ID: ")
    endpoint = f"{PIXELA_ENDPOINT}/{username}/graphs"
    params = {
        "id": i,
        "name": input("Name: "),
        "unit": input("Unit (e.g. km, pages, hours): "),
        "type": input("Type (int for integer, float for decimal): "),
        "color": random.choice(["shibafu", "momiji", "sora", "ichou", "ajisai", "kuro"])
    }
    headers = {"X-USER-TOKEN": token}
    response = requests.post(url=endpoint, json=params, headers=headers)
    rjson = response.json()
    if rjson["isSuccess"] == "true":
        graphid = i
    print(response.json()["message"])


def loadgraph():
    global graphid
    graphid = input("Graph ID: ")


def changegraph():
    global graphid
    graphid = ""


def graphurl():
    print(f"{PIXELA_ENDPOINT}/{username}/graphs/{graphid}.html")


def createpixel():
    d = input("Date (YYYY-MM-DD)(Leave empty for today): ")
    ok = False
    while not ok:
        if d == "":
            d = datetime.now()
            ok = True
        else:
            try:
                arr = d.split("-")
                arr = [int(v) for v in arr]
                d = datetime(year=arr[0], month=arr[1], day=arr[2])
            except IndexError:
                d = input("Date (YYYY-MM-DD)(Leave empty for today): ")
            else:
                ok = True
    endpoint = f"{PIXELA_ENDPOINT}/{username}/graphs/{graphid}"
    params = {
        "date": d.strftime("%Y%m%d"),
        "quantity": input("Quantity: ")
    }
    headers = {"X-USER-TOKEN": token}
    response = requests.post(url=endpoint, json=params, headers=headers)
    print(response.json()["message"])


def updatepixel():
    d = input("Date (YYYY-MM-DD)(Leave empty for today): ")
    ok = False
    while not ok:
        if d == "":
            d = datetime.now()
        else:
            try:
                arr = d.split("-")
                arr = [int(v) for v in arr]
                d = datetime(year=arr[0], month=arr[1], day=arr[2])
            except IndexError:
                d = input("Date (YYYY-MM-DD)(Leave empty for today): ")
            else:
                ok = True
    endpoint = f"{PIXELA_ENDPOINT}/{username}/graphs/{graphid}/{d.strftime('%Y%m%d')}"
    params = {
        "quantity": input("Quantity: ")
    }
    headers = {"X-USER-TOKEN": token}
    response = requests.put(url=endpoint, json=params, headers=headers)
    print(response.json()["message"])


def deletepixel():
    d = input("Date (YYYY-MM-DD)(Leave empty for today): ")
    ok = False
    while not ok:
        if d == "":
            d = datetime.now()
        else:
            try:
                arr = d.split("-")
                arr = [int(v) for v in arr]
                d = datetime(year=arr[0], month=arr[1], day=arr[2])
            except IndexError:
                d = input("Date (YYYY-MM-DD)(Leave empty for today): ")
            else:
                ok = True
    endpoint = f"{PIXELA_ENDPOINT}/{username}/graphs/{graphid}/{d.strftime('%Y%m%d')}"
    headers = {"X-USER-TOKEN": token}
    response = requests.delete(url=endpoint, headers=headers)
    print(response.json()["message"])


while not leave:
    actions = {
        "0": setleave
    }
    if username == "" or token == "":
        actions["1"] = createuser
        actions["2"] = loaduser
        print("Actions")
        print("0. Exit")
        print("1. Create user")
        print("2. Load existing user")
    elif graphid == "":
        actions["1"] = creategraph
        actions["2"] = loadgraph
        actions["3"] = userurl
        actions["4"] = changeuser
        print(f"User: {username}")
        print("Actions")
        print("0. Exit")
        print("1. Create graph")
        print("2. Load existing graph")
        print("3. Get user URL")
        print("4. Change user")
    else:
        actions["1"] = createpixel
        actions["2"] = updatepixel
        actions["3"] = deletepixel
        actions["4"] = graphurl
        actions["5"] = changeuser
        actions["6"] = changegraph
        print(f"User: {username}")
        print(f"Graph: {graphid}")
        print("Actions")
        print("0. Exit")
        print("1. Create pixel")
        print("2. Update pixel")
        print("3. Delete pixel")
        print("4. Get graph URL")
        print("5. Change user")
        print("6. Change graph")
    action = input("Choose an action: ")
    actions[action]()
    print("")
