import shitgram

class ChatJoinRequest:
    chat: "shitgram.types.Chat"
    from_user: "shitgram.types.User"
    user_chat_id: int
    date: int
    bio: str
    invite_link: "shitgram.types.ChatInviteLink"