import requests
import json
from .utils.parser import *

BASE_URL = Api()

class Hentai2read(object):
    """ Hentai2read API wrapper 
    
    Methods
    -------
    get : function
        Gets doujin from path given

    search : function
        Search for doujin based on the latest

    get_random : function
        Gets random doujin on Hentai2read
    """

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
            The book object that represents the specific id response.
        """

        ## if path contains '/' then remove it
        if '/' in path:
            path = path.replace('/', '')
        
        self.specs['u'] = path + '/' + str(chapter)


        try:
            path = str(path)
        except ValueError:
            raise ValueError('Path must be a str')

        data = requests.get(BASE_URL.hentai2read, params=self.specs)

        self.final = json.loads(better_object(data.json()), encoding="utf-8")
   
        if self.final["title"] is '':
            raise ValueError('No results. Make sure you spelled everything right.')

        return better_object(self.final)

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

        self.specs['query'] = query

        query = auto_space(query)

        if query == '':
            raise ValueError('Query must be given')
        data = requests.get(BASE_URL.hentai2read + 'args.php', params=self.specs)

        # if data.json() length is 0, then throw error
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
        data = requests.get(BASE_URL.hentai2read + 'random' + '/', params=self.specs)

        return better_object(data.json())

