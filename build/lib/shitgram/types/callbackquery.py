import shitgram

class CallbackQuery:
    id: int
    from_user: "shitgram.types.User"
    message: "shitgram.types.Message"
    inline_message_id: str
    chat_instance: str
    data: str
    game_short_name: str