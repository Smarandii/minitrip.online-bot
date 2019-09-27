# coding: utf8
import telebot
import os
import datetime

def date_is_ok(x, n_date):
    s_day = x[:2:]
    s_month = x[3:5:]
    n_day = n_date[:2:]
    n_month = n_date[3::]
    if int(n_month) <= int(s_month):
        return True
    elif int(n_month) == int(s_month) and int(n_day) < int(s_day):
        return True
    else:
        return False    

def del_space(x):
    y = ""
    for i in range(len(x)):
        if x[i-1] == "," and x[i] == " ":
            continue
        else:
            y = y + x[i]
    return y

def stars(n):
    y = ""
    star = "⭐️"
    for i in range(n):
        y = y + star
    return y

def night(x):
    y = ""
    if "+" in x:
        x = int(x[0])
        x = str(x) + "н"
    if x[0] in "123456789" and x[1] in "0123456789":
        x = int(x)
    elif x[1] == "н":
        x = int(x[0])
    if x == 1:
        y = y + str(x) + " ночь"
    elif x == 2 or x == 3 or x == 4:
        y = y + str(x) + " ночи"
    elif 20 >= x >= 5:
        y = y + str(x) + " ночей"
    return y

def country(x):
    y = ""
    m = 0
    k = 0
    for i in range(len(x)):
        if x[i] == ",":
            m = m + 1
        if m == 2:
            k = i
            break
    for i in range(k + 1, len(x)):
        if x[i] != ",":
            y = y + x[i]
        else:
            break
    return y

def city(x):
    y = ""
    m = 0
    k = 0
    for i in range(len(x)):
        if x[i] == ",":
            m = m + 1
        if m == 3:
            k = i
            break
    for i in range(k + 1, len(x)):
        if x[i] != ",":
            y = y + x[i]
        else:
            break
    return y

def hotelf(x):
    hotel = "🏨"
    y = hotel + " "
    m = 0
    k = 0
    for i in range(len(x)):
        if x[i] == ",":
            m = m + 1
        if m == 4:
            k = i
            break
    for i in range(k + 1, len(x)):
        if x[i] == "*":
            continue
        elif x[i] in "12345":
            y = y + stars(int(x[i]))
        elif x[i] != ",":
            y = y + x[i]  
        else:
            break
    return y

def food(x):
    y = ""
    k1 = 0
    k2 = 0
    m = 0
    for i in range(len(x)):
        if x[i] == ",":
            m = m + 1
            k2 = i
            if m == 5:
                k1 = i
    for i in range(k1 + 1, k2):
        y = y + x[i]
    return y

def price(x):
    money = "🌴"
    y = money + " "
    m = 0
    k = 0
    for i in range(len(x)):
        if x[i] == ",":
            k = i
    for i in range(k + 1, len(x)):
        y = y + x[i]
    return y

def do_string(x):
    plane = "🛫"    
    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    c5 = 0
    c6 = 0
    marker = 0
    string = []
    for i in range(len(x)):
        if x[i] == ",":
            marker = marker + 1
        if marker == 1 and c1 == 0:
            tmp = plane + " " + x[:5:]
            string.append(tmp)
            tmp = x[i+1:i+3:]
            string.append(night(tmp))
            c1 = 1
        elif marker == 2 and c2 == 0:
            tmp = country(x)
            string.append(tmp)
            c2 = 1
        elif marker == 3 and c3 == 0:
            tmp = city(x)
            string.append(tmp)
            c3 = 1
        elif marker == 4 and c4 == 0:
            tmp = hotelf(x)
            string.append(tmp)
            c4 = 1
        elif marker == 5 and c5 == 0:
            tmp = food(x)
            string.append(tmp)
            c5 = 1
        elif marker == 6 and c6 == 0:
            tmp = price(x)
            string.append(tmp)
            c6 = 1
    return string

def inpute():
    a = 1
    p = []
    while a != "0":
        a = input()
        p.append(a)
    return p

def get_date():
    dat = datetime.datetime.now()
    month = dat.month
    if len(str(month)) == 1:
        month = "0" + str(month)
    day = dat.day
    return str(day) + "." + str(month)

def parse(r):
    l = ""
    for i in r:
        l = l + i + "\n⠀\n"
    return l

def createSTR(b):
    l = f"{b[0]}, {b[1]}, {b[2]}, {b[3]}\n{b[4]}\n{b[5]}\n{b[6]}\n⠀"
    return l

def main(p, date):
    p_ready = []
    for j in range(len(p)):
        a = p[j]
        if a != "0":

            if date_is_ok(a[:5:], date) and a != "0" and a != "":
                a = del_space(a)
                b = do_string(a)
                p_ready.append(createSTR(b))
    return p_ready  
    
def check_message(p):
    if '\n' in p:
        p = p.split("\n")
        for i in p:
            if ("н" in i) and (i.count(",") >= 6):
                continue
            else:
                return False
        return True
    elif ("н" in p) and (p.count(",") >= 6):
        return True
    else:
        return False

date = get_date()
token = "834347746:AAHqfRcUuq0P-93c_luU8bchDEpNfzlVSEM"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])
def start_message(message):
    if message.text == "/start":
        bot.send_message(message.chat.id, f"Сегодня: {date}")
        bot.send_message(message.chat.id, 'Перед тем как отправлять данные проверьте следующие пункты:\n \n✅ Подборка состоит из строк, в которых порядок данных как в этой строке: \n22.10, 4н, Кемер, Турция, Fortuna Kemer 3*, AI — Завтраки, обеды, ужины + напитки, 27564 RUB')
    if message.text == "/help":
        bot.send_message(message.chat.id, '🛠 Доступные команды:')
        bot.send_message(message.chat.id, '/help')
        bot.send_message(message.chat.id, '/start')
@bot.message_handler(content_types=['text'])
def send_tours(message):
    if check_message(message.text):
        p = message.text + "\n0"
        z = p.split("\n")
        l = ""
        for i in main(z,date):
            l = l + i + "\n"
        l = l[:-2:]
        bot.send_message(message.chat.id, "✅ Обработка завершена!")
        bot.send_message(message.chat.id, l)
    else:
        bot.send_message(message.chat.id, "❌ Данные не соответствуют шаблону!")
        bot.send_message(message.chat.id, "Проверьте построчно введённые данные. Пример правильной строки данных :\n22.10, 4н, Кемер, Турция, Fortuna Kemer 3*, AI — Завтраки, обеды, ужины + напитки, 27564 RUB")
bot.polling()    