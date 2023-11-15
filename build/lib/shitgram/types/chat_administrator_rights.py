from .parser import Parser

class ChatAdministratorRights(
    Parser
):
    def __init__(
            self,
            is_anonymous: bool = False,
            can_manage_chat: bool = False,
            can_delete_messages: bool = False,
            can_manage_video_chats: bool = False,
            can_restrict_members: bool = False,
            can_promote_members: bool = False,
            can_change_info: bool = False,
            can_invite_users: bool = False,
            can_post_messages: bool = False,
            can_edit_messages: bool = False,
            can_pin_messages: bool = False,
            can_post_stories: bool = False,
            can_edit_stories: bool = False,
            can_delete_stories: bool = False,
            can_manage_topics: bool = False
    ):
        super().__init__()
        self.can_delete_stories = can_delete_stories
        self.can_edit_stories = can_edit_stories
        self.can_post_stories = can_post_stories
        self.can_pin_messages = can_pin_messages
        self.can_edit_messages = can_edit_messages
        self.can_post_messages = can_post_messages
        self.can_invite_users = can_invite_users
        self.can_change_info = can_change_info
        self.can_promote_members = can_promote_members
        self.can_restrict_members = can_restrict_members
        self.can_manage_video_chats = can_manage_video_chats
        self.can_delete_messages = can_delete_messages
        self.can_manage_chat = can_manage_chat
        self.is_anonymous = is_anonymous
        self.can_manage_topics = can_manage_topics