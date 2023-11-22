import zdgram
from typing import List

class Message:
    message_id: int
    id: int
    message_thread_id: int
    from_user: "zdgram.types.User"
    sender_chat: "zdgram.types.Chat"
    date: int
    chat: "zdgram.types.Chat"
    forward_from: "zdgram.types.User"
    forward_from_chat: "zdgram.types.Chat"
    forward_from_message_id: int
    forward_signature: str
    forward_sender_name: str
    forward_date: int
    is_topic_message: bool
    is_automatic_forward: bool
    reply_to_message: "Message"
    via_bot: "zdgram.types.User"
    edit_date: int
    has_protected_content: bool
    media_group_id: str
    author_signature: str
    text: str
    entities: List["zdgram.types.MessageEntity"]
    animation: "zdgram.types.Animation"
    audio: "zdgram.types.Audio"
    document: "zdgram.types.Document"
    photo: List["zdgram.types.PhotoSize"]
    sticker: "zdgram.types.Sticker"
    story: "zdgram.types.Story"
    video: "zdgram.types.Video"
    video_note: "zdgram.types.VideoNote"
    voice: "zdgram.types.Voice"
    caption: str
    caption_entities: list
    has_media_spoiler: bool
    contact: "zdgram.types.Contact"
    dice: "zdgram.types.Dice"
    game: "zdgram.types.Game"
    poll: "zdgram.types.Poll"
    venue: "zdgram.types.Venue"
    location: "zdgram.types.Location"
    new_chat_members: list["zdgram.types.User"]
    left_chat_member: "zdgram.types.User"
    new_chat_title: str
    new_chat_photo: List["zdgram.types.PhotoSize"]
    delete_chat_photo: bool
    group_chat_created: bool
    supergroup_chat_created: bool
    channel_chat_created: bool
    message_auto_delete_timer_changed: "zdgram.types.MessageAutoDeleteTimerChanged"
    migrate_to_chat_id: int
    migrate_from_chat_id: int
    pinned_message: "Message"
    invoice: "zdgram.types.Invoice"
    successful_payment: "zdgram.types.SuccessfulPayment"
    user_shared: "zdgram.types.UserShared"
    chat_shared: "zdgram.types.ChatShared"
    connected_website: str
    write_access_allowed: "zdgram.types.WriteAccessAllowed"
    passport_data: "zdgram.types.PassportData"
    proximity_alert_triggered: "zdgram.types.ProximityAlertTriggered"
    forum_topic_created: "zdgram.types.ForumTopicCreated"
    forum_topic_edited: "zdgram.types.ForumTopicEdited"
    forum_topic_closed: "zdgram.types.ForumTopicClosed"
    forum_topic_reopened: "zdgram.types.ForumTopicReopened"
    general_forum_topic_hidden: "zdgram.types.GeneralForumTopicHidden"
    general_forum_topic_unhidden: "zdgram.types.GeneralForumTopicUnhidden"
    video_chat_scheduled: "zdgram.types.VideoChatScheduled"
    video_chat_started: "zdgram.types.VideoChatStarted"
    video_chat_ended: "zdgram.types.VideoChatEnded"
    video_chat_participants_invited: "zdgram.types.VideoChatParticipantsInvited"
    web_app_data: None
    reply_markup: "zdgram.types.InlineKeyboardMarkup"
    link: str

    def _parse(self, dt: dict):
        dt['id']=dt['message_id']
        if dt.get('chat'):
            dt['link']=self._get_link(dt)

        if dt.get("reply_to_message"):
            dt['reply_to_message']=self._parse(dt['reply_to_message'])

        return dt

    @staticmethod
    def _get_link(message: dict):
        if message['chat'].get("username"):
            return "http://t.me/{}/{}".format(
                message['chat']['username'],
                str(message['id'])
            )
        else:
            return "http://t.me/c/{}/{}".format(
                str(message['chat']['id']).replace('-100', ''),
                str(message['id'])
            )