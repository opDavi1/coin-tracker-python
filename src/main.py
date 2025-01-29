import database as db
from coin import Coin


def main():
    cursor = db.init()

    coin = Coin().default()
    db.insert_coin(coin)

    coin2 = Coin()
    db.insert_coin(coin2)

    res = cursor.execute("SELECT * FROM coins")
    print(res.fetchall())


if __name__ == "__main__":
    main()
