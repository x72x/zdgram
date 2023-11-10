from . import types
from typing import Union
from json import dumps

import os
import aiohttp
import asyncio

def reply_markup_parse(
        reply_markup: Union["str", "dict", "types.InlineKeyboardMarkup", "types.ForceReply"]
):
    if isinstance(reply_markup, dict):
        return dumps(reply_markup, ensure_ascii=False)
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