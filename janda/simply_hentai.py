import requests
import json
from .utils.parser import *

BASE_URL = Api()


class SimplyHentai(object):
    """Simply-hentai API wrapper

    Methods
    -------
    get : function
        Gets doujin from path given
    """

    def __init__(self, api_key: str = ""):
        """Initializes SimplyHentai.

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

    async def get(self, path: str):
        """Gets doujin from path given

        path: https://www.simply-hentai.com/fate-grand-order/perros => 'fate-grand-order/perros'

        Parameters
        ----------
        path : str
            The path url

        Raises
        ------
        ValueError
            If the doujin is not found.

        Returns
        -------
        dict
            The book object that represents the specific path response.
        """

        if str(path).isdigit():
            raise ValueError("Invalid path, must be a str")

        path = path.strip("/")
        self.specs["book"] = path

        try:
            path = str(path)

        except ValueError or path.isdigit():
            raise ValueError("Path must be a str")

        data = requests.get(BASE_URL.simply_hentai + "/get", params=self.specs)

        return better_object(data.json())
