from janda.utils.client import *
from janda.utils.request import request

Janda = Api()


class SimplyHentai(object):
    """Jandapress simply-hentai API

    Methods
    -------
    get : function
        Get doujin from path given
    """

    def __init__(self, api_key: str = ""):
        """Initializes SimplyHentai.

        Parameters
        ----------
        api_key : str
            scathach.id API key (optional)
        """
        if api_key == "":
            self.api_key = None
        else:
            self.api_key = api_key
        self.specs = {"api_key": self.api_key}

    async def get(self, path: str) -> str:
        """Get simply-hentai doujin from path given

        example: https://www.simply-hentai.com/fate-grand-order/perros => 'fate-grand-order/perros'

        Parameters
        ----------
        path : str
            The path url

        Returns
        -------
        str
            reparsed json as string
        """

        if str(path).isdigit():
            raise ValueError("Invalid path, must be a str")

        path = path.strip("/")
        self.book = path

        try:
            path = str(path)

        except ValueError or path.isdigit():
            raise ValueError("Path must be a str")

        data = await request(Janda.simply_hentai + Janda.endpoint_book, self.book)
        return better_object(data)
