import requests
import json
from .utils.parser import *

BASE_URL = Api()

class Qhentai(object):
    """ Qhentai API wrapper 
    
    Methods
    -------
    get : function
        Gets doujin from path given

    get_random : function
        Gets random doujin on Hentai2read
    """

    def __init__(self, api_key: str = ''):
        """Initializes Qhentai.

        Parameters
        ----------
        api_key : str
            scathach.dev API key (optional)
        """
        if api_key == '':
            self.api_key = None
        else:
            self.api_key = api_key
        self.specs = {'api_key': self.api_key}

    async def get(self, path: str):
        """Gets doujin from path given

        path: https://qhentai.net/comic-aun-kai-vol-17/ => 'comic-aun-kai-vol-17'

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
            raise ValueError('Invalid path, must be a str')

        path = path.strip('/')
        self.specs['g'] = path

        try:
            path = str(path)

        except ValueError or path.isdigit():
            raise ValueError('Path must be a str')

        data = requests.get(BASE_URL.qhentai, params=self.specs)

        self.final = json.loads(better_object(data.json()), encoding="utf-8")
   
        return better_object(self.final)
        

    async def search(self, query: str, page: int = 1):
        """Search for doujin wirh query and page number given

        path: https://qhentai.net/?s=

        Parameters
        ----------
        query : str
            The query to search for

        page : int
            The page number to search for

        Raises
        ------
        ValueError
            If the doujin is not found.

        Returns
        -------
        dict
            The list object that represents the doujin response.
        """

        self.specs['query'] = query
        self.specs['page'] = page

        query = auto_space(query)

        if query == '':
            raise ValueError('Query must be given')
        data = requests.get(BASE_URL.hentai2read + 'args.php', params=self.specs)

        if len(data.json()) == 0:
            raise ValueError('No results found')

        return better_object(data.json())


    async def get_random(self):
        """Gets random doujin on Hentai2read

        Returns
        -------
        dict
            The book object that represents the doujin response.
        """
        data = requests.get(BASE_URL.qhentai + 'random')

        return better_object(data.json())
