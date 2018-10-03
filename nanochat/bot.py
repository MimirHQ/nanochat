"""
chatbot class
"""


class ChatBot:

    cli_mode = True
    message = False

    new_message = None
    new_reply = None
    thread = None
    sid = None
    socket = None

    def __init__(self, cli=True, new_message=None, new_reply=None):
        """"""
        self.cli_mode = cli
        self.new_message = new_message
        self.new_reply = new_reply

    def get(self, prompt=None):
        """"""
        if self.cli_mode:
            val = None
            if prompt is not None:
                val = input(prompt)
            else:
                val = input()
            return val if val else False
        if prompt is not None:
            self.send(prompt)
        self.new_reply.clear()
        self.new_message.wait()
        message_val = self.message
        self.message = False
        self.new_reply.set()
        return message_val if message_val else False

    def send(self, message=''):
        """"""
        if self.cli_mode:
            print(message)
        else:
            self.socket.emit('send_note', {'note': message}, namespace=('/%s' % self.sid))
