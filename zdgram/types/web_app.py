from .parser import Parser

class WebAppData:
    data: str
    button_text: str

class WebAppInfo(
    Parser
):
    def __init__(self, url: str):
        super().__init__()
        self.url = url