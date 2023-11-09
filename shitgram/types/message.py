import shitgram
from typing import List

class Message:
    message_id: int
    id: int
    message_thread_id: int
    from_user: "shitgram.types.User"
    sender_chat: "shitgram.types.Chat"
    date: int
    chat: "shitgram.types.Chat"
    forward_from: "shitgram.types.User"
    forward_from_chat: "shitgram.types.Chat"
    forward_from_message_id: int
    forward_signature: str
    forward_sender_name: str
    forward_date: int
    is_topic_message: bool
    is_automatic_forward: bool
    reply_to_message: "Message"
    via_bot: "shitgram.types.User"
    edit_date: int
    has_protected_content: bool
    media_group_id: str
    author_signature: str
    text: str
    entities: List["shitgram.types.MessageEntity"]
    animation: None
    audio: None
    document: None
    photo: None
    sticker: "shitgram.types.Sticker"
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
    location: "shitgram.types.Location"
    new_chat_members: list["shitgram.types.User"]
    left_chat_member: "shitgram.types.User"
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
    reply_markup: "shitgram.types.InlineKeyboardMarkup"

    def _parse(self, dt: dict):
        dt['id']=dt['message_id']
        return dt
