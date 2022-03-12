from telebot import TeleBot  # Подключаем библиотеку
import telebot
from telebot import apihelper

import time
bot = TeleBot('1639149114:AAFgRtctE2CklrtTTy9r7-F4P_jYWZppvSs')  # Записываем токен

bad_words = ["жопа", "дурак", "мудак", "durak"]  # Словарь для фраз которые мы будем автоматически удалять из чата

other_lang = ["c#", "c++", "дельфи", " ява ", "java", "php", " пхп", "swift", " свифт", " go ",
              "javascript", "kotlin", " котлин", "rust", " раст ", "basic", " бейсик", " паскаль",
              "golang", "pascal", "delphi", "perl", " перл ", "1c", " делфи", " си "]
# Словарь для фраз на которыем мы будем реагировать стикером

other_bot = ["aiogram", "аиограм"]  # Еще один словарь для фраз на которыем мы будем реагировать стикером




@bot.message_handler(
    content_types=['new_chat_members'])  # Хендлер описывающий поведение бота при добавлении нового пользователя
def greeting(message):  # Запуско основной функции хендлера
    #print("User " + message.new_chat_member.last_name + " added")  # Выводим в консоль имя нового пользователя
    try:  # Пытаемся выполнить команду приведеную ниже
        bot.reply_to(message, text='Приветствую тебя в нашем серпентарии. Будь вежливым, и мы постараемся тебе помочь!'
                     , disable_notification=True)  # Выводим приветствие в чат
    except OSError:  # Игнорируем ошибку по таймауту, если телеграмм успел разорвать соединение сс времени прошлой сесии
        print("GreetingError - Sending again after 5 seconds!!!")  # Выводим ошибку в консоль
        time.sleep(3)  # Делаем паузу в 3 секунды и выполняем команду приведеную ниже
        bot.reply_to(message, text='Приветствую тебя в нашем серпентарии. Будь вежливым, и мы постараемся тебе помочь!'
                     , disable_notification=True)  # Выводим приветствие в чат



@bot.message_handler(
    content_types=['left_chat_member'])  # Хендлер описывающий поведение бота при выходе пользователя из чата
def not_greeting(message):  # Запуско основной функции хендлера
    print("User " + message.left_chat_member.first_name + " left")  # Выводим в консоль имя ушедшего пользователя
    try:  # Пытаемся выполнить команду приведеную ниже
        bot.reply_to(message, text='Как жаль, что вы наконец-то уходите...',
                     disable_notification=True)  # Выводим прощание в чат
    except OSError:  # Игнорируем ошибку по таймауту, если телеграмм успел разорвать соединение сс времени прошлой сесии
        print("LeftError - Sending again after 5 seconds!!!")  # Выводим ошибку в консоль
        time.sleep(3)  # Делаем паузу в 3 секунды и выполняем команду приведеную ниже
        bot.reply_to(message, text='Как жаль, что вы наконец-то уходите...',
                     disable_notification=True)  # Выводим прощание в чат



@bot.message_handler(commands=['start'])  # Хендлер описывающий поведение бота при вводе /start
def starting(message):  # Запуско основной функции хендлера
    try:  # Пытаемся выполнить команду приведеную ниже
        bot.reply_to(message, text='Ты мне тут не стартуй!', disable_notification=True)  # Отвечаем на команду /start
    except OSError:  # Игнорируем ошибку по таймауту, если телеграмм успел разорвать соединение сс времени прошлой сесии
        print("StartingError - Sending again after 3 seconds!!!")  # Выводим ошибку в консоль
        time.sleep(3)  # Делаем паузу в 3 секунды и выполняем команду приведеную ниже
        bot.reply_to(message, text='Ты мне тут не стартуй!', disable_notification=True)  # Отвечаем на команду /start



@bot.message_handler(commands=['help'])  # Хендлер описывающий поведение бота при вводе help
def helper(message):  # Запуско основной функции хендлера
    try:  # Пытаемся выполнить команду приведеную ниже
        bot.reply_to(message, text='я тебя не понял. я могу вот что:ну например .... я хочу спать', disable_notification=True)  # Отвечаем на команду /help
    except OSError:  # Игнорируем ошибку по таймауту, если телеграмм успел разорвать соединение сс времени прошлой сесии
        print("HelperError - Sending again after 3 seconds!!!")  # Выводим ошибку в консоль
        time.sleep(3)  # Делаем паузу в 3 секунды и выполняем команду приведеную ниже
        bot.reply_to(message, text='Гугл в помощь!', disable_notification=True)  # Отвечаем на команду /help


@bot.message_handler(content_types=['voice'])  # Хендлер описывающий поведение бота при голосовом сообщении в чате
def voice_msg(message):  # Запуско основной функции хендлера
    try:  # Пытаемся выполнить команду приведеную ниже
        jpg_pic = open('voice.webp', 'rb')  # Открывем стикер и присваиваем его переменной
        bot.send_sticker(message.chat.id, jpg_pic, reply_to_message_id=message.message_id,
                         disable_notification=True)  # Отправляем стикер
    except OSError:  # Игнорируем ошибку по таймауту, если телеграмм успел разорвать соединение сс времени прошлой сесии
        print("Audio_msgError - Sending again after 3 seconds!!!")  # Выводим ошибку в консоль
        time.sleep(3)  # Делаем паузу в 3 секунды и выполняем команду приведеную ниже
        jpg_pic = open('voice.webp', 'rb')  # Открывем стикер и присваиваем его переменной
        bot.send_sticker(message.chat.id, jpg_pic, reply_to_message_id=message.message_id,
                         disable_notification=True)  # Отправляем стикер


