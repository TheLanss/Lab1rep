cursor.execute("INSERT INTO subject_t (name) VALUES ('Алгебра и Геометрия');")
cursor.execute("INSERT INTO teacher_t (full_name, subject) VALUES ('Азовая Александра Афанасьева', 'Алгебра и Геометрия');")
cursor.execute("INSERT INTO teacher_t (full_name, subject) VALUES ('Важаемова Рина Александровна', 'Алгебра и Геометрия');")
cursor.execute("INSERT INTO timetable_t (day, subject, room_numb, start_time, teacher) VALUES (1, 'Алгебра и Геометрия', 406, 1, 'Азовая Александра Афанасьева');")
cursor.execute("INSERT INTO timetable_t (day, subject, room_numb, start_time, teacher) VALUES (6, 'Алгебра и Геометрия', 406, 2, 'Важаемова Рина Александровна');")
cursor.execute("INSERT INTO timetable_t (day, subject, room_numb, start_time, teacher) VALUES (12, 'Алгебра и Геометрия', 504, 3, 'Азовая Александра Афанасьева');")

cursor.execute("INSERT INTO subject_t (name) VALUES ('Компьютерная графика');")
cursor.execute("INSERT INTO teacher_t (full_name, subject) VALUES ('Арбузова Олеся Михайловна', 'Компьютерная графика');")
cursor.execute("INSERT INTO timetable_t (day, subject, room_numb, start_time, teacher) VALUES (1, 'Компьютерная графика', 511, 2, 'Арбузова Олеся Михайловна');")
cursor.execute("INSERT INTO timetable_t (day, subject, room_numb, start_time, teacher) VALUES (3, 'Компьютерная графика', 223, 1, 'Арбузова Олеся Михайловна');")
cursor.execute("INSERT INTO timetable_t (day, subject, room_numb, start_time, teacher) VALUES (9, 'Компьютерная графика', 511, 4, 'Арбузова Олеся Михайловна');")

cursor.execute("INSERT INTO subject_t (name) VALUES ('Физическая культура и спорт');")
cursor.execute("INSERT INTO teacher_t (full_name, subject) VALUES ('Царёв Олег Михайлович', 'Физическая культура и спорт');")
cursor.execute("INSERT INTO timetable_t (day, subject, room_numb, start_time, teacher) VALUES (1, 'Физическая культура и спорт', 232, 3, 'Царёв Олег Михайлович');")
cursor.execute("INSERT INTO timetable_t (day, subject, room_numb, start_time, teacher) VALUES (4, 'Физическая культура и спорт', 232, 3, 'Царёв Олег Михайлович');")
cursor.execute("INSERT INTO timetable_t (day, subject, room_numb, start_time, teacher) VALUES (10, 'Физическая культура и спорт', 232, 3, 'Царёв Олег Михайлович');")
cursor.execute("INSERT INTO timetable_t (day, subject, room_numb, start_time, teacher) VALUES (12, 'Физическая культура и спорт', 232, 2, 'Царёв Олег Михайлович');")

cursor.execute("INSERT INTO subject_t (name) VALUES ('Введение в ИТ');")
cursor.execute("INSERT INTO teacher_t (full_name, subject) VALUES ('Преподаватель 404', 'Введение в ИТ');")
cursor.execute("INSERT INTO teacher_t (full_name, subject) VALUES ('Белгородова Тамара Ивановна', 'Введение в ИТ');")
cursor.execute("INSERT INTO timetable_t (day, subject, room_numb, start_time, teacher) VALUES (3, 'Введение в ИТ', 329, 2, 'Преподаватель 404');")
cursor.execute("INSERT INTO timetable_t (day, subject, room_numb, start_time, teacher) VALUES (5, 'Введение в ИТ', 404, 3, 'Преподаватель 404');")
cursor.execute("INSERT INTO timetable_t (day, subject, room_numb, start_time, teacher) VALUES (5, 'Введение в ИТ', 306, 4, 'Белгородова Тамара Ивановна');")
cursor.execute("INSERT INTO timetable_t (day, subject, room_numb, start_time, teacher) VALUES (8, 'Введение в ИТ', 451, 4, 'Преподаватель 404');")
cursor.execute("INSERT INTO timetable_t (day, subject, room_numb, start_time, teacher) VALUES (9, 'Введение в ИТ', 221, 3, 'Преподаватель 404');")

