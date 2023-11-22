import zdgram

from typing import Callable

class OnPollAnswer:
    def onPollAnswer(self: "zdgram.Bot", func: Callable = None):
        def decorator(func_: Callable) -> Callable:
            self.add_poll_answer_handler(func_, func)
            return func_
        return decorator

    def on_poll_answer(self: "zdgram.Bot", func: Callable = None):
        return self.onPollAnswer(func)