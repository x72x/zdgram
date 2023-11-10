import shitgram
from typing import Callable

class OnMessage:
    def onMessage(self: "shitgram.Bot", func: Callable = None):
        def decorator(func_: Callable) -> Callable:
            self.add_message_handler(func_, func)
            return func_
        return decorator