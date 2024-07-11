import telebot
from gtts import gTTS
from Api_key import api_key as token

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
  bot.send_message(message.chat.id,"Привет ✌️ ")

@bot.message_handler(commands=['to_voice_en'])
def text_handle(message):
   bot.send_message(message.chat.id, "Напиши сообщение для перевода в звук: ")
   bot.register_next_step_handler(message, translate_en)

def translate_en(message):
   tts = gTTS(message.text, lang='en')
   tts.save(f'{message.from_user.id}.mp3')
   audio = open(f'{message.from_user.id}.mp3', 'rb')
   bot.send_audio(message.chat.id, audio)
   audio.close()

bot.polling()