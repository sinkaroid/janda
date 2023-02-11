import aiohttp
from .client import Api

Janda = Api()

async def request(url, params="", timeout=10) -> dict:
    """Request to the api

    Parameters
    ----------
    url : str
        The url to be requested
    params : str
        The parameters to be requested
    timeout : int
        The timeout for the request

    Returns
    -------
    dict
        The response from the api
    """

    async with aiohttp.ClientSession() as session:
        async with session.get(url + params, headers=Janda.header, timeout=timeout) as response:
            print(response.url)
            
            try:
                data = await response.json()
            except:
                data = await response.text()
            return data
