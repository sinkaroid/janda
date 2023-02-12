from janda.utils.client import *
from janda.utils.request import request

Janda = Api()


class Hentai2read(object):
    """Jandapress Hentai2read API

    Methods
    -------
    get : function
        Get doujin from path given

    search : function
        Search for doujin based on the latest

    """

    def __init__(self, api_key: str = ""):
        """Initializes the Hentai2read.

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
        """Get hentai2read doujin from path given
        
        example: https://hentai2read.com/a_story_of_tomoe_gozen_being_punished_by_a_shota/1

        Parameters
        ----------
        path : str
            The path url

        Returns
        -------
        str
            reparsed json as string
        """

        self.book = str(path)

        data = await request(Janda.hentai2read + Janda.endpoint_book, self.book)
        return better_object(data)

    async def search(self, query: str) -> str:
        """Search hentai2read doujin based on the latest

        example: https://hentai2read.com/hentai-list/search/alter

        Parameters
        ----------
        query : str
            The query to search for.

        Returns
        -------
        str
            reparsed json as string
        """

        self.key = query

        data = await request(Janda.hentai2read + Janda.endpoint_search, self.key)
        return better_object(data)
