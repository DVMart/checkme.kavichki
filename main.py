from bs4 import BeautifulSoup
import psycopg2
from config import host, user, password, db_name

url = "/home/bear/Documents/kavichki/checkme.kavichki.com.html"

with open(url) as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")

user_name = soup.find_all("tr")

print(user_name)

for item in user_name:
    print(item.text)

# =================================================
try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )

        print(f"Server version: {cursor.fetchone()}")


    with connection.cursor() as cursor:
        cursor.execute(
            """INSERT INTO checkme (item, quantity, amount, action) VALUES
            ()"""
        )

        print("[INFO] Data was successfully inserted")


except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")

