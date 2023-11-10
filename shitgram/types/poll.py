import shitgram
from typing import List

class PollOption:
    text: str
    voter_count: int

class PollAnswer:
    poll_id: str
    voter_chat: "shitgram.types.Chat"
    user: "shitgram.types.User"
    option_ids: List["int"]

class Poll:
    id: str
    question: str
    options: List["PollOption"]
    total_voter_count: int
    is_closed: bool
    is_anonymous: bool
    type: str
    allows_multiple_answers: bool
    correct_option_id: int
    explanation: str
    explanation_entities: List["shitgram.types.MessageEntity"]
    open_period: int
    close_date: int
