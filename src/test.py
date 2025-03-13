# this file is part of coin-tracker by opdavi1 and subject to the GNU GPL-3.0-or-later license.
# See LICENSE for details or go to <https://www.gnu.org/licenses/>

from coin import Coin
from database import Database


example_coin = Coin().default()


def main():
    db = Database()
    db.insert_coin(example_coin)

    coins = db.get_all_coins()
    print(coins)

    db.close()


if __name__ == "__main__":
    main()
