# this file is part of coin-tracker by opdavi1 and subject to the GNU GPL-3.0-or-later license.
# See LICENSE for details or go to <https://www.gnu.org/licenses/>

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
