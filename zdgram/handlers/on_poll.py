import zdgram

from typing import Callable

class OnPoll:
    def onPoll(self: "zdgram.Bot", func: Callable = None):
        def decorator(func_: Callable) -> Callable:
            self.add_poll_handler(func_, func)
            return func_
        return decorator

    def on_poll(self: "zdgram.Bot", func: Callable = None):
        return self.onPoll(func)