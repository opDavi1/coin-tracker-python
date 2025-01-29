import settings
import database as db
from gui import CoinTrackerGui


def main():
    settings.init()
    cursor = db.init()
    gui = CoinTrackerGui()

    res = cursor.execute("SELECT * FROM coins")
    print(res.fetchall())


if __name__ == "__main__":
    main()
