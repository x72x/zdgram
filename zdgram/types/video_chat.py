import zdgram
from typing import List

class VideoChatScheduled:
    start_date: int

class VideoChatStarted:
    pass

class VideoChatEnded:
    duration: int

class VideoChatParticipantsInvited:
    users: List["zdgram.types.User"]