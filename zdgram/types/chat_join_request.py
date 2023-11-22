import zdgram

class ChatJoinRequest:
    chat: "zdgram.types.Chat"
    from_user: "zdgram.types.User"
    user_chat_id: int
    date: int
    bio: str
    invite_link: "zdgram.types.ChatInviteLink"