@bot.message_handler(
    content_types=['pinned_message'])  # Хендлер описывающий поведение бота после того, как было закрепленно сообщение
def pinned_msg(message):  # Запуско основной функции хендлера
    try:  # Пытаемся выполнить команду приведеную ниже
        bot.reply_to(message, text='Ну, теперь заживем!',
                     disable_notification=True)  # Отвечаем на закрепленное сообщение
    except OSError:  # Игнорируем ошибку по таймауту, если телеграмм успел разорвать соединение сс времени прошлой сесии
        print("PinnedError - Sending again after 3 seconds!!!")  # Выводим ошибку в консоль
        time.sleep(3)  # Делаем паузу в 3 секунды и выполняем команду приведеную ниже
        bot.reply_to(message, text='Ну, теперь заживем',
                     disable_notification=True)  # Отвечаем на закрепленное сообщение


@bot.message_handler(content_types=['text'])  # Хендлер описывающий поведение бота на текст в чате
def txt(message):  # Запуско основной функции хендлера
    for i in range(0, len(bad_words)):  # Перебираем все элементы словаря по очереди
        if bad_words[i] in message.text.lower():  # Проверяем наличие каждого слова из нашего словаря в сообщении
            try:  # Пытаемся выполнить команду приведеную ниже
                bot.delete_message(message.chat.id, message.message_id, )  # Удаляем сообщение
                print(message.text + " delited")  # Выводим удаленное сообщение в консоль
            except OSError:  # Игнорируем ошибку по таймауту, если телеграмм успел разорвать соединение сс времени прошлой сесии
                print("BadWordsError - Sending again after 3 seconds!!!")  # Выводим ошибку в консоль
                time.sleep(3)  # Делаем паузу в 3 секунды и выполняем команду приведеную ниже
                bot.delete_message(message.chat.id, message.message_id)  # Удаляем сообщение
                print(message.text + " delited")  # Выводим удаленное сообщение в консоль
    if '/add' in message.text.lower():  # Проверяем наличие каждого слова из нашего словаря в сообщении
        try:  # Пытаемся выполнить команду приведеную ниже
            new_word = str(message.text.split(' '))
            bad_words.append(new_word[10:-2])
            print(new_word[10:-2])  # Выводим удаленное сообщение в консоль
            print(bad_words)
        except OSError:  # Игнорируем ошибку по таймауту, если телеграмм успел разорвать соединение сс времени прошлой сесии
            print("BadWordsError - Sending again after 3 seconds!!!")  # Выводим ошибку в консоль
            time.sleep(3)  # Делаем паузу в 3 секунды и выполняем команду приведеную ниже
            print(message.text + " delited")  # Выводим удаленное сообщение в консоль

@bot.message_handler(content_types=['audio'])  # Хендлер описывающий поведение бота при добавлении аудиофайла в чат
def audio_msg(message):  # Запуско основной функции хендлера
    try:  # Пытаемся выполнить команду приведеную ниже
        jpg_pic = open('002.jpg', 'rb')  # Открывем изображение и присваиваем его переменной
        bot.send_sticker(message.chat.id, jpg_pic, reply_to_message_id=message.message_id,
                         disable_notification=True)  # Отправляем изображение
    except OSError:  # Игнорируем ошибку по таймауту, если телеграмм успел разорвать соединение сс времени прошлой сесии
        print("Audio_msgError - Sending again after 3 seconds!!!")  # Выводим ошибку в консоль
        time.sleep(3)  # Делаем паузу в 3 секунды и выполняем команду приведеную ниже
        jpg_pic = open('002.jpg', 'rb')  # Открывем изображение и присваиваем его переменной
        bot.send_sticker(message.chat.id, jpg_pic, reply_to_message_id=message.message_id,
                         disable_notification=True)  # Отправляем изображение




@bot.message_handler(commands=['go'])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Привет', 'Пока','/test')
    bot.send_message(message.chat.id, 'Привет!', reply_markup=keyboard)

@bot.message_handler(commands=['test'])
def start_message(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='Три(3)', callback_data=3))
    markup.add(telebot.types.InlineKeyboardButton(text='Четыре(4)', callback_data=4))
    markup.add(telebot.types.InlineKeyboardButton(text='Пять(5)', callback_data=5))
    bot.send_message(message.chat.id, text="Какая средняя оценка была у Вас в школе? Только честно)", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Мы уже здоровались)')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощались уже )')

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):

    bot.answer_callback_query(callback_query_id=call.id, text='Молодец!Спасибо за ответ!')
    answer = ''
    if call.data == '3':
        answer = 'Вы троечник, ай ай ай )!'
    elif call.data == '4':
        answer = 'Вы хорошист! это хорошо)'
    elif call.data == '5':
        answer = 'Вы отличник! ВОТ ЭТО КРУТО))'

    bot.send_message(call.message.chat.id, answer)
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

bot.polling()

if __name__ == '__main__':  # Блок запуска бота
    try:  # Пытаемся выполнить команду приведеную ниже
        bot.polling(none_stop=True)  # Запускаем бота
    except OSError:  # Игнорируем ошибку по таймауту, если телеграмм успел разорвать соединение сс времени прошлой сесии
        print("PollingError - Sending again after 5 seconds!!!")  # Выводим ошибку в консоль
        time.sleep(5)  # Делаем паузу в 5 секунд и выполняем команду приведеную ниже
        bot.polling(none_stop=True)  # Запускаем бота












































