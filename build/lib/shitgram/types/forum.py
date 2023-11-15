
class ForumTopicCreated:
    name: str
    icon_color: int
    icon_custom_emoji_id: str

class ForumTopicClosed:
    pass

class ForumTopicEdited:
    name: str
    icon_custom_emoji_id: str

class ForumTopicReopened:
    pass

class GeneralForumTopicHidden:
    pass

class GeneralForumTopicUnhidden:
    pass