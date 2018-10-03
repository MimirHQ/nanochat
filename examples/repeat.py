"""
simple echo bot
"""
from nanochat.bot import (
    ChatBot
)


def main(bot):
    """"""
    bot.send_message('Welcome to my chatbot.')
    bot.send_message('Type "STOP" to leave the chat.')
    message = bot.get_message()
    while message:
        bot.send_message('I heard you say: %s' % message)
        message = bot.get_message()
        if message.lower() == 'stop':
            break
    bot.send_message('Have a nice day!')


if __name__ == '__main__':
    bot = ChatBot()
    main(bot)
