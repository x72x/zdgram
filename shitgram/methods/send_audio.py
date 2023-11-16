from json import dumps
from typing import Union, List

import shitgram

class SendAudio:
    async def sendAudio(
            self: "shitgram.Bot",
            chat_id: Union[int, str],
            audio: Union["shitgram.types.InputFile", str, bytes],
            caption: str = None,
            parse_mode: str = None,
            caption_entities: List["shitgram.types.MessageEntity"] = None,
            duration: int = None,
            performer: str = None,
            title: str = None,
            thumbnail: Union["shitgram.types.InputFile", str] = None,
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
        files = {}
        is_file = False
        if isinstance(audio, str):
            data['audio']=audio
        elif isinstance(audio, shitgram.types.InputFile):
            is_file = True
        elif isinstance(audio, bytes):
            is_file = True
        if caption:
            data['caption']=caption
        if parse_mode:
            data['parse_mode']=parse_mode
        if caption_entities:
            if isinstance(caption_entities[0], shitgram.types.MessageEntity):
                data['caption_entities']=dumps([i.__dict__ for i in caption_entities], ensure_ascii=False)
            else:
                data['caption_entities']=dumps([i.__dict__.get("_DictionaryToClass__dict") for i in caption_entities], ensure_ascii=False)
        if duration:
            data["duration"]=duration
        if performer:
            data["performer"]=performer
        if title:
            data["title"]=title
        if message_thread_id:
            data['message_thread_id']=message_thread_id
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

        if is_file:
            files["audio"]=audio
            if thumbnail:
                files["thumbnail"]=thumbnail
            resp_json = await self.sendRequest(
                method_name="sendAudio",
                params=data,
                timeout=timeout,
                files=files
            )
        else:
            resp_json = await self.sendRequest(
                method_name="sendAudio",
                params=data,
                timeout=timeout
            )
        return shitgram.types.Update()._parse(shitgram.types.Message()._parse(resp_json.get("result")))