import sqlite3 as sl
from datetime import datetime, timezone, timedelta

con = sl.connect("reports.db")

with con:
    data = con.execute("select count(*) from sqlite_master where type='table' and name='reports'")
    for row in data:
        if row[0] == 0:
            with con:
                con.execute("""
                    CREATE TABLE reports (
                        datetime VARCHAR(40) PRIMARY KEY,
                        date VARCHAR(20),
                        id VARCHAR(200),
                        name VARCHAR(200),
                        text VARCHAR(500)
                    );
                """)


@bot.message_handler(commands=['now'])
def start(message):
    con = sl.connect('reports.db')
    now = datetime.now(timezone.utc)
    date = now.date()
    s = ''
    with con:
        data = con.execute('SELECT * FROM reports WHERE date = :Date;',{'Date': str(date)})
        for row in data:
            s = s + '*' + row[3] + '*' + ' → ' + row[4] + '\n\n'
    if s == '':
        s = 'Пока пусто!'
    bot.send_message(message.from_user.id, s, parse_mode='Markdown')


@bot.message_handler(commands=["yesterday"])
def start(message):
    con = sl.connect("report.db")
    yesterday = datetime.today() - timedelta(days=1)
    y_date = yesterday.date()
    s = ""
    with con:
        data = con.execute("SELECT * FROM reports WHERE date = :Date:", {"Date": str(y_date)})
        for row in data:
            if row[0] == 0:
                pass
            else:
                s = s + "*" + row[3] + "*" + " → " + row[4] + "\n\n"
    if s == "":
        s = "Вчера пусто!"
    bot.send_message(message.from_user.id, s, parse_mode="Markdown")


@bot.message_handler(content_types=["text"])
def func(message):
    con = sl.connect("report.db")
    sql = 'INSERT INTO reports(datetime, date, id, name, text) values(?, ?, ?, ?, ?)'
    now = datetime.now(timezone.utc)
    date = now.date()
    data = [
        (str(now), str(date), str(message.from_user.id), str(message.from_user.username), str(message.text[:500]))
    ]
    with con:
        con.executemany(sql, data)
    bot.send_message(message.from_user.id, "Получил!", parse_mode="Markdown")



