import telebot

from telebot import types

bot = telebot.TeleBot("7407865143:AAEETcTvdi5voEWXXieyqMg_r5H9owJMg6A")


@bot.message_handler(commands=["start"])
def start(message):
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("От всего сердца, КосмоПривет!🧑‍🚀🤟")
    markup1.add(btn1)
    bot.send_message(message.from_user.id, "🧑‍🚀🤟 КосмоПривет в ответ! Я - VanAk4, робот-помощник с вагоном приколов на любой вкус и цвет! И, безусловно-точно, правая рука нашего Капитана Акыревича.", reply_markup=markup1)


@bot.message_handler(commands=["stop"])
def stop(message):
    markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Пора возвращаться!🫡 ")
    markup2.add(btn1)
    bot.send_message(message.from_user.id, "Ещё свидимся! Доброго пути, КосмоМатрос!", reply_markup=markup2)


@bot.message_handler(content_types=["text"])
def get_text_messages(message):
    if message.text == "От всего сердца, КосмоПривет!🧑‍🚀🤟":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Отправится к истокам!")
        btn2 = types.KeyboardButton("Журнал рекомендаций <El AK>")
        btn3 = types.KeyboardButton("Путеводитель и сборник правил.")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, "Что желаете осмотреть?🕵️", reply_markup=markup)

    elif message.text == "Отправится к истокам!":
        bot.send_message(message.from_user.id, "Ступайте в Хранилище! Великую обитель Приколов и прочей ерунды: " + "[совершить прыжок](https://vk.com/icecreeeaaammm)", parse_mode="Markdown")

    elif message.text == "Журнал рекомендаций <El AK>":
        bot.send_message(message.from_user.id, "На станции сегодня скучновато! К счастью, рядом с вами всегда есть электронный журнальчик: " + "[пролистать журнал](https://vk.com/topic-210642122_49358601)", parse_mode="Markdown")

    elif message.text == "Путеводитель и сборник правил.":
        bot.send_message(message.from_user.id, "Ознакомиться с правилом поведения на Космическом Корабле: " + "[изучить руководство](https://vk.com/topic-210642122_48271410)", parse_mode="Markdown")


bot.polling(none_stop=True, interval=0)  # строка обязательная, чтобы бот не отключался и работал нон-стоп

# завершить сеанс (циклом)
# добавить функционала