from typing import List
import shitgram

class Chat:
    id = int
    type: str
    title: str
    username: str
    first_name: str
    last_name: str
    is_forum: bool
    photo: "shitgram.types.ChatPhoto"
    active_usernames: List[str]
    emoji_status_custom_emoji_id: str
    emoji_status_expiration_date: int
    bio: str
    has_private_forwards: bool
    has_restricted_voice_and_video_messages: bool
    join_to_send_messages: bool
    join_by_request: bool
    description: str
    invite_link: str
    pinned_message: "shitgram.types.Message"
    permissions: "shitgram.types.ChatPermissions"
    slow_mode_delay: int
    message_auto_delete_time: int
    has_aggressive_anti_spam_enabled: bool
    has_hidden_members: bool
    has_protected_content: bool
    sticker_set_name: str
    can_set_sticker_set: bool
    linked_chat_id: int
    location: "shitgram.types.Location"