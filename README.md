# Anecdote_Parsing_Bot
https://t.me/Anecdote_Parsing_Bot - телеграм бот, который производит парсинг сайта с анекдотами, затем отправляет пользователю по запросу анекдот. Реализовано логирование в файл `py_log.log` и создание базы данных `db.db` с двумя таблицами:
1. `users` - таблица пользователей, работающих с ботом
2. `anecdotes` - список анекдотов, отправленных ботом пользователю

Используемые библиотеки:
- aiogram
- aiosqlite
- emoji
- requests
- beautifulsoup4
- python-dotenv
- logging
