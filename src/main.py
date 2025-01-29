# main.py is part of coin_tracker by opDavi1; see LICENSE for details

import database as db
from app import CoinTracker
# from coin import Coin


def main():
    cursor = db.init()

    res = cursor.execute("SELECT * FROM coins")
    print(res.fetchall())

    CoinTracker()


if __name__ == "__main__":
    main()
