from .user import User
from .chat import Chat
from .location import Location
from .message_entity import MessageEntity
from .sticker import Sticker

from typing import List

class Message:
    message_id: int
    id: int
    message_thread_id: int
    from_user: "User"
    sender_chat: "Chat"
    date: int
    chat: "Chat"
    forward_from: "User"
    forward_from_chat: "Chat"
    forward_from_message_id: int
    forward_signature: str
    forward_sender_name: str
    forward_date: int
    is_topic_message: bool
    is_automatic_forward: bool
    reply_to_message: "Message"
    via_bot: "User"
    edit_date: int
    has_protected_content: bool
    media_group_id: str
    author_signature: str
    text: str
    entities: List["MessageEntity"]
    animation: None
    audio: None
    document: None
    photo: None
    sticker: "Sticker"
    story: None
    video: None
    video_note: None
    voice: None
    caption: str
    caption_entities: list
    has_media_spoiler: bool
    contact: None
    dice: None
    game: None
    poll: None
    venue: None
    location: "Location"
    new_chat_members: list["User"]
    left_chat_member: "User"
    new_chat_title: str
    new_chat_photo: list
    delete_chat_photo: bool
    group_chat_created: bool
    supergroup_chat_created: bool
    channel_chat_created: bool
    message_auto_delete_timer_changed: None
    migrate_to_chat_id: int
    migrate_from_chat_id: int
    pinned_message: "Message"
    invoice: None
    successful_payment: None
    user_shared: None
    chat_shared: None
    connected_website: str
    write_access_allowed: None
    passport_data: None
    proximity_alert_triggered: None
    forum_topic_created: None
    forum_topic_edited: None
    forum_topic_closed: None
    forum_topic_reopened: None
    general_forum_topic_hidden: None
    general_forum_topic_unhidden: None
    video_chat_scheduled: None
    video_chat_started: None
    video_chat_ended: None
    video_chat_participants_invited: None
    web_app_data: None
    reply_markup: None

    def _parse(self, dt: dict):
        dt['id']=dt['message_id']
        return dt
