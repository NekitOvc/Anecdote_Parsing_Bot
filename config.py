import emoji

class AllConfigurations():
    TOKEN = '' # тут должен быть токен

    welcome_text = emoji.emojize('Привет!:wave: Я бот!\
        \n\nЯ могу тебе улучшить настроение с помощью анекдотов :relieved: Ты готов? Нажми /go', language='alias')

    command_go = emoji.emojize('Отлично!:blush: Напиши мне любую цифру, а я расскажу анекдот.', language='alias')

    error_text = emoji.emojize('Такой команды я не знаю.:neutral_face: Напиши цифру.', language='alias')