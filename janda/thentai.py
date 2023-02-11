from janda.utils.client import *
from janda.utils.request import request

Janda = Api()


class Thentai(object):
    """Jandapress 3hentai API

    Methods
    -------
    get: function
        Get doujin from id

    get_random: function
        Get random doujin

    search: function
        Searches doujin by tags / artist / character / parody or group
    """

    def __init__(self, api_key: str = ""):
        """Initializes the 3hentai.

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

    async def get(self, book: int) -> str:
        """Get 3hentai doujin book from Id

        Parameters
        ----------
        book : int
            The id number of the doujin

        Raises
        ------
        ValueError
            If the doujin is not found.

        Returns
        -------
        str
            reparsed json as string
        """

        self.book = str(book)
        data = await request(Janda.thentai + Janda.endpoint_book, self.book)
        return better_object(data)

    async def search(self, query: str, page: int = 1, sort: str = "recent") -> str:
        """Search 3hentai by tags / artist / character / etc

        Parameters
        ----------
        query : str
            query to search for

        page : int
            Page number. Default is 1

        sort : str
            recent, popular-24h, popular-7d, popular

        Returns
        -------
        str
            reparsed json as string
        """

        if sort not in [
            "recent", "popular-24h", "popular-7d", "popular"
        ]:
            raise ValueError(
                "Sort must be one of these: recent, popular-24h, popular-7d, popular"
            )

        self.query = query
        self.page = page
        self.sort = sort
        self.req = str(self.query + "&page=" +
                       str(self.page) + "&sort=" + self.sort)

        data = await request(Janda.thentai + Janda.endpoint_search, self.req)
        return better_object(data)

    async def get_random(self) -> str:
        """Get 3hentai random doujin

        Returns
        -------
        str
            reparsed json as string
        """
        data = await request(Janda.thentai + Janda.endpoint_random)
        return better_object(data)
