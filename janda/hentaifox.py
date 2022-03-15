import requests
import json
from .utils.parser import *

BASE_URL = Api()

class Hentaifox(object):
    """ HentaiFox API wrapper 
    
    Methods
    -------
    get : function
        Get doujin API from Id

    search_by_latest : function
        Search for doujin based on the latest

    search_by_popular : function
        Search for doujin based on the popular

    get_random : function
        Gets random doujin on hentaifox
    """

    def __init__(self, api_key: str = ''):
        """Initializes the Hentaifox.

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

        self.specs['g'] = book

        # handle if book not int, then throw error
        try:
            book = int(book)
        except ValueError:
            raise ValueError('Book must be an int')

        data = requests.get(BASE_URL.hentaifox, params=self.specs)
        if data.json()['type'] is None:
            raise ValueError('No results found')

        self.final = json.loads(better_object(data.json()), encoding="utf-8")

        return better_object(self.final)

    async def search_by_latest(self, query: str, page: int = 1):
        """Search for doujin based on the latest 

        path: https://hentaifox.com/search/?q=alter&sort=latest

        Parameters
        ----------
        query : str
            The query to search for.
        
        page : int
            The page number to search

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
        self.specs['sort'] = "latest"
        self.specs['page'] = page

        query = auto_space(query)

        if query == '':
            raise ValueError('Query must be given')
        data = requests.get(BASE_URL.hentaifox + 'args.php', params=self.specs)

        # if data.json() length is 0, then throw error
        if len(data.json()) == 0:
            raise ValueError('No results found')

        return better_object(data.json())

    async def search_by_popular(self, query: str, page: int = 1):
        """Search for doujin based on the latest 

        path: https://hentaifox.com/search/?q=alter&sort=popular

        Parameters
        ----------
        query : str
            The query to search for.
        
        page : int
            The page number to search

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
        self.specs['sort'] = "popular"
        self.specs['page'] = page

        query = auto_space(query)

        if query == '':
            raise ValueError('Query must be given')
        data = requests.get(BASE_URL.hentaifox + 'args.php', params=self.specs)

        # if data.json() length is 0, then throw error
        if len(data.json()) == 0:
            raise ValueError('No results found')

        return better_object(data.json())

    async def get_random(self):
        """Gets random doujin on hentaifox

        Returns
        -------
        dict
            The book object that represents the doujin response.
        """
        data = requests.get(BASE_URL.hentaifox + 'random' + '/', params=self.specs)

        return better_object(data.json())

