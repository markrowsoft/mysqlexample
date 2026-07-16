import os
import pprint as pp

import mysql.connector


def connect(host, user, password, database):
    """Connect to MySQL and return a connection object."""
    return mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database,
    )


def insert_user(cursor, first_name, last_name, phone, social):
    """Insert a user row. Returns the number of rows inserted."""
    sql = (
        "INSERT INTO user_tb (first_name, last_name, phone, social) "
        "VALUES (%s, %s, %s, %s);"
    )
    values = (first_name, last_name, phone, social)
    cursor.execute(sql, values)
    return cursor.rowcount


def fetch_users_by_first_name(cursor, first_name):
    """Return all user rows matching first_name."""
    select_sql = "SELECT * FROM `user_tb` WHERE `first_name`=%s;"
    cursor.execute(select_sql, (first_name,))
    return cursor.fetchall()


def main():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    phone = input("Enter your phone number: ")
    social = input("Enter your social security number: ")

    host = os.environ.get("MYSQL_HOST", "127.0.0.1")
    user = os.environ.get("MYSQL_USER", "root")
    password = os.environ.get("MYSQL_PASSWORD", "root")
    database = os.environ.get("MYSQL_DATABASE", "myusers")

    mydb = connect(host, user, password, database)
    mycursor = mydb.cursor()
    try:
        rowcount = insert_user(mycursor, first_name, last_name, phone, social)
        mydb.commit()
        print(rowcount, "record inserted.")
        data = fetch_users_by_first_name(mycursor, first_name)
        pp.pprint(data)
    finally:
        mycursor.close()
        mydb.close()


if __name__ == "__main__":
    main()
