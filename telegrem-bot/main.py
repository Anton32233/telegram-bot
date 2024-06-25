import telebot
from fastapi import FastAPI, Request
from conf import API_TOKEN, EXCEL_FILE_PATH
from search import search_in_excel, read_row_values

bot = telebot.TeleBot(API_TOKEN)
app = FastAPI()

@app.route('/' + API_TOKEN, methods=['POST'])
def webhook(request: Request):
    update = telebot.types.Update.de_json(request.json(), bot)
    bot.process_new_updates([update])
    return 'ok', 200

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, 'Привет! Я могу помочь тебе найти внутренний код по фамилии сотрудника. Просто напиши мне фамилию сотрудника.')

@bot.message_handler(func=lambda message: True)
def search_contact(message):
    results = search_in_excel(EXCEL_FILE_PATH, message.text)
    if results:
        for result in results:
            row_values = read_row_values(EXCEL_FILE_PATH, result['sheet'], result['row'])
            if row_values:
                bot.reply_to(message, f'Номер {row_values[0]} для {message.text} находится на листе {result["sheet"]}, строка {result["row"]}.')
            else:
                bot.reply_to(message, f'К сожалению, не удалось получить информацию для {message.text}.')
    else:
        bot.reply_to(message, f'К сожалению, я не смог найти номер для {message.text}.')

if __name__ == '__main__':
    bot.remove_webhook()
    bot.polling()