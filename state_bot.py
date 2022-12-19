import telebot
from telebot import types
import config
import dbworker
from parser_1 import parse_user_datafile_bs


# Токент бота
TOKEN = '5597125983:AAFcvSuyrWoSHXnNoJTntzYY3kNUd62ucvs'
 
# Создание бота
bot = telebot.TeleBot(TOKEN)


# Начало диалога
@bot.message_handler(commands=['start'])
def cmd_start(message):
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEGfQRje0lu-9ziLvJJI2c1E4CRzYLB3AACLBUAAoGBwUtbO0Y-udNhQSsE')
    dbworker.set(dbworker.make_key(message.chat.id, config.CURRENT_STATE), config.States.STATE_GROUP.value)
    markup = types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='1я группа' , callback_data = 1))
    markup.add(telebot.types.InlineKeyboardButton(text='2я группа' , callback_data = 2))
    markup.add(telebot.types.InlineKeyboardButton(text='3я группа' , callback_data = 3))
    markup.add(telebot.types.InlineKeyboardButton(text='4я группа' , callback_data = 4))
    markup.add(telebot.types.InlineKeyboardButton(text='5я группа' , callback_data = 5))
    bot.send_message(message.chat.id, 'Приветики 2й курс ИУ5, выбери номер группы, чтобы глянуть расписание', reply_markup=markup)


# По команде /reset будем сбрасывать состояния, возвращаясь к началу диалога
@bot.message_handler(commands=['reset'])
def cmd_reset(message):
    bot.send_message(message.chat.id, 'Сбрасываем результаты предыдущего ввода.')
    dbworker.set(dbworker.make_key(message.chat.id, config.CURRENT_STATE), config.States.STATE_GROUP.value)
    markup = types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='1я группа' , callback_data = 1))
    markup.add(telebot.types.InlineKeyboardButton(text='2я группа' , callback_data = 2))
    markup.add(telebot.types.InlineKeyboardButton(text='3я группа' , callback_data = 3))
    markup.add(telebot.types.InlineKeyboardButton(text='4я группа' , callback_data = 4))
    markup.add(telebot.types.InlineKeyboardButton(text='5я группа' , callback_data = 5))
    bot.send_message(message.chat.id, 'Приветики 2й курс ИУ5, выбери номер группы, чтобы глянуть расписание', reply_markup=markup)


# Обработка номера группы
@bot.callback_query_handler(func=lambda call: dbworker.get(dbworker.make_key(call.message.chat.id, config.CURRENT_STATE)) == config.States.STATE_GROUP.value)
def group(call):
    markup2 = types.InlineKeyboardMarkup()
    # Меняем текущее состояние
    dbworker.set(dbworker.make_key(call.message.chat.id, config.CURRENT_STATE), config.States.STATE_DAY.value)
    # Сохраняем первое число
    dbworker.set(dbworker.make_key(call.message.chat.id, config.States.STATE_GROUP.value), call.data)
    markup2.add(telebot.types.InlineKeyboardButton(text='Понедельник' , callback_data = 11))
    markup2.add(telebot.types.InlineKeyboardButton(text='Вторник' , callback_data = 12))
    markup2.add(telebot.types.InlineKeyboardButton(text='Среда' , callback_data = 13))
    markup2.add(telebot.types.InlineKeyboardButton(text='Четверг' , callback_data = 14))
    markup2.add(telebot.types.InlineKeyboardButton(text='Пятница' , callback_data = 15))
    markup2.add(telebot.types.InlineKeyboardButton(text='Суббота' , callback_data = 16))
    markup2.add(telebot.types.InlineKeyboardButton(text='Вернуться к выбору группы' , callback_data = 100))
    bot.send_message(call.message.chat.id, 'Выберите день недели', reply_markup=markup2)


# Обработка второго числа
@bot.callback_query_handler(func=lambda call: dbworker.get(dbworker.make_key(call.message.chat.id, config.CURRENT_STATE)) == config.States.STATE_DAY.value)
def second_num(call):
    # Меняем текущее состояние
    
    if call.data == '100':
        print("------------------------------------------------------------")
        bot.send_sticker(call.message.chat.id, 'CAACAgIAAxkBAAEGfQRje0lu-9ziLvJJI2c1E4CRzYLB3AACLBUAAoGBwUtbO0Y-udNhQSsE')
        dbworker.set(dbworker.make_key(call.message.chat.id, config.CURRENT_STATE), config.States.STATE_GROUP.value)
        markup = types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='1я группа' , callback_data = 1))
        markup.add(telebot.types.InlineKeyboardButton(text='2я группа' , callback_data = 2))
        markup.add(telebot.types.InlineKeyboardButton(text='3я группа' , callback_data = 3))
        markup.add(telebot.types.InlineKeyboardButton(text='4я группа' , callback_data = 4))
        markup.add(telebot.types.InlineKeyboardButton(text='5я группа' , callback_data = 5))
        bot.send_message(call.message.chat.id, 'Приветики 2й курс ИУ5, выбери номер группы, чтобы глянуть расписание', reply_markup=markup)

        
    else:
        dbworker.set(dbworker.make_key(call.message.chat.id, config.CURRENT_STATE), config.States.STATE_DAY.value)
        # Сохраняем первое число
        #dbworker.set(dbworker.make_key(call.message.chat.id, config.States.STATE_GROUP.value), call.data)
        markup2 = types.InlineKeyboardMarkup()
        sh = []
        group = dbworker.get(dbworker.make_key(call.message.chat.id, config.States.STATE_GROUP.value))
        print(group)
        sh = parse_user_datafile_bs('page.html', int(group))
        ch_r =[]
        zn_r = []
        for s in sh[int(call.data) - 11]:
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
        markup2.add(telebot.types.InlineKeyboardButton(text='Вернуться к выбору группы' , callback_data = 100))
        answer = 'Выбери день недели' 
        bot.send_message(call.message.chat.id, answer, reply_markup=markup2)
    
if __name__ == '__main__':
    bot.infinity_polling()