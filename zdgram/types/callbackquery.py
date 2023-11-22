import zdgram

class CallbackQuery:
    id: str
    from_user: "zdgram.types.User"
    message: "zdgram.types.Message"
    inline_message_id: str
    chat_instance: str
    data: str
    game_short_name: str