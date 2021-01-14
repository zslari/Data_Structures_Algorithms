"""
Created By: Zafir Lari
Application: Sample Email Message Class

Description: Runs with the demo_Email.py file
"""


class Message:
    """ Messages include a sender, recipient, and body of text """

    MAX_LEN = 50
    EMPTY_STR = ""

    def __init__(self, sender: str, recipient: str):
        self._body = Message.EMPTY_STR
        self._sender = Message.EMPTY_STR
        self._recipient = Message.EMPTY_STR
        self.set_sender(sender)
        self.set_recipient(recipient)

    def set_sender(self, new_sender: str):
        if self.str_ok(new_sender):
            self._sender = new_sender
        else:
            self._sender = Message.EMPTY_STR
            return False

    def set_recipient(self, new_recipient: str):
        if self.str_ok(new_recipient):
            self._recipient = new_recipient
        else:
            self._recipient = Message.EMPTY_STR
            return False

    def append(self, line: str):
        if self.str_ok(line):
            self._body += (line + "\n")

    def to_string(self):
        ret_str = "From: " + self._sender + "\n"
        ret_str = ret_str + "To: " + self._recipient + "\n"
        ret_str = ret_str + self._body + "\n"
        return ret_str

    def str_ok(self, the_str):
        if isinstance(the_str, str) and len(the_str) <= Message.MAX_LEN:
            return True
        else:
            return False
