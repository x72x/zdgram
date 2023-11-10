from .parser import Parser

class CallbackGame(
    Parser
):
    def __init__(self):
        super().__init__()
        self.callback_game = True