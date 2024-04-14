import telebot
from config import TOKEN
import webbrowser

# from extensions import MoneyConverter, APIException

bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=["start"])
def start(message):
    name = message.from_user.first_name
    text = (f"Здравствуйте, {name}!\U0001F60A\n Приветствуем Вас в нашем Telegram-боте! Тут вы можете:\n\
    - Узнать краткую информацию о нашем зоопарке /info\n\
    - Посетить сайт Московского зоопарка \U0001F63A\ /zoo\n\
    - Пройти уникальную викторину 'Какое твое тотемное животное', благодаря которой вы определите ваше 'ментальное'\
    животное. А в качестве бонуса Вам будет доступна информация, которая поможет Вам стать лучше и найти еще одного доброго друга!\n\
    (пусть он и не очень разговорчивый на 'нашем' языке)\n\
    - связаться с сотрудником зоопарка, для решения возникших вопросов \U0000260E/call")
    photo = open('welc.webp', 'rb')
    bot.send_photo(message.chat.id,photo,caption=text)



@bot.message_handler(commands=["info"])
def info(message):
    text=("Московский зоопарк – первый зоопарк в России, был открыт в 1864 году. Сейчас в нём содержится около восьми тысяч животных,\
    относящихся более чем к тысяче видов мировой фауны. Основные цели зоопарка - природоохранная, просветительская и научно-исследовательская деятельность")
    bot.reply_to(message,text)


@bot.message_handler(commands=["zoo"])
def info(message):
    bot.reply_to(message, webbrowser.open('https://moscowzoo.ru/'))


bot.polling(none_stop=True)