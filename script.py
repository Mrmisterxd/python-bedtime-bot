import telebot
import os
import time
from telebot import types

bot = telebot.TeleBot('here_you_token')

is_sleep = False

@bot.message_handler(commands=['start'])
def main(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('Information')
    button2 = types.KeyboardButton('Pc control')
    markup.add(button1)
    markup.add(button2)
    bot.send_message(message.chat.id, 'Hello! this is bot for bedtime and off you PC!', reply_markup=markup)

@bot.message_handler()

def on_click(message):
    if message.text == 'Information':
        bot.send_message(message.chat.id, "Say /start to reboot bot")

    elif message.text == 'Pc control':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)        
        button3 = types.KeyboardButton('Off pc')
        button4 = types.KeyboardButton('Set bedtime in seconds')
        button5 = types.KeyboardButton('Set bedtime in minutes')
        button6 = types.KeyboardButton('Set bedtime in hours')
        button7 = types.KeyboardButton('Turn off bedtime')
        button8 = types.KeyboardButton('Check bedtime')
        markup.add(button3)
        markup.add(button4)
        markup.add(button5)
        markup.add(button6)
        markup.add(button7)
        markup.add(button8)
        bot.send_message(message.chat.id, "Choice:", reply_markup=markup)

    elif message.text == 'Off pc':
        bot.clear_step_handler_by_chat_id(chat_id=message.chat.id) 
        user_accept(message)

    elif message.text == 'Set bedtime in seconds':
        bot.clear_step_handler_by_chat_id(chat_id=message.chat.id) 
        bot.send_message(message.chat.id, "Set time in seconds (1 hour - 3600 seconds)")
        seconds = bot.send_message(message.chat.id, 'Enter seconds: ')
        bot.register_next_step_handler(seconds, set_seconds)

    
    elif message.text == 'Set bedtime in minutes':
        bot.clear_step_handler_by_chat_id(chat_id=message.chat.id) 
        bot.send_message(message.chat.id, "Set bedtime in minutes (decimal values allowed, f.e. 2.5)")
        minutes = bot.send_message(message.chat.id, 'Enter minutes: ')
        bot.register_next_step_handler(minutes, set_minutes)


    elif message.text == 'Set bedtime in hours':
        bot.clear_step_handler_by_chat_id(chat_id=message.chat.id) 
        bot.send_message(message.chat.id, 'Set bedtime in hours (decimal values allowed, e.g. 1.5)')
        hours = bot.send_message(message.chat.id, 'Enter hours: ')
        bot.register_next_step_handler(hours, set_hours)

    elif message.text == 'Turn off bedtime':
        bot.clear_step_handler_by_chat_id(chat_id=message.chat.id) 
        global is_sleep
        os.system("shutdown -a")      
        bot.send_message(message.chat.id, 'Bedtime cancelled')
        is_sleep = False
        main(message)
    
    elif message.text == 'Check bedtime':
        bot.clear_step_handler_by_chat_id(chat_id=message.chat.id) 
        check_sleep(message)
        
def set_seconds(message):
    global is_sleep
    try:
        seconds = int(message.text)
        if seconds < 0:
            bot.send_message(message.chat.id, "You can't turn off the computer in the past!")
            main(message)
            return        
        os.system(f"shutdown -s -f -t {seconds}")
        is_sleep = True
        bot.send_message(message.chat.id, f"PC will off in {seconds} seconds")
        main(message)
    except ValueError:
        msg = bot.send_message(message.chat.id, "Error: Enter a number")
        bot.register_next_step_handler(msg, set_seconds)

def set_minutes(message):
    global is_sleep
    try:
        minutes = float(message.text)
        minutes_seconds = int(60 * minutes)
        if minutes < 0:
            bot.send_message(message.chat.id, "You can't turn off the computer in the past!")
            main(message)
            return        
        os.system(f"shutdown -s -f -t {minutes_seconds}")
        is_sleep = True
        bot.send_message(message.chat.id, f"PC will off in {minutes} minutes")
        main(message)
    except ValueError:
        msg = bot.send_message(message.chat.id, "Error: Enter a number")
        bot.register_next_step_handler(msg, set_minutes)

def set_hours(message):
    global is_sleep
    try:
        hours = float(message.text)
        hours_seconds = int(3600 * hours)
        if hours < 0:
            bot.send_message(message.chat.id, "You can't turn off the computer in the past!")
            main(message)
            return
        os.system(f"shutdown -s -f -t {hours_seconds}")
        is_sleep = True
        bot.send_message(message.chat.id, f"PC will off in {hours} hours")
        main(message)
    except ValueError:
        msg = bot.send_message(message.chat.id, "Error: Enter a number")
        bot.register_next_step_handler(msg, set_hours)
def check_sleep(message):
    global is_sleep
    if is_sleep:
        bot.send_message(message.chat.id, 'Bedtime was set')
        main(message)
    else:
        bot.send_message(message.chat.id, 'Bedtime is not set')
        main(message)

def user_accept(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button9 = types.KeyboardButton('Yes')
    button10 = types.KeyboardButton('No')
    markup.add(button9)
    markup.add(button10)
    send_message = bot.send_message(message.chat.id, 'Are you sure?', reply_markup=markup)
    bot.register_next_step_handler(send_message, acept_shutdown)

def acept_shutdown(message):
    accept = message.text
    if accept == 'Yes':
        remove_buttons = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'Pc off now', reply_markup=remove_buttons)
        os.system("shutdown -s -f -t 0")
    elif accept == 'No':
        main(message)
    else:
        user_accept(message)  

bot.polling(none_stop=True)
