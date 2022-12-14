from aiogram import Bot, Dispatcher, executor, types
from config import AllConfigurations
from parser_url import ParserURL

import logging

# инициализация бота
bot = Bot(token=AllConfigurations.TOKEN)
dp = Dispatcher(bot)

# логирование в файл py_log.log в режиме перезаписи при каждом запуске бота с указанием времени
logging.basicConfig(level=logging.INFO, filename='py_log.log', filemode='w', format='%(asctime)s %(levelname)s %(message)s')

# обработка команды /start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    logging.info(f'Пользователь {message.from_user.full_name} активировал бота')
    await bot.send_message(message.from_user.id, AllConfigurations.welcome_text)
    logging.info(f'Бот отправил приветственное сообщение пользователю {message.from_user.full_name}')

# обработка команды /go
@dp.message_handler(commands=['go'])
async def command_go(message: types.Message):
    logging.info(f'Пользователь {message.from_user.full_name} активировал команду /go')
    await bot.send_message(message.from_user.id, AllConfigurations.command_go)
    logging.info(f'Бот отправил ответ пользователю {message.from_user.full_name}')

@dp.message_handler(content_types=['text'])
async def get_a_joke(message: types.Message):
    logging.info(f'Пользователь {message.from_user.full_name} ввёл сообщение {message.text}')
    if message.text.lower() in '1234567890': # текст переводится в нижний регистр. Если пользователь вводит любую цифру
        await bot.send_message(message.from_user.id, ParserURL.list_of_jokes[0]) # отображается анекдот
        del ParserURL.list_of_jokes[0] # после выбора пользователя анекдот удаляется из списка, чтобы в следующий раз он не повторился
    else:
        await bot.send_message(message.from_user.id, AllConfigurations.error_text) # иначе отображается текст


# бот не отвечает на сообщения, которые были отправлены, когда бот был оффлайн
executor.start_polling(dp, skip_updates=True)