import shitgram

class AnswerCallbackQuery:
    async def answerCallbackQuery(
            self: "shitgram.Bot",
            callback_query_id: str,
            text: str = None,
            show_alert: bool = None,
            url: str = None,
            cache_time: int = None,
            timeout: int = None
    ):
        data = {"callback_query_id": callback_query_id}
        if text:
            data["text"]=text
        if show_alert:
            data["show_alert"]=show_alert
        if url:
            data["url"]=url
        if cache_time:
            data["cache_time"]=cache_time

        await self.sendRequest(
            method_name="answerCallbackQuery",
            params=data,
            timeout=timeout
        )
        return True

    answer_callback_query = answerCallbackQuery