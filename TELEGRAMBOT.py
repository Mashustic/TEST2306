import telebot
import redis

TOKEN = "6848763048:AAGeCGD13m-CVAuzBAlIweuCs55Xr-0ONDY"
bot = telebot.TeleBot(TOKEN)


# убедимся, что все корректно работает и заставим отправлять полученное сообщение обратно:
@bot.message_handler(content_types=['text'])
def echo(message):
    bot.send_message(message.chat.id, text=f"{message.text}")

# Обрабатываются все сообщения, содержащие команды '/start' or '/help'.
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    pass

# Обрабатываются все документы и аудиозаписи
@bot.message_handler(content_types=['document', 'audio'])
def handle_docs_audio(message):
    pass

@bot.message_handler(content_types=['voice', ])
def repeat (message: telebot. types.Message):
    bot. send_message (message. chat.id,'У тебя очень красивый голос!')
    pass

# берет из сообщения username и выдает приветственное сообщение с привязкой к пользователю.
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, f"Welcome, \ c{message.chat.username}")
    pass



@bot.message_handler(commands=['start', 'help'])

def help (message: telebot. types.Message):
    text= 'Чтобы начать работу введите комманду боту в слудеющем формате: \п‹имя валюты> ' \
          '<в какую валюту перевести> \ количество переводимой валюты> '

    bot. reply_to (message, text)

bot.polling(none_stop=True)



