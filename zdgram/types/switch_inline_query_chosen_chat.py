from .parser import Parser

class SwitchInlineQueryChosenChat(
    Parser
):
    def __init__(
            self,
            query: str = None,
            allow_user_chats: bool = True,
            allow_bot_chats: bool = True,
            allow_group_chats: bool = True,
            allow_channel_chats: bool = True
    ):
        super().__init__()
        self.allow_channel_chats = allow_channel_chats
        self.allow_group_chats = allow_group_chats
        self.allow_bot_chats = allow_bot_chats
        self.allow_user_chats = allow_user_chats
        self.query = query
