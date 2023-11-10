import aiohttp

from json import dumps
from typing import Union

import shitgram

class SendSticker:
    async def sendSticker(
            self: "shitgram.Bot",
            chat_id: Union[int, str],
            sticker: Union["shitgram.types.InputFile", str],
            emoji: str = None,
            message_thread_id: int = None,
            disable_notification: bool = None,
            protect_content: bool = None,
            reply_to_message_id: int = None,
            allow_sending_without_reply: bool = None,
            reply_markup: Union[
                "shitgram.types.InlineKeyboardMarkup",
                "shitgram.types.ForceReply",
                "shitgram.types.ReplyKeyboardMarkup",
                "shitgram.types.ReplyKeyboardRemove"
            ] = None,
            timeout: int = None
    ) -> "shitgram.types.Message":
        data = {
            'chat_id': chat_id,
        }
        if isinstance(sticker, str):
            data['sticker']=sticker
        elif isinstance(sticker, shitgram.types.InputFile):
            data['sticker']=sticker.get
        if message_thread_id:
            data['message_thread_id']=message_thread_id
        if emoji:
            data['emoji']=emoji
        if disable_notification:
            data['disable_notification']=disable_notification
        if protect_content:
            data['protect_content']=protect_content
        if reply_to_message_id:
            data['reply_to_message_id']=reply_to_message_id
        if allow_sending_without_reply:
            data['allow_sending_without_reply']=allow_sending_without_reply
        if reply_markup:
            data['reply_markup']=shitgram.utils.reply_markup_parse(reply_markup)

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
            return shitgram.types.Update()._parse(shitgram.types.Message()._parse(resp_json.get("result")))