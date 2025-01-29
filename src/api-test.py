import requests

API_KEY = ""
NUMISTA_ID = 1337


def main():
    response = requests.get(
        "https://api.numista.com/v3/types/" + NUMISTA_ID,
        headers={"Numista-API-Key": API_KEY}
    )

    if response.status_code == 401:
        raise Exception("The API key is missing or incorrect")

    search_result = response.json()
    print("===== Coin Found: =====")
    print(search_result)

    with open("result.json", "w") as f:
        f.write(search_result)


if __name__ == "__main__":
    main()
