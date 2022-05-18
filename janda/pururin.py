import requests
import json
from janda.utils.parser import *

BASE_URL = Api()

class Pururin(object):
    """ Pururin API wrapper
    
    Methods
    -------
    get: function
        Gets doujin from id

    get_random: function
        Gets random doujin

    get_random_with_query: function
        Gets random doujin with query

    search_by_newest: function
        Searches for doujin based on newest

    search_by_most_popular: function
        Searches doujin based on most popular

    search_by_highest_rated: function
        Searches doujin based on highest rated

    search_by_most_viewed: function
        Searches doujin based on most viewed

    search_by_title: function
        Searches doujin based on title

    search_by_random: function
        Searches doujin based on random with query
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

        return string.replace(' ', '+')

    def __init__(self, api_key: str = ''):
        """Initializes the Pururin.

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

        self.specs['g'] = book

        try:
            book = int(book)
        except ValueError:
            raise ValueError('Book must be an int')

        data = requests.get(BASE_URL.pururin, params=self.specs)
        if data.json()['type'] is None:
            raise ValueError('No results found')

        self.final = json.loads(Pururin.better_object(data.json()))

        return Pururin.better_object(self.final)


    async def search_by_newest(self, query: str):
        """Search for doujin based on newest 

        path: https://pururin.to/search/most-popular?q=alter

        Parameters
        ----------
        query : str
            The query to search for

        Raises
        ------
        ValueError
            If the doujin is not found.

        Returns
        -------
        dict
            The list object that represents the newest doujin response.
        """

        self.specs['query'] = query
        self.specs['sort'] = "newest"
        query = Pururin.auto_space(query)

        if query == '':
            raise ValueError('Query must be given')
        data = requests.get(BASE_URL.pururin + 'args.php', params=self.specs)

        if len(data.json()) == 0:
            raise ValueError('No results found')

        return Pururin.better_object(data.json())


    async def search_by_most_popular(self, query: str):
        """Search doujins by most popular

        path: https://pururin.to/search/most-popular?q=alter

        Parameters
        ----------
        query : str
            The query to search for

        Raises
        ------
        ValueError
            If the doujin is not found.

        Returns
        -------
        dict
            The list object that represents the popular doujin response.
        """

        self.specs['query'] = query
        self.specs['sort'] = "most-popular"
        query = Pururin.auto_space(query)

        if query == '':
            raise ValueError('Query must be given')
        data = requests.get(BASE_URL.pururin + 'args.php', params=self.specs)

        if len(data.json()) == 0:
            raise ValueError('No results found')

        return Pururin.better_object(data.json())


    async def search_by_highest_rated(self, query: str):
        """Search for doujin based on the highest rated

        path: https://pururin.to/search/highest-rated?q=alter

        Parameters
        ----------
        query : str
            The query to search for

        Raises
        ------
        ValueError
            If the doujin is not found.

        Returns
        -------
        dict
            The list object that represents the highest rated doujin response.
        """

        self.specs['query'] = query
        self.specs['sort'] = "highest-rated"
        query = Pururin.auto_space(query)

        if query == '':
            raise ValueError('Query must be given')
        data = requests.get(BASE_URL.pururin + 'args.php', params=self.specs)

        if len(data.json()) == 0:
            raise ValueError('No results found')

        return Pururin.better_object(data.json())


    async def search_by_most_viewed(self, query: str):
        """Search for doujin based on the most viewed

        path: https://pururin.to/search/most-viewed?q=alter

        Parameters
        ----------
        query : str
            The query to search for

        Raises
        ------
        ValueError
            If the doujin is not found.

        Returns
        -------
        dict
            The list object that represents the most viewed doujin response.
        """

        self.specs['query'] = query
        self.specs['sort'] = "most-viewed"
        query = Pururin.auto_space(query)

        if query == '':
            raise ValueError('Query must be given')
        data = requests.get(BASE_URL.pururin + 'args.php', params=self.specs)

        if len(data.json()) == 0:
            raise ValueError('No results found')

        return Pururin.better_object(data.json())


    async def search_by_title(self, query: str):
        """Search for doujin based on title

        path: https://pururin.to/search/title?q=alter

        Parameters
        ----------
        query : str
            The query to search for

        Raises
        ------
        ValueError
            If the doujin is not found.

        Returns
        -------
        dict
            The list object that represents the doujin response according to the title.
        """

        self.specs['query'] = query
        self.specs['sort'] = "title"
        query = Pururin.auto_space(query)

        if query == '':
            raise ValueError('Query must be given')
        data = requests.get(BASE_URL.pururin + 'args.php', params=self.specs)

        if len(data.json()) == 0:
            raise ValueError('No results found')

        return Pururin.better_object(data.json())


    async def search_by_random(self, query: str):
        """Search for doujin based on random

        path: https://pururin.to/search/random?q=alter

        Parameters
        ----------
        query : str
            The query to search for

        Raises
        ------
        ValueError
            If the doujin is not found.

        Returns
        -------
        dict
            The list object that represents the doujin response according query and mixed to random.
        """

        self.specs['query'] = query
        self.specs['sort'] = "random"
        query = Pururin.auto_space(query)

        if query == '':
            raise ValueError('Query must be given')
        data = requests.get(BASE_URL.pururin + 'args.php', params=self.specs)

        if len(data.json()) == 0:
            raise ValueError('No results found')

        return Pururin.better_object(data.json())


    async def get_random(self):
        """Gets random doujin on pururin

        Returns
        -------
        dict
            The book object that represents the random doujin response.
        """
        data = requests.get(BASE_URL.pururin + 'random' + '/', params=self.specs)

        return Pururin.better_object(data.json())

    async def get_random_with_query(self, query: str):
        """Gets doujin on pururin by query

        path: https://pururin.to/search?q=alter

        Parameters
        ----------
        query : str
            The query to search for

        Raises
        ------
        ValueError
            If the doujin is not found.

        Returns
        -------
        dict
            The book object that represents the doujin response according to the query
        """

        self.specs['p'] = query
        query = Pururin.auto_space(query)
        data = requests.get(BASE_URL.pururin + 'search.php', params=self.specs)

        if data.json()['type'] is None:
            raise ValueError('No results found')

        return Pururin.better_object(data.json())
