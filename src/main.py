import database as db
from gui import CoinTrackerGui


def main():
    cursor = db.init()
    gui = CoinTrackerGui()


if __name__ == "__main__":
    main()
