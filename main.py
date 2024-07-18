import telebot
from telebot import types

BOT_TOKEN = "7407865143:AAEETcTvdi5voEWXXieyqMg_r5H9owJMg6A"

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["start"])
def start(message):
    first_mess = ("От всего сердца, КосмоПривет!🧑‍🚀🤟 "
                  "\nЯ - VanAk4, робот-помощник с вагоном приколов на любой вкус и цвет! "
                  "И, безусловно-точно, правая рука нашего Капитана Акыревича.")
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text="Открыть журнал исследований🕵️", callback_data="mag_yes")
    btn2 = types.InlineKeyboardButton(text="МемСинтМашин", callback_data="mem_sm")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, first_mess, parse_mode="html", reply_markup=markup)


@bot.callback_query_handler(func=lambda call:True)
def response(function_call):
    if function_call.message:
        if function_call.data == "mag_yes":
            second_mess = ("Журнал исследований открыт! "
                           "\nЗдесь вы можете найти для себя различные ресурсы для просмотра бесплатного контента по СКЗ."
                           "\n📑ГиперФикс-2022 - Пристанище Капитана Акыревича, где он проводил своё собственное расследования СКЗ-звёзд и баловался форматом мп4 в личное пользование."
                           "\n📑МежГалоЕды - личный сборник Капитана Акыревича на фикбук, который хранит в себе небольшое количество приятного чтива для любителей крепкой мужской дружбы."
                           "\n📑Архив On-Расслабон - ютуб-канал легендарного человека, который собрал воедино все транляции СКЗ,"
                           "включая те, что хранились на VLive, дак ещё и перевёл их на английский язык. "
                           "\n📑ККП - Официальный канал СКЗ, а именно страница на их плейлисты, для более глубокого погружения в Стейвиль.")
            markup = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton(text="ГиперФикс-2022", url="https://vk.com/icecreeeaaammm")
            btn2 = types.InlineKeyboardButton(text="МежГалоЕды", url="https://ficbook.net/collections/26150258")
            btn3 = types.InlineKeyboardButton(text="Архив ON-Расслабон", url="https://www.youtube.com/@stayk23")
            btn4 = types.InlineKeyboardButton(text="ККП", url="https://www.youtube.com/@StrayKids/playlists")
            markup.add(btn1, btn2, btn3, btn4)
            bot.send_message(function_call.message.chat.id, second_mess, reply_markup=markup)
            bot.answer_callback_query(function_call.id)

        elif function_call.data == "mem_sm":
            third_mess = "На станции сегодня скучновато... \nО, вам пришло сообщение от Капитана! \nОткрываю?"
            markup1 = types.InlineKeyboardMarkup()
            btn1 = types.InlineKeyboardButton(text="Открыть!")
            markup1.add(btn1)
            # bot.send_photo()
            bot.answer_callback_query(function_call.id)


@bot.message_handler(commands=["stop"])
def stop(message):
    markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Ещё свидимся!🫡 ")
    markup2.add(btn1)
    bot.send_message(message.from_user.id, "...", reply_markup=markup2)


@bot.message_handler(commands=["help"])
def help(message):
    markup3 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bot.send_message(message.from_user.id, "...", reply_markup=markup3)


if __name__ == "__main__":
    print("Бот готов к работе! Leggo!")
    bot.infinity_polling()



# @bot.message_handler(content_types=["text"])
# def get_text_message(message):
    # if message.text == "От всего сердца, КосмоПривет!🧑‍🚀🤟":
        # btn4 = types.KeyboardButton("Скрасить ожидание на КосмоПалубе")  # игры
        # markup.add(btn1, btn2, btn3, btn4)
        # bot.send_message(message.from_user.id, "Что желаете осмотреть?🕵️", reply_markup=markup)

    # elif message.text == "Отправится к истокам!":
        # bot.send_message(message.from_user.id, ans_one, parse_mode="Markdown")









