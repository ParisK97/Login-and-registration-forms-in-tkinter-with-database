import sqlite3


# create table for the database
def create_table() ->None:
    connection = sqlite3.connect('user_information.db')
    cursor = connection.cursor()

    command = '''CREATE TABLE IF NOT EXISTS user_info (
    Username TEXT PRIMARY KEY NOT NULL,
    Email TEXT NOT NULL,
    Name TEXT,
    Password TEXT NOT NULL CHECK (LENGTH(Password) > 8),
    Confirm_password TEXT NOT NULL
    )
    '''

    cursor.execute(command)

    connection.commit()
    connection.close()

# insert data into database 
def insert_data(data: tuple) -> None:
    connection = sqlite3.connect('user_information.db')
    cursor = connection.cursor()

    cursor.execute('INSERT INTO user_info VALUES (?, ?, ?, ?, ?)', data)

    connection.commit()
    connection.close()

def retrive_data() -> list:
    connection = sqlite3.connect('user_information.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM user_info')

    return cursor.fetchall()



create_table()

