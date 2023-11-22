import zdgram

from typing import Callable

class OnPreCheckoutQuery:
    def onPreCheckoutQuery(self: "zdgram.Bot", func: Callable = None):
        def decorator(func_: Callable) -> Callable:
            self.add_pre_checkout_query_handler(func_, func)
            return func_
        return decorator

    def on_pre_checkout_query(self: "zdgram.Bot", func: Callable = None):
        return self.onPreCheckoutQuery(func)