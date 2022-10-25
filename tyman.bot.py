from ast import arg
from tracemalloc import start
from base64 import decode
from cgitb import text
from email.mime import audio
from tkinter import END
from telegram import *
from telegram.ext import *
from requests import *
from war_stats import war_stats_txt
commands = '/start\n/help\n/stats\n/audio\n/photo'

token_test = "5635713355:AAEC5BvI9Hw06jzXJZkpXwWDszWrc1R9j6Q"
token = "5635713355:AAEC5BvI9Hw06jzXJZkpXwWDszWrc1R9j6Q" 
updater = Updater(token_test, use_context=True) 
dispatcher = updater.dispatcher 
 
def start_handler(update: Update, context: CallbackContext): 
    buttons = [[KeyboardButton("help")],[KeyboardButton("war stats")]]
    context.bot.send_message(chat_id=update.effective_chat.id,  text=f"Привіт!☀️, {update.effective_chat.first_name}!\nfor more info write \"/help\"",
    reply_markup=ReplyKeyboardMarkup(buttons))
    pass

def message_handler(update: Update, context: CallbackContext):
    if "help" in update.message.text:
        context.bot.send_message(chat_id=update.effective_chat.id, text = f"commands, that u can use: \n{commands}")
    if "war stats" in update.message.text:
        context.bot.send_message(chat_id=update.effective_chat.id,  text=f'Привіт!☀️{war_stats_txt}')
        

def stats_handler(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id,  text=f'{war_stats_txt}') 
pass  

def audio_handler(update: Update, context: CallbackContext):
    with open('nazar.mp3', 'rb') as file:
        context.bot.send_chat_action(update.effective_chat.id, ChatAction.UPLOAD_AUDIO)
        context.bot.send_audio(update.effective_chat.id, audio=file)
    pass

def photo_handler(update: Update, context: CallbackContext):
    with open('retyrn.png', 'rb') as photo:
        context.bot.send_chat_action(update.effective_chat.id, ChatAction.UPLOAD_PHOTO)
        context.bot.send_photo(update.effective_chat.id, photo=photo)
    pass

def help_handler(update: Update, context:CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text = f"commands, that u can use: \n{commands}")
    pass

start_command_handler = CommandHandler("audio", audio_handler)
dispatcher.add_handler(start_command_handler)

start_command_handler = CommandHandler("photo", photo_handler)
dispatcher.add_handler(start_command_handler)

start_command_handler = CommandHandler("stats", stats_handler) 
dispatcher.add_handler(start_command_handler) 

start_command_handler = CommandHandler("start", start_handler) 
dispatcher.add_handler(start_command_handler) 
 
dispatcher.add_handler(MessageHandler(Filters.text ,message_handler))

start_command_handler = CommandHandler("help", help_handler) 
dispatcher.add_handler(start_command_handler)

updater.start_polling()