cursor.execute("INSERT INTO subject_t (name) VALUES ('Вычтех');")
cursor.execute("INSERT INTO teacher_t (full_name, subject) VALUES ('Азотая Александра Афанасьева', 'Вычтех');")
cursor.execute("INSERT INTO teacher_t (full_name, subject) VALUES ('Жердин Павел Виссарионович', 'Вычтех');")
cursor.execute("INSERT INTO timetable_t (day, subject, room_numb, start_time, teacher) VALUES (3, 'Вычтех', 512, 3, 'Азотая Александра Афанасьева');")
cursor.execute("INSERT INTO timetable_t (day, subject, room_numb, start_time, teacher) VALUES (8, 'Вычтех', 512, 2, 'Жердин Павел Виссарионович');")
cursor.execute("INSERT INTO timetable_t (day, subject, room_numb, start_time, teacher) VALUES (8, 'Вычтех', 512, 3, 'Азотая Александра Афанасьева');")
cursor.execute("INSERT INTO timetable_t (day, subject, room_numb, start_time, teacher) VALUES (10, 'Вычтех', 223, 4, 'Азотая Александра Афанасьева');")


cursor.execute("INSERT INTO subject_t (name) VALUES ('Иностранный язык');")
cursor.execute("INSERT INTO teacher_t (full_name, subject) VALUES ('Нелапин Нетигран Нельвович', 'Иностранный язык');")
cursor.execute("INSERT INTO timetable_t (day, subject, room_numb, start_time, teacher) VALUES (6, 'Иностранный язык', 404, 3, 'Нелапин Нетигран Нельвович');")
cursor.execute("INSERT INTO timetable_t (day, subject, room_numb, start_time, teacher) VALUES (10, 'Иностранный язык', 404, 2, 'Нелапин Нетигран Нельвович');")


conn.commit()



sides = [3,2,4,7,5,12,11,13,15,16,14,14]
sides = sorted(sides,reverse=True)
smax = 0
for i in range(len(sides)):
    for j in range(i+1,len(sides)):
        for k in range(j+1,len(sides)):
            a = sides[i]
            b = sides[j]
            c = sides[k]
            if a + b > c and a + c > b and b + c >a:
                p = (a+b+c)/2
                s = (p*(p-a)*(p-b)*(p-c))**(1/2)
                if s > smax:
                    smax = s
print('Maks ploshad treuga', smax)


import telebot
from telebot import types
import psycopg2
from datetime import date

token = "5948988656:AAGGp3WONAnlSLSXKney2iMSO6D4-FdUsrE"
bot = telebot.TeleBot(token=token)

conn = psycopg2.connect(database="tg_raspis_db", user="postgres", password="vvitpass",
                        host="localhost", port="5432") # подключение к БД
cursor = conn.cursor()

date_start = date(2022, 9, 5)
week_type = date.today() - date_start
week_type = week_type.days // 7

pair_time = {1: "9:30", 2: "11:20", 3: "13:10", 4: "15:25"}
week_days = {1: "Понедельник", 2: "Вторник", 3: "Среда", 4: "Четверг", 5: "Пятница", 6: "Суббота"}

def send_message(message, bot_msg):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("a. Понедельник", "b. Вторник", "c. Среда", "d. Четверг", "e. Пятница")
    keyboard.row("f. Расписание на текущую неделю", "g. Расписание на следующую неделю")
    bot.send_message(message.chat.id, bot_msg, reply_markup=keyboard)

def day_raspis(day, plus_week=False):
    global week_type
    if not week_type:
        day += 7
    if plus_week:
        day += 7
        day %= 14
    cursor.execute(f"select * from timetable_t where day = {day};")
    records = list(map(lambda x: x[1:], list(cursor.fetchall())))
    records.sort(key=lambda x: x[3])
    return records


@bot.message_handler(commands=['start'])
def starting(message):
    text = f"Здравствуйте, {message.from_user.first_name + ' ' + message.from_user.last_name}!\n Для получения информации о работе бота используйте команду /help!"
    send_message(message, text)

