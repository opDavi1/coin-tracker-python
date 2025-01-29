import sqlite3

DATABASE_NAME = "cointracker.db"


class Coin:
    def __init__(self):
        self.numista_id = 0
        self.name = ""
        self.year = 0
        self.country = ""


def db_init():
    global sqlite_connection
    sqlite_connection = sqlite3.connect(DATABASE_NAME)
    global cursor
    cursor = sqlite_connection.cursor()
    cursor.execute(
        "CREATE TABLE coins ("
        + "id INTEGER PRIMARY KEY AUTOINCREMENT,"
        + "numista_id INTEGER,"
        + "name TEXT,"
        + "year TEXT,"
        + "country TEXT"
        + ");"
    )


def coin_db_create(coin: Coin):
    cursor.execute(
        f"INSERT INTO coins VALUE ({coin.numista_id}, {coin.name}, {coin.year}, {coin.country});"
    )


def coin_db_read(numista_id: int):
    cursor.execute(f"SELECT * FROM coins WHERE numista_id = {numista_id};")


def coin_db_update(old_coin: Coin, new_coin: Coin):
    cursor.execute(
        "UPDATE coins "
        + f"SET numista_id = {new_coin.numista_id}, name = {new_coin.name}, year = {new_coin.year}, country = {new_coin.country} "
        + f"WHERE id = {old_coin.id};"
    )


def coin_db_delete(coin: Coin):
    cursor.execute(f"DELETE FROM coins WHERE numista_id = {coin.numista_id};")


def main():
    db_init()


if __name__ == "__main__":
    main()
