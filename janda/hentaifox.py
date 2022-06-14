import requests
import json
from .utils.parser import *

BASE_URL = Api()


class Hentaifox(object):
    """HentaiFox API wrapper

    Methods
    -------
    get : function
        Get doujin API from Id

    search : function
        Search for doujin wirh query and page number given

    get_random : function
        Get random doujin
    """

    def __init__(self, api_key: str = ""):
        """Initializes the Hentaifox.

        Parameters
        ----------
        api_key : str
            scathach.dev API key (optional)
        """
        if api_key == "":
            self.api_key = None
        else:
            self.api_key = api_key
        self.specs = {"api_key": self.api_key}

    async def get(self, book: int):
        """Get doujin API from Id

        path: https://hentaifox.com/gallery/88027/

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

        data = requests.get(BASE_URL.hentaifox + "/get", params=self.specs)

        if data.status_code != 200:
            raise ValueError("No results found")

        return better_object(data.json())

    async def search(self, query: str, page: int = 1, sort: str = "latest"):
        """Search for doujin based on the latest

        path: https://hentaifox.com/search/?q=alter&sort=latest

        Parameters
        ----------
        query : str
            The query to search for

        page : int
            The page number to search

        sort : str
            The sort order to search: latest, popular

        Raises
        ------
        ValueError
            If the doujin is not found.

        Returns
        -------
        dict
            The list object that represents the doujin response.
        """

        self.specs["key"] = query
        self.specs["sort"] = sort
        self.specs["page"] = page

        query = auto_space(query)

        if query == "":
            raise ValueError("Query must be given")
        data = requests.get(BASE_URL.hentaifox + "/search", params=self.specs)

        if len(data.json()["data"]) == 0:
            raise ValueError("No results found")

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

        data = requests.get(BASE_URL.hentaifox + "/random", params=self.specs)

        if data.status_code != 200:
            raise ValueError(
                "Request failed with status code {}".format(data.status_code)
            )

        return better_object(data.json())
