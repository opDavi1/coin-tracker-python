# this file is part of coin-tracker by opdavi1 and subject to the GNU GPL-3.0-or-later license.
# See LICENSE for details or go to <https://www.gnu.org/licenses/>

import database as db


example_coin = db.get_coin_by_numista_id(23126)  # 1933 double eagle


def main():
    cursor = db.init()
    res = cursor.execute("SELECT * FROM coins")
    if res.rowcount == 0:
        db.insert_coin(example_coin)

    res = cursor.execute("SELECT * FROM coins")
    print(res.fetchall())


if __name__ == "__main__":
    main()
