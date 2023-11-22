from .parser import Parser

class LoginUrl(
    Parser
):
    def __init__(
            self,
            url: str,
            forward_text: str = None,
            bot_username: str = None,
            request_write_access: bool = None
    ):
        super().__init__()
        self.url = url
        if forward_text: self.forward_text = forward_text
        if bot_username: self.bot_username = bot_username
        if request_write_access is not None: self.request_write_access = request_write_access
