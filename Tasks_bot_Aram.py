from random import choice
import telebot
from first_telegram_bot import token

Token = token
bot = telebot.TeleBot(Token)

RANDOM_TASKS = ['Написать Гвидо письмо', 'Выучить Python', 'Записаться на курс в Нетологию', 'Посмотреть 4 сезон Рик и Морти']

tasks = {}

HELP = '''Список доступных команд:
/print  - напечать все задачи на заданную дату, для этого: 
введите команду в формате /print дата дата дата
/show - вывести одну задачу на заданную дату, для этого: 
введите команду в формате /show дата
/random - добавить на сегодня случайную задачу, для этого: 
введите команду в формате /random
/help - Напечатать help
/add - Добавить команду, для этого: введите команду в формате /add дата сама - задача
'''

def add_task(date, task):
  if date in tasks:
      # Дата есть в словаре
      # Добавляем в список задачу
      tasks[date].append(task)
  else:
      # Даты в словаре нет
      # Создаем запись с ключом даты и добавляем задачу на эту дату
      tasks[date] = []
      tasks[date].append(task)


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, HELP)

# @bot.message_handler(commands=['add']) #№№№№№№№№№№№№№№№ Проверка
# def add(message):
#     bot.send_message(message.chat.id, "Команду принял")
#     print((message.text)) # ==> /add 11.02 make a bot of tasks

@bot.message_handler(commands=['add'])
def add(message):
    texted = message.text.split(maxsplit=2)
    date = texted[1].lower()
    task = texted[2]
    if len(task) >= 3:
        add_task(date, task)
        bot.send_message(message.chat.id, f'Задача {task} добавлена на дату {date}')
    else:
        wrong = 'Задача состоящая менее чем из трёх символов не может быть добавлена.'
        print(wrong)
        bot.send_message(message.chat.id, wrong)

@bot.message_handler(commands=['random'])
def random(message):
    date = 'сегодня'
    task = choice(RANDOM_TASKS)
    add_task(date, task)
    text = f'Задача {task} добавлена на {date}'
    bot.send_message(message.chat.id, text)
 

@bot.message_handler(commands=['show'])
def show(message):
    date_show = message.text.split(maxsplit=1)
    date = date_show[1].lower()
    text = ""
    if date in tasks:
        text = date.upper() + '\n'
        for task in tasks[date]:
            text = f"{text} [] {task} \n"
    else:
        text = 'Такой даты нет'
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['print'])
def print(message):
    date_tasks = message.text.split()
    # date = date_tasks[1].lower()
    dates = date_tasks[1:]
    for date in dates:
        date = date.lower()
        text = ""
        if date in tasks:
            text = date.upper() + '\n'
            for task in tasks[date]:
                text = f"{text} [] {task} \n"
            bot.send_message(message.chat.id, text)
        else:
            text = 'Такой даты нет'
            bot.send_message(message.chat.id, text)
        


bot.polling(none_stop=True)