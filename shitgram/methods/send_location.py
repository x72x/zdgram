from typing import Union

import shitgram

class SendLocation:
    async def sendLocation(
            self: "shitgram.Bot",
            chat_id: Union[int, str],
            latitude: float,
            longitude: float,
            horizontal_accuracy: float = None,
            live_period: int = None,
            heading: int = None,
            proximity_alert_radius: int = None,
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
        Use this method to send point on the map


        :param chat_id: Unique identifier for the target chat or username of the target channel (in the format @channelusername)
        :param latitude: Latitude of the location
        :param longitude: Longitude of the location
        :param horizontal_accuracy: The radius of uncertainty for the location, measured in meters; 0-1500
        :param live_period: Period in seconds for which the location will be updated (see Live Locations, should be between 60 and 86400.
        :param heading: For live locations, a direction in which the user is moving, in degrees. Must be between 1 and 360 if specified.
        :param proximity_alert_radius: For live locations, a maximum distance for proximity alerts about approaching another chat member, in meters. Must be between 1 and 100000 if specified.
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
            'longitude': longitude
        }
        if self.protect_content:
            data['protect_content']=self.protect_content
        if self.disable_notification:
            data['disable_notification']=self.disable_notification
        if horizontal_accuracy is not None:
            data["horizontal_accuracy"]=horizontal_accuracy
        if live_period is not None:
            data["live_period"]=live_period
        if heading is not None:
            data["heading"]=heading
        if proximity_alert_radius is not None:
            data["proximity_alert_radius"]=proximity_alert_radius
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

    send_location = sendLocation