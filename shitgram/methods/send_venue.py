from typing import Union

import shitgram

class SendVenue:
    async def sendVenue(
            self: "shitgram.Bot",
            chat_id: Union[int, str],
            latitude: float,
            longitude: float,
            title: str,
            address: str,
            foursquare_id: str = None,
            foursquare_type: str = None,
            google_place_id: str = None,
            google_place_type: str = None,
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
        """
        Use this method to send information about a venue. On success, the sent Message is returned.

        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :param latitude: Latitude of the venue
        :param longitude: Longitude of the venue
        :param title: Name of the venue
        :param address: Address of the venue
        :param foursquare_id: Foursquare identifier of the venue
        :param foursquare_type: Foursquare type of the venue, if known. (For example, “arts_entertainment/default”, “arts_entertainment/aquarium” or “food/icecream”.)
        :param google_place_id: Google Places identifier of the venue
        :param google_place_type: Google Places type of the venue. (See supported types at : https://developers.google.com/places/web-service/supported_types .)
        :param message_thread_id: Unique identifier for the target message thread (topic) of the forum; for forum supergroups only
        :param disable_notification: Sends the message silently. Users will receive a notification with no sound.
        :param protect_content: Protects the contents of the sent message from forwarding and saving
        :param reply_to_message_id: If the message is a reply, ID of the original message
        :param allow_sending_without_reply: Pass True if the message should be sent even if the specified replied-to message is not found
        :param reply_markup: Additional interface options. A JSON-serialized object for an inline keyboard, custom reply keyboard, instructions to remove reply keyboard or to force a reply from the user.
        :param timeout: Request TimeOut
        :return: On success, the sent Message is returned.
        """
        data = {
            'chat_id': chat_id,
            'latitude': latitude,
            'longitude': longitude,
            'title': title,
            'address': address
        }
        if self.protect_content:
            data['protect_content']=self.protect_content
        if self.disable_notification:
            data['disable_notification']=self.disable_notification
        if foursquare_id is not None:
            data["foursquare_id"]=foursquare_id
        if foursquare_type is not None:
            data["foursquare_type"]=foursquare_type
        if google_place_id is not None:
            data["google_place_id"]=google_place_id
        if google_place_type is not None:
            data["google_place_type"]=google_place_type
        if message_thread_id:
            data['message_thread_id']=message_thread_id
        if disable_notification is not None:
            data['disable_notification']=disable_notification
        if protect_content is not None:
            data['protect_content']=protect_content
        if reply_to_message_id:
            data['reply_to_message_id']=reply_to_message_id
        if allow_sending_without_reply:
            data['allow_sending_without_reply']=allow_sending_without_reply
        if reply_markup:
            data['reply_markup']=shitgram.utils.reply_markup_parse(reply_markup)

        resp_json = await self.sendRequest(
            method_name="sendLocation",
            params=data,
            timeout=timeout
        )
        return shitgram.bot.update_manager._parse(shitgram.bot.message_manager._parse(resp_json.get("result")))

    send_venue = sendVenue