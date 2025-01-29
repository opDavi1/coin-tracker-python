import database as db
from gui import CoinTrackerGui


def main():
    cursor = db.init()

    res = cursor.execute("SELECT * FROM coins")
    print(res.fetchall())
    gui = CoinTrackerGui()


if __name__ == "__main__":
    main()
