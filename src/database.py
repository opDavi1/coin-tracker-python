import sqlite3
from coin import Coin


NUMISTA_API_KEY = ""
DATABASE_NAME = "coin_database.db"


def init():
    global sqlite_connection
    sqlite_connection = sqlite3.connect(DATABASE_NAME)
    global cursor
    cursor = sqlite_connection.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS coins ("
        + "id INTEGER PRIMARY KEY AUTOINCREMENT,"
        + "numista_id INTEGER,"
        + "name TEXT NOT NULL,"
        + "coin_type INT,"
        + "issuer TEXT,"
        + "country TEXT,"
        + "min_year INT,"
        + "max_year INT,"
        + "composition TEXT,"
        + "shape INT,"
        + "diameter REAL,"
        + "thickness REAL,"
        + "weight REAL,"
        + "orientation INT,"
        + "denomination TEXT,"
        + "value REAL,"
        + "value_numerator INT,"
        + "value_denominator INT,"
        + "currency TEXT,"
        + "grade INT,"
        + "obverse_image TEXT,"
        + "reverse_image TEXT,"
        + "obverse_description TEXT,"
        + "reverse_destription TEXT,"
        + "is_demonitized INT,"
        + "comments TEXT)"
    )
    print("init db")
    return cursor


def insert_coin(coin: Coin):
    cursor.execute(
        "INSERT INTO coins (id, numista_id, name, coin_type, issuer, country, min_year, max_year, composition, shape, diameter, thickness, weight, orientation, denomination, value, value_numerator, value_denominator, currency, grade, obverse_image, reverse_image, obverse_description, reverse_destription, is_demonitized, comments) VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        (
            coin.numista_id,
            coin.name,
            coin.coin_type.value,
            coin.issuer,
            coin.country,
            coin.min_year,
            coin.max_year,
            coin.composition,
            coin.shape.value,
            coin.diameter,
            coin.thickness,
            coin.weight,
            coin.orientation.value,
            coin.denomination,
            coin.value,
            coin.value_numerator,
            coin.value_denominator,
            coin.currency,
            coin.grade,
            coin.obverse_image,
            coin.reverse_image,
            coin.obverse_description,
            coin.reverse_destription,
            coin.is_demonitized,
            coin.comments,
        ),
    )
    sqlite_connection.commit()


def get_coin_by_numista_id(numista_id: int):
    res = cursor.execute("SELECT * FROM coins WHERE numista_id = ?", numista_id)
    return res.fetchone()


# TODO: make this function not ass
def update_coin(old_coin: Coin, new_coin: Coin):
    cursor.execute(
        "UPDATE coins "
        + f"SET numista_id = {new_coin.numista_id}, name = {new_coin.name}, year = {new_coin.year}, country = {new_coin.country} "
        + f"WHERE id = {old_coin.id}"
    )
    sqlite_connection.commit()


# TODO: do better.
def delete_coin(coin: Coin):
    cursor.execute(f"DELETE FROM coins WHERE numista_id = {coin.numista_id}")
