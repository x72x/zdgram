import shitgram
from typing import Union, List
from json import dumps

class SendMediaGroup:
    async def sendMediaGroup(
            self: "shitgram.Bot",
            chat_id: Union["str", "int"],
            media: List[
                Union[
                    "shitgram.types.InputMediaPhoto",
                    "shitgram.types.InputMediaVideo",
                    "shitgram.types.InputMediaAudio",
                    "shitgram.types.InputMediaAnimation",
                    "shitgram.types.InputMediaDocument"
                ]
            ],
            disable_notification: bool = None,
            protect_content: bool = None,
            reply_to_message_id: int = None,
            allow_sending_without_reply: bool = None,
    ) -> List["shitgram.types.Message"]:
        result = await shitgram.utils.send_media_group(
            self,
            chat_id=chat_id,
            media=media,
            disable_notification=disable_notification,
            protect_content=protect_content,
            reply_to_message_id=reply_to_message_id,
            allow_sending_without_reply=allow_sending_without_reply
        )
        if not result.get("ok"):
            raise shitgram.exceptions.ApiException(
                dumps(result, ensure_ascii=False)
            )
        return [shitgram.types.Update()._parse(shitgram.types.Message()._parse(i)) for i in result.get("result")]