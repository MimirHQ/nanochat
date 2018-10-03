"""
addition bot
"""
from nanochat.bot import (
    ChatBot
)


def main(bot):
    """"""
    total = 0
    bot.send('Time to add up some integers!')
    bot.send('Type "STOP" to stop.')
    while True:
        message = bot.get()
        if message.lower() == 'stop':
            break
        try:
            num = int(message)
            total = total + num
            bot.send('Your new total is %d' % total)
        except Exception:
            bot.send('That is not an integer :(')
    bot.send('See you later!')


if __name__ == '__main__':
    bot = ChatBot()
    main(bot)
