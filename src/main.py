import sqlite3

NUMISTA_API_KEY = ""
DATABASE_NAME = "cointracker.db"


class Coin:
    def __init__(self):
        self.numista_id = 0
        self.name = ""
        self.year = ""
        self.country = ""
        self.location = ""
        self.issuing_entity = ""
        self.composition = ""
        self.shape = "Round"
        self.diameter = ""
        self.thickness = ""
        self.weight = ""
        self.orientation = ""
        self.denomination = ""
        self.currency = ""
        self.value = ""
        self.coin_type = ""
        self.grade = ""
        self.obverse_description = "Face"
        self.reverse_destription = ""
        self.demonitized = ""
        self.comments = ""

    def default(self):
        self.numista_id = 22995
        self.name = "20 Kreuzers - Francis I"
        self.year = "1829-1830"
        self.country = "Austrian Empire"
        self.location = ""
        self.issuing_entity = "Austrian Empire"
        self.composition = "Silver (.583)"
        self.shape = "Round"
        self.diameter = "27.6 mm"
        self.thickness = "1.16 mm"
        self.weight = "6.68 g"
        self.orientation = "Medal alignment ^^"
        self.denomination = "Kreuzer"
        self.currency = "Gulden"
        self.value = "20 Kreuzers (1/3)"
        self.coin_type = "Standard circulation coins"
        self.grade = ""
        self.obverse_description = "Bust of Franz I flanked by boughs"
        self.reverse_destription = "Double-headed eagle"
        self.demonitized = "Yes"
        self.comments = "There are slight differences between the workshops. The image below, for example, highlights the shift in the legends on the obverse left between A and B, whereas the portraits and branches are almost exactly the same. The writing on B is shifted downwards:"


def db_init():
    global sqlite_connection
    sqlite_connection = sqlite3.connect(DATABASE_NAME)
    global cursor
    cursor = sqlite_connection.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS coins ("
        + "id INTEGER PRIMARY KEY AUTOINCREMENT,"
        + "numista_id INTEGER,"
        + "name TEXT,"
        + "issuing_entity TEXT,"
        + "country TEXT,"
        + "location TEXT,"
        + "year TEXT,"
        + "composition TEXT,"
        + "shape TEXT,"
        + "diameter TEXT,"
        + "thickness TEXT,"
        + "weight TEXT,"
        + "orientation TEXT,"
        + "denomination TEXT,"
        + "currency TEXT,"
        + "value TEXT,"
        + "coin_type TEXT,"
        + "grade TEXT,"
        + "obverse_description TEXT,"
        + "reverse_destription TEXT,"
        + "demonitized TEXT,"
        + "comments TEXT)"
    )
    print("init db")


def coin_db_insert(coin: Coin):
    cursor.execute(
        "INSERT INTO coins (id, numista_id, name, issuing_entity, country, location, year, composition, shape, diameter, thickness, weight, orientation, denomination, currency, value, coin_type, grade, obverse_description, reverse_destription, demonitized, comments) VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        (
            coin.numista_id,
            coin.name,
            coin.issuing_entity,
            coin.country,
            coin.location,
            coin.year,
            coin.composition,
            coin.shape,
            coin.diameter,
            coin.thickness,
            coin.weight,
            coin.orientation,
            coin.denomination,
            coin.currency,
            coin.value,
            coin.coin_type,
            coin.grade,
            coin.obverse_description,
            coin.reverse_destription,
            coin.demonitized,
            coin.comments,
        ),
    )
    sqlite_connection.commit()


def get_coin_by_numista_id(numista_id: int):
    res = cursor.execute("SELECT * FROM coins WHERE numista_id = ?", numista_id)
    return res.fetchone()


# TODO: make this function not ass
def coin_db_update(old_coin: Coin, new_coin: Coin):
    cursor.execute(
        "UPDATE coins "
        + f"SET numista_id = {new_coin.numista_id}, name = {new_coin.name}, year = {new_coin.year}, country = {new_coin.country} "
        + f"WHERE id = {old_coin.id}"
    )
    sqlite_connection.commit()


# TODO: do better.
def coin_db_delete(coin: Coin):
    cursor.execute(f"DELETE FROM coins WHERE numista_id = {coin.numista_id}")


def main():
    db_init()

    coin = Coin()
    coin.default()
    coin_db_insert(coin)
    res = cursor.execute("SELECT * FROM coins")
    print(res.fetchall())


if __name__ == "__main__":
    main()
