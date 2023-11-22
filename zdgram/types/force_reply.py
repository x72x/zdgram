from .parser import Parser

class ForceReply(
    Parser
):
    def __init__(self, input_field_placeholder: str = None, selective: bool = None) -> None:
        super().__init__()
        self.force_reply = True
        if input_field_placeholder: self.input_field_placeholder = input_field_placeholder
        if selective is not None: self.selective = selective