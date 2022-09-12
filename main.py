import requests
import telebot
from auth_data import token
from datetime import datetime

HELP_MSG = """
/btc   /btc_rub     BTC
/eth   /eth_rub     Ethereum
/ltc   /ltc_rub     LiteCoin
/doge  /doge_rub    DogeCoin
"""

ABOUT_MSG = """
Для связи с автором:
admin@bug4f.ru
"""

def telegram_bot(token):
    bot = telebot.TeleBot(token)
    bot.delete_webhook()
    #Принимаем команды, отправляем ответ
    @bot.message_handler(commands=["start"])
    def start_message(message):
        bot.send_message(message.chat.id, "Привет юзернейм!\nЯ умею показывать цену продажи криптовалют в $ и Ꝑ.\nЧтобы посмотреть доступные команды, введи /help")
    @bot.message_handler(commands=["help"])
    def start_message(message):
        bot.send_message(message.chat.id, HELP_MSG)
    @bot.message_handler(commands=["about"])
    def start_message(message):
        bot.send_message(message.chat.id, ABOUT_MSG)
    # Принимаем текстовые сообщения, отправляем ответ
    @bot.message_handler(content_types=["text"])
    def send_text(message):
        if message.text.lower() == "/btc":
            try:
                req = requests.get("https://yobit.net/api/3/ticker/btc_usd")
                response = req.json()
                sell_price_1 = response ["btc_usd"]["sell"]
                sell_price = round(sell_price_1, 2)
                bot.send_message(
                    message.chat.id,
                    f"По состоянию на {datetime.now().strftime('%Y-%m-%d %H:%M')}\nЦена продажи BTC: {sell_price}$"
                )
            except Exception as ex:
                print(ex)
                bot.send_message(
                    message.chat.id,
                    "Ошибка BTC"
                )
        elif message.text.lower() == "/btc_rub":
            try:
                req = requests.get("https://yobit.net/api/3/ticker/btc_rur")
                response = req.json()
                sell_price_1 = response["btc_rur"]["sell"]
                sell_price = round(sell_price_1, 2)
                bot.send_message(
                    message.chat.id,
                    f"По состоянию на {datetime.now().strftime('%Y-%m-%d %H:%M')}\nЦена продажи BTC: {sell_price} руб."
                )
            except Exception as ex:
                print(ex)
                bot.send_message(
                    message.chat.id,
                    "Ошибка BTC_RUB"
                )
        elif message.text.lower() == "/eth":
            try:
                req = requests.get("https://yobit.net/api/3/ticker/eth_usd")
                response = req.json()
                sell_price_1 = response["eth_usd"]["sell"]
                sell_price = round(sell_price_1, 2)
                bot.send_message(
                    message.chat.id,
                    f"По состоянию на {datetime.now().strftime('%Y-%m-%d %H:%M')}\nЦена продажи ETH: {sell_price}$"
                )
            except Exception as ex:
                print(ex)
                bot.send_message(
                    message.chat.id,
                    "Ошибка ETH"
                )
        elif message.text.lower() == "/eth_rub":
            try:
                req = requests.get("https://yobit.net/api/3/ticker/eth_rur")
                response = req.json()
                sell_price_1 = response["eth_rur"]["sell"]
                sell_price = round(sell_price_1, 2)
                bot.send_message(
                    message.chat.id,
                    f"По состоянию на {datetime.now().strftime('%Y-%m-%d %H:%M')}\nЦена продажи ETH: {sell_price} руб."
                )
            except Exception as ex:
                print(ex)
                bot.send_message(
                    message.chat.id,
                    "Ошибка ETH_RUB"
                )
        elif message.text.lower() == "/doge":
            try:
                req = requests.get("https://yobit.net/api/3/ticker/doge_usd")
                response = req.json()
                sell_price_1 = response["doge_usd"]["sell"]
                sell_price = round(sell_price_1, 2)
                bot.send_message(
                    message.chat.id,
                    f"По состоянию на {datetime.now().strftime('%Y-%m-%d %H:%M')}\nЦена продажи DOGE: {sell_price}$"
                )
            except Exception as ex:
                print(ex)
                bot.send_message(
                    message.chat.id,
                    "Ошибка LTC_RUB"
                )
        elif message.text.lower() == "/doge_rub":
            try:
                req = requests.get("https://yobit.net/api/3/ticker/doge_rur")
                response = req.json()
                sell_price_1 = response["doge_rur"]["sell"]
                sell_price = round(sell_price_1, 2)
                bot.send_message(
                    message.chat.id,
                    f"По состоянию на {datetime.now().strftime('%Y-%m-%d %H:%M')}\nЦена продажи DOGE: {sell_price} руб."
                )
            except Exception as ex:
                print(ex)
                bot.send_message(
                    message.chat.id,
                    "Ошибка DOGE_RUB"
                )
        elif message.text.lower() == "/ltc":
            try:
                req = requests.get("https://yobit.net/api/3/ticker/ltc_usd")
                response = req.json()
                sell_price_1 = response["ltc_usd"]["sell"]
                sell_price = round(sell_price_1, 2)
                bot.send_message(
                    message.chat.id,
                    f"По состоянию на {datetime.now().strftime('%Y-%m-%d %H:%M')}\nЦена продажи LTC: {sell_price}$"
                )
            except Exception as ex:
                print(ex)
                bot.send_message(
                    message.chat.id,
                    "Ошибка LTC"
                )
        elif message.text.lower() == "/ltc_rub":
            try:
                req = requests.get("https://yobit.net/api/3/ticker/ltc_rur")
                response = req.json()
                sell_price_1 = response["ltc_rur"]["sell"]
                sell_price = round(sell_price_1, 2)
                bot.send_message(
                    message.chat.id,
                    f"По состоянию на {datetime.now().strftime('%Y-%m-%d %H:%M')}\nЦена продажи LTC: {sell_price} руб."
                )
            except Exception as ex:
                print(ex)
                bot.send_message(
                    message.chat.id,
                    "Ошибка LTC"
                )
        else:
            bot.send_message(message.chat.id, "Не понимаю команду.")
    bot.polling()


if __name__ == '__main__':
    # get_data()
    telegram_bot(token)