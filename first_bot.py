import telebot
from first_telegram_bot import token

Token = token

bot = telebot.TeleBot(Token)



@bot.message_handler(content_types=["text"])
def echo(message):
    if 'Арам' in message.text:
        bot.send_message(message.chat.id, "Ба! Знакомые все лица!")
    else:
        bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
    # Постоянно обращается к серверам телеграм.    
    bot.polling(none_stop=True)    
