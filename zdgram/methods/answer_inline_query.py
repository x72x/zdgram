import zdgram
from typing import List, Union
from json import dumps

class AnswerInlineQuery:
    async def answerInlineQuery(
            self: "zdgram.Bot",
            inline_query_id: str,
            results: List[
                Union[
                    "zdgram.types.InlineQueryResultArticle", "None"
                ]
            ],
            cache_time: int = None,
            is_personal: bool = None,
            next_offset: str = None,
            button: "zdgram.types.InlineQueryResultsButton" = None,
            timeout: int = None
    ):
        data = {"inline_query_id": inline_query_id, "results": dumps([i.__default__(i) for i in results])}
        if is_personal:
            data["is_personal"]=is_personal
        if next_offset:
            data["next_offset"]=next_offset
        if button:
            data["button"]=str(button)
        if cache_time:
            data["cache_time"]=cache_time

        await self.sendRequest(
            method_name="answerInlineQuery",
            params=data,
            timeout=timeout
        )
        return True

    answer_inline_query = answerInlineQuery