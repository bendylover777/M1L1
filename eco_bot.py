import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = telebot.TeleBot('TOKEN')

def get_inline_keyboard():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton('пластиковая бутылка', callback_data='btn1'))
    markup.add(InlineKeyboardButton('кожура банана', callback_data='btn2'))
    markup.add(InlineKeyboardButton('стекло', callback_data='btn3'))
    markup.add(InlineKeyboardButton('алюминиевая банка', callback_data='btn4'))
    markup.add(InlineKeyboardButton('бумага', callback_data='btn5'))
    return markup

@bot.message_handler(commands=['start', 'help'])
def starting(message):
    bot.send_message(message.chat.id, 'Привет! Я эко-бот. Напиши мне команду /eco')

@bot.message_handler(commands=['eco'])
def eco_items(message):
    bot.send_message(message.chat.id, 'Выбери предмет, для которого хочешь узнать сколько он разлагается', reply_markup=get_inline_keyboard())

@bot.callback_query_handler(func=lambda call: call.data in ['btn1', 'btn2', 'btn3', 'btn4', 'btn5'])
def handle_inline_keyboard(call):
    items = {
        'btn1': 'пластиковая бутылка разлагается450 лет',
        'btn2': 'кожура банана разлагается до 2 лет',
        'btn3': 'стекло разлагается более 1000 лет',
        'btn4': 'алюминиевая банка разлагается 500 лет',
        'btn5': 'бумага разлагается 2 года'
    }
    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, items[call.data])

bot.infinity_polling()