@bot.message_handler(commands=['help'])
def helping(message):
    text = """Здравствуйте! Добро пожаловать в бот-расписание БФИ2202!
Для получения доступа к расписанию дней текущей недели - используйте ввод формата алфавитный_номер_дня_недели. День_недели
Для получения доступа ко всему расписанию текущей недели - f. Расписание на текущую неделю
Для получения доступа ко всему расписанию следующей недели - g. Расписание на следующую неделю
Для получения ссылки на сайт Московского Технического Университета Связи и Информатики - используйте команду /mtuci
Для того, чтобы узнать, верхняя сейчас или нижняя неделя - используйте команду /week

Форма вывода расписания - Предмет | Кабинет | Время | Преподаватель
 
Приятного использования бота!
"""
    send_message(message, text)


@bot.message_handler(commands=['mtuci'])
def mtuci_site(message):
    send_message(message, "https://mtuci.ru")


@bot.message_handler(commands=['week'])
def what_week(message):
    global week_type
    week_type = date.today() - date_start
    week_type = week_type.days // 7
    send_message(message, "Верхняя" if week_type else "Нижняя")

@bot.message_handler(content_types=['text'])
def text_obr(message):
    if message.text == "a. Понедельник":
        rasp = day_raspis(1)
        text = "ПОНЕДЕЛЬНИК\n" + "-" * 7 + '\n'
        for x in rasp:
            text += x[1] + ' | ' + str(x[-3]) + ' | ' + pair_time[x[3]] + ' | ' + str(x[2]) + ' | ' + x[-1] + '\n'
        text += "-" * 7 + '\n'
        send_message(message, text)
    elif message.text == "b. Вторник":
        rasp = day_raspis(2)
        text = "ВТОРНИК\n" + "-" * 7 + '\n'
        for x in rasp:
            text += x[1] + ' | ' + str(x[-3]) + ' | ' + pair_time[x[3]] + ' | ' + str(x[2]) + ' | ' + x[-1] + '\n'
        text += "-" * 7 + '\n'
        send_message(message, text)
    elif message.text == "c. Среда":
        rasp = day_raspis(3)
        text = "СРЕДА\n" + "-" * 7 + '\n'
        for x in rasp:
            text += x[1] + ' | ' + str(x[-3]) + ' | ' + pair_time[x[3]] + ' | ' + str(x[2]) + ' | ' + x[-1] + '\n'
        text += "-" * 7 + '\n'
        send_message(message, text)
    elif message.text == "d. Четверг":
        rasp = day_raspis(4)
        text = "ЧЕТВЕРГ\n" + "-" * 7 + '\n'
        for x in rasp:
            text += x[1] + ' | ' + str(x[-3]) + ' | ' + pair_time[x[3]] + ' | ' + str(x[2]) + ' | ' + x[-1]+ '\n'
        text += "-" * 7 + '\n'
        send_message(message, text)
    elif message.text == "e. Пятница":
        rasp = day_raspis(5)
        text = "Пятница\n" + "-" * 7 + '\n'
        for x in rasp:
            text += x[1] + ' | ' + str(x[-3]) + ' | ' + pair_time[x[3]] + ' | ' + str(x[2]) + ' | ' + x[-1] + '\n'
        text += "-" * 7 + '\n'
        send_message(message, text)
    elif message.text == "f. Расписание на текущую неделю":
        text = "Ваше расписание на текущую неделю:\n\n"
        for i in range(1, 7):
            rasp = day_raspis(i)
            text += week_days[i] + '\n' + '-' * 7 + '\n'
            for x in rasp:
                text += x[1] + ' | ' + str(x[-3]) + ' | ' + pair_time[x[3]] + ' | ' + str(x[2]) + ' | ' + x[-1] + '\n'
            text += "-" * 7 + '\n\n'
        send_message(message, text)
    elif message.text == "g. Расписание на следующую неделю":
        text = "Ваше расписание на следующую неделю:\n\n"
        for i in range(1, 7):
            rasp = day_raspis(i, plus_week=True)
            text += week_days[i] + '\n' + '-' * 7 + '\n'
            for x in rasp:
                text += x[1] + ' | ' + str(x[-3]) + ' | ' + pair_time[x[3]] + ' | ' + str(x[2]) + ' | ' + x[-1] + '\n'
            text += "-" * 7 + '\n\n'
        send_message(message, text)
    else:
        send_message(message, "Извините, я Вас не понял.")


bot.polling(none_stop=True, interval=0)
