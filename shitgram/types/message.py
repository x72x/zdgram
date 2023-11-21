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
    animation: "shitgram.types.Animation"
    audio: "shitgram.types.Audio"
    document: "shitgram.types.Document"
    photo: List["shitgram.types.PhotoSize"]
    sticker: "shitgram.types.Sticker"
    story: "shitgram.types.Story"
    video: "shitgram.types.Video"
    video_note: "shitgram.types.VideoNote"
    voice: "shitgram.types.Voice"
    caption: str
    caption_entities: list
    has_media_spoiler: bool
    contact: "shitgram.types.Contact"
    dice: "shitgram.types.Dice"
    game: "shitgram.types.Game"
    poll: "shitgram.types.Poll"
    venue: "shitgram.types.Venue"
    location: "shitgram.types.Location"
    new_chat_members: list["shitgram.types.User"]
    left_chat_member: "shitgram.types.User"
    new_chat_title: str
    new_chat_photo: List["shitgram.types.PhotoSize"]
    delete_chat_photo: bool
    group_chat_created: bool
    supergroup_chat_created: bool
    channel_chat_created: bool
    message_auto_delete_timer_changed: "shitgram.types.MessageAutoDeleteTimerChanged"
    migrate_to_chat_id: int
    migrate_from_chat_id: int
    pinned_message: "Message"
    invoice: "shitgram.types.Invoice"
    successful_payment: "shitgram.types.SuccessfulPayment"
    user_shared: "shitgram.types.UserShared"
    chat_shared: "shitgram.types.ChatShared"
    connected_website: str
    write_access_allowed: "shitgram.types.WriteAccessAllowed"
    passport_data: "shitgram.types.PassportData"
    proximity_alert_triggered: "shitgram.types.ProximityAlertTriggered"
    forum_topic_created: "shitgram.types.ForumTopicCreated"
    forum_topic_edited: "shitgram.types.ForumTopicEdited"
    forum_topic_closed: "shitgram.types.ForumTopicClosed"
    forum_topic_reopened: "shitgram.types.ForumTopicReopened"
    general_forum_topic_hidden: "shitgram.types.GeneralForumTopicHidden"
    general_forum_topic_unhidden: "shitgram.types.GeneralForumTopicUnhidden"
    video_chat_scheduled: "shitgram.types.VideoChatScheduled"
    video_chat_started: "shitgram.types.VideoChatStarted"
    video_chat_ended: "shitgram.types.VideoChatEnded"
    video_chat_participants_invited: "shitgram.types.VideoChatParticipantsInvited"
    web_app_data: None
    reply_markup: "shitgram.types.InlineKeyboardMarkup"
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