"""
nanochat server
"""
from nanobot.bot import (
    ChatBot
)
from nanobot.chat import (
    main
)
from flask import (
    Flask,
    render_template,
    request
)
from flask_socketio import (
    SocketIO
)
from threading import (
    Thread,
    Event
)
from typing import (  # noqa
    Mapping
)


server = Flask(__name__)
socketio = SocketIO(server)


@server.route('/')
def home():
    """Serving HTML Pages/Templates"""
    return render_template('index.html')


# handle conversations

CONVERSATIONS = {}  # type: Mapping


@socketio.on('connect')
def handle_connect():
    """"""
    pass


def init_conversation(sid):
    """"""
    bot = ChatBot(cli=False, new_message=Event(), new_reply=Event())
    bot.sid = sid
    bot.socket = socketio
    bot.thread = Thread(name=('Chatbot %s' % sid), target=main, args=(bot,))
    return bot


def handle_first_connect():
    """"""
    sid = request.sid
    bot = CONVERSATIONS[sid]
    bot.thread.start()


def handle_send_message(json):
    """"""
    sid = request.sid
    if sid in CONVERSATIONS:
        bot = CONVERSATIONS[sid]
        bot.message = json['data']['message']
        bot.new_message.set()
        bot.new_message.clear()
        bot.new_reply.wait()
        alive = bot.thread.is_alive()
        if not alive:
            del CONVERSATIONS[sid]
            print('Ended conversation with sessionid = %s' % sid)
        return {'alive': alive}
    return {'alive': False}


@socketio.on('get_namespace')
def handle_get_namespace(json):
    """"""
    sid = request.sid
    CONVERSATIONS[sid] = init_conversation(sid)
    print('Started conversation with sessionid = %s' % sid)
    socketio.on_event('send_message', handle_send_message, namespace=('/%s' % sid))
    socketio.on_event('connect', handle_first_connect, namespace=('/%s' % sid))
    return sid


if __name__ == '__main__':
    socketio.run(server)
