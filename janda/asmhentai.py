import requests
import json
from .utils.parser import *

BASE_URL = Api()

class Asmhentai(object):
    """ Asmhentai API wrapper 
    
    Methods
    -------
    get : function
        Gets doujin from id given

    search : function
        Search for doujin wirh query and page number given

    get_random : function
        Gets random doujin
    """

    def __init__(self, api_key: str = ''):
        """Initializes Asmhentai.

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

    async def get(self, id: int):
        """Gets doujin from id given

        path: https://asmhentai.com/g/311851

        Parameters
        ----------
        id : int
            The id of the doujin

        Raises
        ------
        ValueError
            If the doujin is not found.

        Returns
        -------
        dict
            The book object that represents the specific id response.
        """

        if isinstance(id, int):
                id = str(id)

        path = id.strip('/')
        self.specs['g'] = path

        try:
            path = str(path)

        except ValueError or path.isdigit():
            raise ValueError('Path must be a str')

        data = requests.get(BASE_URL.asmhentai, params=self.specs)

        self.final = json.loads(better_object(data.json()), encoding="utf-8")
   
        return better_object(self.final)


    async def search(self, query: str, page: int = 1):
        """Search for doujin with query and page number given

        path: https://asmhentai.com/search/?q=

        Parameters
        ----------
        query : str
            The query to search for

        page : int
            The page number to search for, Default is 1

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
        data = requests.get(BASE_URL.asmhentai + 'args.php', params=self.specs)

        if len(data.json()) == 0:
            raise ValueError('No results found')

        return better_object(data.json())

   
    async def get_random(self):
        """Gets random doujin on Hentai2read

        Returns
        -------
        dict
            The book object that represents the random doujin response.
        """
        random = requests.get('https://asmhentai.com/random/')

        try:
            self.book = str(just_number(random.url))
            self.specs['g'] = self.book

        except ValueError:
            raise ValueError('Uh oh something wrong here')

        data = requests.get(BASE_URL.asmhentai, params=self.specs)

        self.final = json.loads(better_object(data.json()), encoding="utf-8")
   
        return better_object(self.final)
