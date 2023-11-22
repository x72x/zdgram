import zdgram
from typing import Callable

class OnMessage:
    def onMessage(self: "zdgram.Bot", func: Callable = None):
        def decorator(func_: Callable) -> Callable:
            self.add_message_handler(func_, func)
            return func_
        return decorator

    def on_message(self: "zdgram.Bot", func: Callable = None):
        return self.onMessage(func)