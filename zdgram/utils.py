from . import types
from typing import Union, List
from orjson import dumps, loads

import os
import aiohttp
import asyncio
import zdgram

async def convert_input_media_array(array):
    media = []
    files = {}
    for input_media in array:
            media_dict = loads(str(input_media))
            if media_dict['media'].startswith('attach://'):
                key = media_dict['media'].replace('attach://', '')
                files[key] = input_media.media
            media.append(media_dict)
    return dumps(media).decode(), files

async def send_media_group(
        bot: "zdgram.Bot", chat_id, media,
        disable_notification=None, reply_to_message_id=None,
        timeout=None, allow_sending_without_reply=None, protect_content=None, message_thread_id=None):
    method_name = "sendMediaGroup"
    media_json, files = await convert_input_media_array(media)
    payload = {'chat_id': chat_id, 'media': media_json}
    if disable_notification is not None:
        payload['disable_notification'] = disable_notification
    if reply_to_message_id:
        payload['reply_to_message_id'] = reply_to_message_id
    if timeout:
        payload['timeout'] = timeout
    if allow_sending_without_reply is not None:
        payload['allow_sending_without_reply'] = allow_sending_without_reply
    if protect_content is not None:
        payload['protect_content'] = protect_content
    if message_thread_id:
        payload['message_thread_id'] = message_thread_id
    return await bot.sendRequest(
        method_name, params=payload,
        files=files if files else None
    )

async def run_multiple_bots(bots: List["zdgram.Bot"]):
    tasks = []
    while True:
        for i in bots:
            try:
                task = asyncio.create_task(i.start_polling())
                tasks.append(task)
            except:
                pass
        try:
            await asyncio.wait(tasks)
        except asyncio.CancelledError:
            tasks.clear()
            pass

def reply_markup_parse(
        reply_markup: Union["str", "dict", "types.InlineKeyboardMarkup", "types.ForceReply"]
):
    if isinstance(reply_markup, dict):
        return dumps(reply_markup).decode()
    elif isinstance(reply_markup, str):
        return reply_markup
    elif isinstance(
        reply_markup, types.InlineKeyboardMarkup
    ) or isinstance(
        reply_markup, types.ForceReply
    ) or isinstance(
        reply_markup, types.ReplyKeyboardMarkup
    ) or isinstance(
        reply_markup, types.ReplyKeyboardRemove
    ):
        return str(reply_markup)

async def upload_files(file_path, file, server_url, session: aiohttp.ClientSession, params: dict):
    # Create a session object
    del params['upload_file']
    del params['file_path']
    del params['ident']
    async with session:
        # Create a form data object
        data = aiohttp.FormData()
        # Get the filename and extension of the file
        filename = os.path.basename(file_path)
        extension = os.path.splitext(file_path)[1]
        # Get the content type based on the extension
        if extension == ".jpg" or extension == ".jpeg":
            content_type = "image/jpeg"
        elif extension == ".png":
            content_type = "image/png"
        else:
            content_type = "application/octet-stream"

        # Add the file to the form data
        with open(file_path, 'rb') as f:
            data.add_field(
                name=file,
                value=f,
                filename=filename,
                content_type=content_type,
            )

        for i in params:
            data.add_field(
                name=i,
                value=params.get(i)
            )


        # Send a POST request to the server URL with the form data
        async with session.post(
            server_url,
            data=data,
        ) as response:
            # Get the status code, headers, and body of the response
            status = response.status
            body = await response.json()
            return body

all_updates = [
    "message",
    "edited_message",
    "channel_post",
    "edited_channel_post",
    "inline_query",
    "chosen_inline_result",
    "callback_query",
    "shipping_query",
    "pre_checkout_query",
    "poll",
    "poll_answer",
    "my_chat_member",
    "chat_member",
    "chat_join_request"
]