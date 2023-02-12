from janda.utils.client import *
from janda.utils.request import request

Janda = Api()


class Asmhentai(object):
    """Jandapress Asmhentai API

    Methods
    -------
    get : function
        Get doujin from id given

    search : function
        Search for doujin wirh query and page number given

    get_random : function
        Get random doujin
    """

    def __init__(self, api_key: str = ""):
        """Initializes Asmhentai.

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

    async def get(self, id: int) -> str:
        """Get asmhentai doujin from id given

        example: https://asmhentai.com/g/311851

        Parameters
        ----------
        id : int
            The id of the doujin

        Returns
        -------
        str
            reparsed json as string
        """

        self.book = str(id)
        data = await request(Janda.asmhentai + Janda.endpoint_book, self.book)
        return better_object(data)

    async def search(self, query: str, page: int = 1) -> str:
        """Search asmhentai doujin with query and page number given

        example: https://asmhentai.com/search/?q=

        Parameters
        ----------
        query : str
            The query to search for

        page : int
            The page number to search for, Default is 1

        Returns
        -------
        str
            reparsed json as string
        """

        self.query = query
        self.page = page
        self.req = str(self.query) + "&page=" + str(self.page)

        data = await request(Janda.asmhentai + Janda.endpoint_search, self.req)
        return better_object(data)

    async def get_random(self) -> str:
        """Get asmhentai random doujin

        Returns
        -------
        str
            reparsed json as string
        """

        data = await request(Janda.asmhentai + Janda.endpoint_random)
        return better_object(data)
