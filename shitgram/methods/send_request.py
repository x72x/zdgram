import shitgram
import aiohttp
import os


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
            elif isinstance(f, shitgram.types.InputFile):
                file_name = f.file_name
                file = f.file
            else:
                file_name, file = _prepare_file(f) or key, f

            data.add_field(key, file, filename=file_name)

    return data

class SendRequest:
    async def sendRequest(
            self: "shitgram.Bot",
            method_name: str,
            params: dict = None,
            files=None,
            timeout: int = None,
    ) -> dict:
        if params and params.get("chat_id"):
            params.update({"chat_id": str(params.get("chat_id"))})
        if files:
            params = _prepare_data(params, files)
        session = await shitgram.bot.session_manager.get_session()
        async with session.request(
            method="post",
            url=self.api.format(self.bot_token, method_name),
            data=params,
            timeout=aiohttp.ClientTimeout(total=timeout or 300)
        ) as resp:
                return await resp.json()