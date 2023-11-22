import zdgram

from typing import Callable

class OnEditedMessage:
    def onEditedMessage(self: "zdgram.Bot", func: Callable = None):
        def decorator(func_: Callable) -> Callable:
            self.add_edited_message_handler(func_, func)
            return func_
        return decorator

    def on_edited_message(self: "zdgram.Bot", func: Callable = None):
        return self.onEditedMessage(func)