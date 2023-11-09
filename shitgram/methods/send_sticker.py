import aiohttp

from json import dumps
from typing import Union, List

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
            reply_markup: Union["shitgram.types.InlineKeyboardMarkup", str, dict] = None
    ) -> "shitgram.types.Message":
        data = {
            'chat_id': chat_id,
            'sticker': sticker
        }
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
            if isinstance(reply_markup, dict):
                data['reply_markup']=dumps(reply_markup, ensure_ascii=False)
            elif isinstance(reply_markup, str):
                data['reply_markup']=reply_markup
            elif isinstance(reply_markup, shitgram.types.InlineKeyboardMarkup):
                data_ = {'inline_keyboard': []}
                for i in reply_markup.inline_keyboard:
                    data_['inline_keyboard'].append(
                        [x.__dict__ for x in i]
                    )
                data['reply_markup']=dumps(data_, ensure_ascii=False)

        async with aiohttp.ClientSession() as client:
            async with client.post(
                self.api.format(self.bot_token, "sendSticker"),
                data=data
            ) as resp:
                resp_json: dict = await resp.json()
                if not resp_json.get("ok"):
                    raise shitgram.exceptions.ApiException(
                        dumps(resp_json, ensure_ascii=False)
                    )
                return shitgram.types.Update()._parse(shitgram.types.Message()._parse(resp_json.get("result")))