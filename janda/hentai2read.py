import requests
import json
from .utils.parser import *

BASE_URL = Api()


class Hentai2read(object):
    """Hentai2read API wrapper

    Methods
    -------
    get : function
        Gets doujin from path given

    search : function
        Search for doujin based on the latest

    """

    def __init__(self, api_key: str = ""):
        """Initializes the Hentai2read.

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

    async def get(self, path: str, chapter: int = 1):
        """Gets doujin from path given

        path: https://hentai2read.com/a_story_of_tomoe_gozen_being_punished_by_a_shota/1

        Parameters
        ----------
        path : str
            The path url

        chapter : int
            The chapter number. Default is 1

        Raises
        ------
        ValueError
            If the doujin is not found.

        Returns
        -------
        dict
            The book object that represents the specific path response.
        """

        if "/" in path:
            path = path.replace("/", "")

        self.specs["book"] = path + "/" + str(chapter)

        try:
            path = str(path)
        except ValueError:
            raise ValueError("Path must be a str")

        data = requests.get(BASE_URL.hentai2read + "/get", params=self.specs)

        return better_object(data.json())

    async def search(self, query: str):
        """Search for doujin based on the latest

        path: https://hentai2read.com/hentai-list/search/alter

        Parameters
        ----------
        query : str
            The query to search for.

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

        query = auto_space(query)

        if query == "":
            raise ValueError("Query must be given")
        data = requests.get(BASE_URL.hentai2read + "/search", params=self.specs)

        if len(data.json()["data"]) == 0:
            raise ValueError("No results found")

        return better_object(data.json())
