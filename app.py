# -*- coding: utf-8 -*-
import os
import asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from config import AllConfigurations
from logger import setup_logging
from parser_url import list_of_jokes
from connect_db import db_connection, new_user, table_of_jokes, record_responce

load_dotenv(".env.local")
TOKEN = os.getenv("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

logger = setup_logging()

@dp.message(Command("start"))
async def command_start(message: types.Message):
    """Обработка команды /start"""
    logger.info(f"Пользователь {message.from_user.full_name} активировал бота")
    await bot.send_message(message.from_user.id, AllConfigurations.welcome_text)
    logger.info(f"Бот отправил приветственное сообщение пользователю {message.from_user.full_name}")
    await db_connection()
    await new_user(user_id=message.from_user.id, user_name=message.from_user.full_name)
    await table_of_jokes()

@dp.message(Command("go"))
async def command_go(message: types.Message):
    """Обработка команды /go"""
    logger.info(f"Пользователь {message.from_user.full_name} активировал команду /go")
    await bot.send_message(message.from_user.id, AllConfigurations.command_go)
    logger.info(f"Бот отправил ответ пользователю {message.from_user.full_name}")

@dp.message()
async def get_a_joke(message: types.Message):
    """Функция получения анекдота"""
    logger.info(f"Пользователь {message.from_user.full_name} ввёл сообщение {message.text}")

    if message.text.isdigit() and int(message.text) in range(1, 10):
        if list_of_jokes:
            joke = list_of_jokes.pop(0)
            await bot.send_message(message.from_user.id, joke)
            await record_responce([joke])
        else:
            await bot.send_message(message.from_user.id, "Анекдоты закончились.")
    else:
        await bot.send_message(message.from_user.id, AllConfigurations.error_text)

async def start_polling():
    try:
        print("Осуществлён запуск бота")
        logger.info("Осуществлён запуск бота")
        await dp.start_polling(bot)
    except asyncio.CancelledError:
        print("Polling был отменен.")
        logger.warning("Polling был отменен.")
    except KeyboardInterrupt:
        print("Бот остановлен.")
        logger.warning("Бот остановлен.")
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(start_polling())