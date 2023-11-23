import zdgram
import aiohttp
import os
import logging

from json import dumps, loads

logger = logging.getLogger(__name__)

def _prepare_file(obj):
    """
    Prepares file for upload.
    """
    name = getattr(obj, 'name', None)
    if name and isinstance(name, str) and name[0] != '<' and name[-1] != '>':
        return os.path.basename(name)

def _prepare_data(params=None, files=None):
    """
    Adds the parameters and files to the request.

    :param params:
    :param files:
    :return:
    """
    data = aiohttp.formdata.FormData(quote_fields=False)

    if params:
        for key, value in params.items():
            data.add_field(key, str(value))
    if files:
        for key, f in files.items():
            if isinstance(f, tuple):
                if len(f) == 2:
                    file_name, file = f
                else:
                    raise ValueError('Tuple must have exactly 2 elements: filename, fileobj')
            elif isinstance(f, zdgram.types.InputFile):
                file_name = f.file_name
                file = f.file
            else:
                file_name, file = _prepare_file(f) or key, f

            data.add_field(key, file, filename=file_name)

    return data

class SendRequest:
    async def sendRequest(
            self: "zdgram.Bot",
            method_name: str,
            params: dict = None,
            files=None,
            timeout: int = None,
    ) -> dict:
        if method_name.lower() != "getupdates":
            logger.debug(
                "   Sending request : %s",
                method_name
            )
        if params and params.get("chat_id"):
            params.update({"chat_id": str(params.get("chat_id"))})
        if files:
            params = _prepare_data(params, files)
        session = await zdgram.bot.session_manager.get_session()
        async with session.request(
            method="post" if files else "get",
            url=self.api.format(self.bot_token, method_name),
            data=params,
            timeout=aiohttp.ClientTimeout(total=timeout or 60)
        ) as resp:
            resp_json = loads(await resp.read())
            if method_name.lower() != "getupdates":
                logger.debug(
                "   Responce recived: %s",
                method_name
            )
            if not resp_json.get("ok"):
                raise zdgram.exceptions.ApiException(
                    dumps(resp_json, indent=2)
                )
            return resp_json

    send_request = sendRequest