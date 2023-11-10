import aiohttp
import shitgram

from typing import Union
from json import dumps

class ForwardMessage:
    async def forwardMessage(
            self: "shitgram.Bot",
            chat_id: Union[int, str],
            from_chat_id: Union[int, str],
            message_id: int,
            message_thread_id: int = None,
            disable_notification: bool = None,
            protect_content: bool = None,
            timeout: int = None
    ) -> "shitgram.types.Message":
        data = {
            'chat_id': chat_id,
            'from_chat_id': from_chat_id,
            'message_id': message_id
        }
        if message_thread_id:
            data['message_thread_id']=message_thread_id
        if disable_notification:
            data['disable_notification']=disable_notification
        if protect_content:
            data['protect_content']=protect_content

        session = await shitgram.bot.session_manager.get_session()
        async with session.request(
            method="post",
            url=self.api.format(self.bot_token, "sendMessage"),
            data=data,
            timeout=aiohttp.ClientTimeout(total=timeout or 300)
        ) as resp:
            resp_json: dict = await resp.json()
            if not resp_json.get("ok"):
                raise shitgram.exceptions.ApiException(
                    dumps(resp_json, ensure_ascii=False)
                )
            return  shitgram.types.Update()._parse(shitgram.types.Message()._parse(resp_json.get("result")))