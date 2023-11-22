import zdgram

class ChatInviteLink:
    invite_link: str
    creator: "zdgram.types.User"
    creates_join_request: bool
    is_primary: bool
    is_revoked: bool
    name: str
    expire_date: int
    member_limit: int
    pending_join_request_count: int