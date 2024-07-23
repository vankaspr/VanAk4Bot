import telebot

from telebot import types
from bot_token import BOT_TOKEN

import random
import os

from text import second_mess, bot_instruct

bot = telebot.TeleBot(BOT_TOKEN)


img_folder = 'D:/web/personal/VanAk4Bot/pythonProject/img'
files = [os.path.join(img_folder, f) for f in os.listdir(img_folder)
         if f.endswith('.jpg')]

# os.path.join(img_folder, f) полный путь к каждому файлу в директории
# os.listdir(img_folder) список всех файлов в директории
# for f in os.listdir(img_folder)
#          if f.endswith('.jpg') - цикл по каждому элементу в списке при условии, что этот файл .jpg
# files = [...] список


@bot.message_handler(commands=["start"])
def start(message):
    first_mess = ("От всего сердца, КосмоПривет!🧑‍🚀🤟 "
                  "\nЯ - VanAk4, робот-помощник с вагоном приколов на любой вкус и цвет! "
                  "И, безусловно-точно, правая рука нашего Капитана Акыревича.")
    markup = types.InlineKeyboardMarkup()
    bt1 = types.InlineKeyboardButton(text="Журнал Исследований", callback_data="bt1")
    bt2 = types.InlineKeyboardButton(text="МемСинтМашин", callback_data="bt2")
    bt3 = types.InlineKeyboardButton(text="БотИнструкт", callback_data="bt3")
    bt4 = types.InlineKeyboardButton(text="Квизовик", callback_data="bt4")
    markup.add(bt1, bt2, bt3, bt4)
    bot.send_message(message.chat.id, first_mess, reply_markup=markup, parse_mode="html")


@bot.message_handler(commands=["back"])
def back(message):
    back_mess = "Вернуться на главную панель?"
    markup = types.InlineKeyboardMarkup()
    back_btn = types.InlineKeyboardButton(text="Yappy!", callback_data="back")
    markup.add(back_btn)
    bot.send_message(message.chat.id, back_mess, parse_mode="html", reply_markup=markup)


@bot.message_handler(commands=["help"])
def help(message):
    help_mess = "Нужна помощь в управлении?"
    markup = types.InlineKeyboardMarkup()
    help_btn = types.InlineKeyboardButton(text="Yappy!", callback_data="help")
    markup.add(help_btn)
    bot.send_message(message.chat.id, help_mess, parse_mode="html", reply_markup=markup)


@bot.callback_query_handler(func=lambda call:True)
def response(call):
    if call.message:
        if call.data == "bt1":
            keyboard = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton(text="KKП", url="https://www.youtube.com/@StrayKids/playlists")
            btn2 = types.InlineKeyboardButton(text="Архив ON-Расслабон", url="https://www.youtube.com/@stayk23")
            btn3 = types.InlineKeyboardButton(text="МежГалоЕды", url="https://ficbook.net/collections/26150258")
            btn4 = types.InlineKeyboardButton(text="ГиперФикс-2022", url="https://vk.com/icecreeeaaammm")
            keyboard.add(btn1, btn2, btn3, btn4)
            bot.send_message(call.message.chat.id, second_mess, reply_markup=keyboard)
            bot.answer_callback_query(call.id)

        elif call.data == "bt2":
            third_mess = ("На станции сегодня скучновато... \nО, кажется наш Капитан собирается развеселить вас! "
                          "\nПримите свою порцию КосмоХохмы!📩")
            photo = open(random.choice(files), 'rb')
            # rb read binary - для чтения бинарных файлов, например, изображений
            bot.send_message(call.message.chat.id, third_mess)
            bot.send_photo(call.message.chat.id, photo)
            bot.answer_callback_query(call.id)

        elif call.data == "bt3":
            for_mess = ("Это руководство по эксплуатации бота, чтобы и вам удобно, и мне полезно!"
                        "\n"
                        "\nVanAk4Bot - простой в использовании бот со своими приколами, созданный по воле случая "
                        "и с доброй душой. Этот бот некоммерческого издания и не несёт никакой услады для капиталистов,"
                        "это лишь детище одного Капитана по фамилии Акыре, который уж слишком любит бойзбэнд бродячих "
                        "детей и систематизировать все полученные им ссылки и информацию в одну понятную кучу."
                        "\n\nОсторожно, много текста! ")
            keyboard = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton(text="Изучить!", callback_data="btn1")  # dont work
            keyboard.add(btn1)
            bot.send_message(call.message.chat.id, for_mess, reply_markup=keyboard)
            bot.answer_callback_query(call.id)

        elif call.data == "btn1":  # кнопка для изучить, которая кидает гайд с text.py
            bot.send_message(call.message.chat.id, bot_instruct)
            bot.answer_callback_query(call.id)

        elif call.data == "help":  # кнопка вызова подсказок
            bot.send_message(call.message.chat.id, "/start - начинает работу бота,"
                                                   "\n /back - возвращает к приветственному сообщению,"
                                                   "\n /help - кидает подсказки"
                                                   "\n Все подсказки есть в Menu в левом нижнем углу :)")
            bot.answer_callback_query(call.id)

        elif call.data == "back":
            start(call.message)  # возвращает к стартовому сообщению

        elif call.data == "bt4":
            five_mess = "Кто вы из персонажей акыречной аушки под названием 'Лягушка и стрекоза'?"
            keyboard = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton(text="Сквизнуть🤸🏻", url="https://uquiz.com/j0Ek0E")
            keyboard.add(btn1)
            bot.send_message(call.message.chat.id, five_mess, reply_markup=keyboard)
            bot.answer_callback_query(call.id)


if __name__ == "__main__":
    print("Бот готов к работе! Leggo!")
    bot.infinity_polling()
