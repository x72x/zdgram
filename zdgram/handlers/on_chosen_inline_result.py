import zdgram

from typing import Callable

class OnChosenInlineResult:
    def onChosenInlineResult(self: "zdgram.Bot", func: Callable = None):
        def decorator(func_: Callable) -> Callable:
            self.add_chosen_inline_result_handler(func_, func)
            return func_
        return decorator

    def on_chosen_inline_result(self: "zdgram.Bot", func: Callable = None):
        return self.onChosenInlineResult(func)