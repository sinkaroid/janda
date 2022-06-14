import requests
import json
from janda.utils.parser import *

BASE_URL = Api()


class Pururin(object):
    """Pururin API wrapper

    Methods
    -------
    get: function
        Gets doujin from id

    get_random: function
        Gets random doujin

    search: function
        Searches doujin by tags / artist / character / parody or group
    """

    @staticmethod
    def better_object(parser: dict):
        """Converts the json object to a more readable object.

        Parameters
        ----------
        parser : dict
            The json object.
        """
        return json.dumps(parser, sort_keys=True, indent=4)

    @staticmethod
    def auto_space(string: str):
        """Automatically adds spaces for GET requests

        Parameters
        ----------
        string : str
            The string to be formatted.
        """

        return string.replace(" ", "+")

    def __init__(self, api_key: str = ""):
        """Initializes the Pururin.

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
        """Get doujin from id

        path: https://pururin.to/gallery/61119

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
        dict
            The book object that represents the specific id response.
        """

        self.specs["book"] = book

        try:
            book = int(book)
        except ValueError:
            raise ValueError("Book must be an int")

        data = requests.get(BASE_URL.pururin + "/get", params=self.specs)
        if data.json()["data"]["title"] == "":
            raise ValueError("No results found")

        return better_object(data.json())

    async def search(self, query: str, page: int = 1, sort: str = "newest"):
        """Search doujin by tags / artist / character / parody or group

        Parameters
        ----------
        query : str
            query to search for

        page : int
            Page number. Default is 1

        sort : str
            newest, most-popular, highest-rated, most-viewed, title, random

        Raises
        ------
        ValueError
            If the doujin is not found.

        Returns
        -------
        dict
            The list object that represents the doujin response
        """

        if sort not in [
            "newest",
            "most-popular",
            "highest-rated",
            "most-viewed",
            "title",
            "random",
        ]:
            raise ValueError(
                "Sort must be one of newest, most-popular, highest-rated, most-viewed, title, random"
            )

        self.specs["key"] = query
        self.specs["page"] = page
        self.specs["sort"] = sort

        data = requests.get(BASE_URL.pururin + "/search", params=self.specs)

        if len(data.json()["data"]) == 0:
            raise ValueError("No results found")

        if data.status_code != 200:
            raise ValueError(
                "Request failed with status code {}".format(data.status_code)
            )

        return better_object(data.json())

    async def get_random(self):
        """Gets random doujin on pururin

        Returns
        -------
        dict
            The book object that represents the random doujin response.
        """
        data = requests.get(BASE_URL.pururin + "/random", params=self.specs)

        return better_object(data.json())
