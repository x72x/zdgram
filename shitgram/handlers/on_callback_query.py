import shitgram

from typing import Callable

class OnCallbackQuery:
    def onCallbackQuery(self: "shitgram.Bot", func: Callable = None):
        def decorator(func_: Callable) -> Callable:
            self.add_callback_query_handler(func_, func)

        return decorator