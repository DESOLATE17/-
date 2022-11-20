#5597125983:AAFcvSuyrWoSHXnNoJTntzYY3kNUd62ucvs
import os
import telebot
from telebot import types
from parser import parse_user_datafile_bs


# Токент бота
TOKEN = '5597125983:AAFcvSuyrWoSHXnNoJTntzYY3kNUd62ucvs'
 
# Создание бота
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='1я группа' , callback_data = 1))
    markup.add(telebot.types.InlineKeyboardButton(text='2я группа' , callback_data = 2))
    markup.add(telebot.types.InlineKeyboardButton(text='3я группа' , callback_data = 3))
    markup.add(telebot.types.InlineKeyboardButton(text='4я группа' , callback_data = 4))
    markup.add(telebot.types.InlineKeyboardButton(text='5я группа' , callback_data = 5))
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEGefdjed_O7xn-xHhkPfaFd98KoBW7hQAClBgAAvdbgEjPGPx-6kVXrisE')
    bot.send_message(message.chat.id, 'Приветики 2 курс ИУ5, выбери свою группу, чтобы глянуть расписание' , reply_markup=markup)

group = 0

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    global group
    sh = []
    days = ['11', '12', '13', '14', '15', '16']
    markup2 = types.InlineKeyboardMarkup()
    if call.data == '1':
        group = 1
    elif call.data == '2':
        group = 2
    elif call.data == '3':
        group = 3
    elif call.data == '4':
        group = 4
    elif call.data == '5':
        group = 5
    elif call.data in days:
        sh = parse_user_datafile_bs('page.html', group)
        ch_r =[]
        zn_r = []
        for s in sh[int(call.data) %10 - 1]:
            print(s)
            print()
            res1 = []
            res2 = []
            for key in s.keys():
                if key == 'chisl':
                    res1.append(s[key]) 
                elif key == 'znam':
                    res2.append(s[key]) 
                else:
                    res1.append(s[key])
                    res2.append(s[key])
            #print(res1)
            #print()
            #print(res2)       
            if len(res1) > 1:
                ch_r.append(res1)
            if len(res2) > 1:
                zn_r.append(res2)

        bot.send_message(call.message.chat.id, f"Числитель\n")
        for s in ch_r:
            bot.send_message(call.message.chat.id, f"{s[1]}  {s[0]}")
        bot.send_message(call.message.chat.id, f"Знаменатель\n")
        for s in zn_r:
            bot.send_message(call.message.chat.id, f"{s[1]}  {s[0]}")
    markup2.add(telebot.types.InlineKeyboardButton(text='Понедельник' , callback_data = 11))
    markup2.add(telebot.types.InlineKeyboardButton(text='Вторник' , callback_data = 12))
    markup2.add(telebot.types.InlineKeyboardButton(text='Среда' , callback_data = 13))
    markup2.add(telebot.types.InlineKeyboardButton(text='Четверг' , callback_data = 14))
    markup2.add(telebot.types.InlineKeyboardButton(text='Пятница' , callback_data = 15))
    markup2.add(telebot.types.InlineKeyboardButton(text='Суббота' , callback_data = 16))
    answer = 'Выбери день недели' 
    bot.send_message(call.message.chat.id, answer, reply_markup=markup2)
    


bot.infinity_polling()

