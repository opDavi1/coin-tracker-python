import requests
import coin
from settings import settings

API_KEY = settings["api_key"]


def get_coin_by_numista_id(numista_id: int):
    response = requests.get(
        "https://api.numista.com/v3/types/" + str(numista_id),
        headers={"Numista-API-Key": API_KEY},
    )

    if response.status_code == 401:
        raise Exception("The API key is missing or incorrect")

    data = response.json()
    print("===== Coin Found: =====")
    print(data)
    print("=======================")
    c = coin.Coin()
    c.numista_id = data["id"]
    c.name = data["title"]
    c.min_year = data["min_year"]
    c.max_year = data["max_year"]
    c.issuer = data["issuer"]["name"]
    c.composition = data["composition"]["text"]
    c.diameter = data["size"]
    c.thickness = data["thickness"]
    c.weight = data["weight"]
    c.denomination = data["value"][""]
    c.value = data["value"]["numeric_value"]
    c.value_numerator = data["value"]["numerator"]
    c.value_denominator = data["value"]["denominator"]
    c.currency = data["value"]["currency"]["name"]
    c.grade = 70
    c.obverse_description = data["obverse"]["description"]
    c.reverse_destription = data["reverse"]["description"]
    c.is_demonitized = data["demonetization"]["is_demonitized"]
    c.comments = data["comments"]
    c.shape = coin.CoinShape[data["shape"].upper()]
    c.orientation = coin.CoinOrientation[data["orientation"].upper()]

    # TODO download image from link provided in response and put the path in
    # these vars:

    # c.obverse_image =
    # c.reverse_image =

    return coin
