from flask import Flask, request
import telepot
import urllib3
import random


proxy_url = "http://proxy.server:3128"
telepot.api._pools = {
    'default': urllib3.ProxyManager(proxy_url=proxy_url, num_pools=3, maxsize=10, retries=False, timeout=30),
}
telepot.api._onetime_pool_spec = (urllib3.ProxyManager, dict(proxy_url=proxy_url, num_pools=1, maxsize=1, retries=False, timeout=30))

secret = "BOT"
bot = telepot.Bot('Token')
bot.setWebhook("https://USERNAME.pythonanywhere.com/{}".format(secret), max_connections=1)

app = Flask(__name__)


def generate():
    pw = ""
    for i in range(6):
        pw += str(random.choice(range(10)))
    return pw

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)
    message = msg['text']

    if content_type == 'text':
        if message == "/start" :
            bot.sendMessage(chat_id, """
Hello! Welcome to my bot.
This bot can send you a generated password.
Enter "Send" to receive a generated password""")

        elif message == "Send" or message == "send" :
            password = generate()
            bot.sendMessage(chat_id, password)
        else :
            bot.sendMessage(chat_id, "Invalid input")


@app.route('/{}'.format(secret), methods=["POST"])
def telegram_webhook():
    update = request.get_json()
    if "message" in update:
        handle(update['message'])
    return "OK"
