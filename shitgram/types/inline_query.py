import shitgram
from .parser import Parser

class InlineQuery:
    id: str
    from_user: "shitgram.types.User"
    query: str
    offset: str
    chat_type: str
    location: "shitgram.types.Location"

class ChosenInlineResult:
    result_id: str
    from_user: "shitgram.types.User"
    location: "shitgram.types.Location"
    inline_message_id: str
    query: str

class InlineQueryResultsButton(
    Parser
):
    def __init__(
            self,
            text: str,
            web_app: "shitgram.types.WebAppInfo" = None,
            start_parameter: str = None
    ):
        super().__init__()
        self.start_parameter = start_parameter
        self.web_app = web_app
        self.text = text

# class InlineQueryResultArticle(
#     Parser
# ):
#     def __init__(
#             self
#     ):
#         super().__init__()
#         self.type = "article"
