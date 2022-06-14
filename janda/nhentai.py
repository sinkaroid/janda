import requests
import json
from .utils.parser import *

BASE_URL = Api()


class Nhentai(object):
    """Nhentai API wrapper

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

    async def get(self, book: int):
        """Get doujin book from Id

        Parameters
        ----------
        book : int
            The id number of the doujin.

        Raises
        ------
        ValueError
            If the doujin is not found.

        Returns
        -------
        dict
            The book object that represents the specific id response.
        """

        self.specs["book"] = book

        try:
            book = int(book)
        except ValueError:
            raise ValueError("Book must be an int")

        data = requests.get(BASE_URL.nhentai + "/get", params=self.specs)

        self.final = json.loads(better_object(data.json()))

        return better_object(self.final)

    async def search(self, query: str, page: int = 1, sort: str = "popular-today"):
        """Search doujin by tags / artist / character / parody or group

        Parameters
        ----------
        query : str
            query to search for

        page : int
            Page number. Default is 1

        sort : str
            popular-today, popular-week, popular

        Raises
        ------
        ValueError
            If the doujin is not found.

        Returns
        -------
        dict
            The list object that represents the doujin response
        """

        if sort not in ["popular-today", "popular-week", "popular"]:
            raise ValueError(
                "Sort must be one of the following: popular-today, popular-week, popular"
            )

        self.specs["key"] = query
        self.specs["page"] = page
        self.specs["sort"] = sort

        data = requests.get(BASE_URL.nhentai + "/search", params=self.specs)

        if len(data.json()["data"]) == 0:
            raise ValueError("No results found")

        if data.status_code != 200:
            raise ValueError(
                "Request failed with status code {}".format(data.status_code)
            )

        return better_object(data.json())

    async def search_related(self, book: int):
        """Get related book API from book ID or book link

        Parameters
        ----------
        book : int
            Number id of the book

        Raises
        ------
        ValueError
            If the doujin is not found.

        Returns
        -------
        dict
            The list object that represents the doujin response
        """

        self.specs["book"] = book

        data = requests.get(BASE_URL.nhentai + "/related", params=self.specs)

        if data.status_code != 200:
            raise ValueError(
                "Request failed with status code {}".format(data.status_code)
            )

        return better_object(data.json())

    async def get_random(self):
        """Get random doujin

        Raises
        ------
        ValueError
            If the doujin is not found.

        Returns
        -------
        dict
            The book object that represents the random doujin response.
        """

        data = requests.get(BASE_URL.nhentai + "/random", params=self.specs)

        if data.status_code != 200:
            raise ValueError(
                "Request failed with status code {}".format(data.status_code)
            )

        return better_object(data.json())
