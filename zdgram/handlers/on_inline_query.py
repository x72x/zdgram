import zdgram

from typing import Callable

class OnInlineQuery:
    def onInlineQuery(self: "zdgram.Bot", func: Callable = None):
        def decorator(func_: Callable) -> Callable:
            self.add_inline_query_handler(func_, func)
            return func_
        return decorator

    def on_inline_query(self: "zdgram.Bot", func: Callable = None):
        return self.onInlineQuery(func)