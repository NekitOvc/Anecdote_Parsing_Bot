import sqlite3
import logging

# подключение БД
async def db_connection():
    global connection, cursor
    connection = sqlite3.connect('db.db')
    cursor = connection.cursor()
    logging.info('Подключение к БД произошло успешно')

    # если таблицы users не существует, создать её
    cursor.execute('CREATE TABLE IF NOT EXISTS users(user_id TEXT PRIMARY KEY, name TEXT)')
    connection.commit()
    logging.info('Создана таблица users')
    

# запись нового пользователя
async def new_user(user_id, user_name):
    user = cursor.execute('SELECT 1 FROM users WHERE user_id == "{key}"'.format(key=user_id)).fetchone()
    
    # если пользователя не существует в БД
    if not user:
        # осуществляется запись в БД
        cursor.execute('INSERT INTO users VALUES(?, ?)', (user_id, user_name))
        connection.commit()
        logging.info(f'Пользователь {user_name} успешно внесён в БД')

# если таблицы anecdotes не существует, создать её
async def table_of_jokes():
    cursor.execute('CREATE TABLE IF NOT EXISTS anecdotes(column VARCHAR)')
    connection.commit()
    logging.info('Создана таблица anecdotes')

# запись анекдота в БД
async def record_responce(column):
    cursor.execute('INSERT INTO anecdotes VALUES(?)', (column))

    connection.commit()
    logging.info('Анекдот внесён в БД')
    