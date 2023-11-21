import shitgram

from typing import Callable

class OnShippingQuery:
    def onShippingQuery(self: "shitgram.Bot", func: Callable = None):
        def decorator(func_: Callable) -> Callable:
            self.add_shipping_query_handler(func_, func)
            return func_
        return decorator

    def on_shipping_query(self: "shitgram.Bot", func: Callable = None):
        return self.onShippingQuery(func)