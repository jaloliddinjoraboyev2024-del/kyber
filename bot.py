import telebot
from telebot import types
import os

TOKEN = "8272068901:AAEmlUWxVO-PZkEzc1qJ52FuqFIgpIPPMic"
WEB_APP_URL = "https://github.com/jaloliddinjoraboyev2024-del/kyber" # GitHub Pages manzili

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.InlineKeyboardMarkup()
    web_app_btn = types.InlineKeyboardButton(
        "🛡️ Kiberxavfsizlik Testiga o'tish", 
        web_app=types.WebAppInfo(url=WEB_APP_URL)
    )
    markup.add(web_app_btn)
    bot.send_message(message.chat.id, 
        "Assalomu alaykum! *CyberShield* platformasiga xush kelibsiz.\n\n"
        "Quyidagi tugma orqali testni boshlang 👇", 
        parse_mode="Markdown", reply_markup=markup)

# 24/7 ishlash uchun polling
bot.infinity_polling()