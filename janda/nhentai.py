from janda.utils.client import *
from janda.utils.request import request

Janda = Api()


class Nhentai(object):
    """Jandapress Nhentai API

    Methods
    -------
    get : function
        Get doujin API from Id

    search : function
        Search doujin by tags / artist / character / parody or group

    search_related : function
        Get related book API from book Id

    get_random : function
        Get random doujin
    """

    def __init__(self):
        self.specs = {}

    async def get(self, book: int) -> str:
        """Get nhentai doujin book from Id

        Parameters
        ----------
        book : int
            The id number of the doujin.

        Returns
        -------
        str
            reparsed json as string
        """

        self.book = str(book)
        data = await request(Janda.nhentai + Janda.endpoint_book, self.book)
        return better_object(data)

    async def search(self, query: str, page: int = 1, sort: str = "popular-today") -> str:
        """Search nhentai doujin by tags / artist / character / parody or group

        Parameters
        ----------
        query : str
            query to search for

        page : int
            Page number. Default is 1

        sort : str
            popular-today, popular-week, popular

        Returns
        -------
        str
            reparsed json as string
        """

        if sort not in ["popular-today", "popular-week", "popular"]:
            raise ValueError(
                "Sort must be one of the following: popular-today, popular-week, popular"
            )

        self.query = query
        self.page = page
        self.sort = sort
        self.req = str(self.query + "&page=" +
                       str(self.page) + "&sort=" + self.sort)

        data = await request(Janda.nhentai + Janda.endpoint_search, self.req)
        return better_object(data)

    async def search_related(self, book: int) -> str:
        """Get nhentai related from book ID

        Parameters
        ----------
        book : int
            Number id of the book

        Returns
        -------
        str
            reparsed json as string
        """

        self.book = str(book)
        data = await request(Janda.nhentai + Janda.endpoint_related + self.book)
        return better_object(data)


    async def get_random(self) -> str:
        """Get nhentai random doujin

        Returns
        -------
        str
            reparsed json as string
        """

        data = await request(Janda.nhentai + Janda.endpoint_random)
        return better_object(data)
