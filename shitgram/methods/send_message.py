from json import dumps
from typing import Union, List

import shitgram

class SendMessage:
    async def sendMessage(
            self: "shitgram.Bot",
            chat_id: Union[int, str],
            text: str,
            parse_mode: str = None,
            message_thread_id: int = None,
            entities: List["shitgram.types.MessageEntity"] = None,
            disable_web_page_preview: bool = None,
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
            'text': text
        }
        if message_thread_id:
            data['message_thread_id']=message_thread_id
        if parse_mode:
            data['parse_mode']=parse_mode
        if entities:
            data['entities']=dumps([str(i) if isinstance(i, shitgram.types.MessageEntity) else i.__dict__.get("_DictionaryToClass__dict") for i in entities], ensure_ascii=False)
        if disable_web_page_preview:
            data['disable_web_page_preview']=disable_web_page_preview
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

        resp_json = await self.sendRequest(
            method_name="sendMessage",
            params=data,
            timeout=timeout
        )
        return shitgram.types.Update()._parse(shitgram.types.Message()._parse(resp_json.get("result")))