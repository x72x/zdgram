import shitgram

from typing import Callable

class OnEditedMessage:
    def onEditedMessage(self: "shitgram.Bot", func: Callable = None):
        def decorator(func_: Callable) -> Callable:
            self.add_edited_message_handler(func_, func)
            return func_
        return decorator