import requests
import json
from .utils.parser import *

BASE_URL = Api()

class Nhentai(object):    
    """ Nhentai API wrapper 
    
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

    async def get(self, book: int, safe: bool = None):
        """Get doujin API from Id

        Parameters
        ----------
        book : int
            Nmber id of the book

        safe : bool
            If True, janda will throw you error whenever contains minor content, such as loli or shota. Default is False

        Raises
        ------
        ValueError
            If the doujin is not found.

        Returns
        -------
        dict
        """

        try:

            if isinstance(book, int):
                book = str(book)

            self.book = str(just_number(book))

        except ValueError:
            raise ValueError('Book must be contain int')

        data = requests.get(F'{BASE_URL.api}/api/gallery/{self.book}')
        if data.status_code == 404:
            raise ValueError('Book not found')

        if data.status_code != 200:
            raise ValueError('Request failed')

        self.tags = preg_match_tags(data.json()['tags'])

        if safe is True:
            if 'lolicon' in self.tags or 'shotacon' in self.tags:
                raise ValueError('Book contains minor content')
        
        return parser(data.json())


    async def search(self, tags: str, page: int = 1, popular: str = 'today'):
        """Search doujin by tags / artis / character / parody or group

        Parameters
        ----------
        tags : str
            Tags to search for.

        page : int
            Page number. Default is 1.

        popular : str
            today, all, and week. Default is today.

        Raises
        ------
        ValueError
            If the doujin is not found.

        Returns
        -------
        dict
        """

        if popular not in ['today', 'all', 'week']:
            raise ValueError('popular must be today, all, or week')

        self.specs['query'] = tags
        self.specs['page'] = page
        self.specs['popular'] = popular

        data = requests.get(
            f'{BASE_URL.api}/api/galleries/search', params=self.specs)

        if data.status_code == 404:
            raise ValueError('No results')

        if data.status_code != 200:
            raise ValueError('Request failed')


        self.raw_object = json.loads(better_object(data.json()), encoding="utf-8")
        self.results = self.raw_object['result']

        self.results_object = []
        for result in self.results:
            self.results_object.append({
                'id': result['id'],
                'title': result['title'],
                'link': f'https://nhentai.net/g/{result["id"]}',
                'upload_date': readable_timestamp(result['upload_date']),
                'num_pages': result['num_pages'],
                'num_favorites': result['num_favorites'],
                'language': get_language_in_tags(result['tags']),
                'tags': preg_match_tags(result['tags'])
            })

        return better_object(self.results_object)


    async def search_related(self, book: int):
        """Get related book API from book ID or book link

        Parameters
        ----------
        book : int
            Nmber id of the book

        Raises
        ------
        ValueError
            If the doujin is not found.

        Returns
        -------
        dict
        """

        try:
            if isinstance(book, int):
                book = str(book)

            self.book = str(just_number(book))

        except ValueError:
            raise ValueError('Book must be an int')

        data = requests.get(F'{BASE_URL.api}/api/gallery/{self.book}/related')

        if data.status_code != 200:
            raise ValueError('Request failed')

        return neat_result(data.json())

    async def get_random(self):
        """Get random doujin
        
        Raises
        ------
        ValueError
            If the doujin is not found.

        Returns
        -------
        dict
        """
        random = requests.get(F'{BASE_URL.api}/random')

        try:
            self.book = str(just_number(random.url))

        except ValueError:
            raise ValueError('Uh oh something wrong here')

        data = requests.get(F'{BASE_URL.api}/api/gallery/{self.book}')
        
        if data.status_code == 404:
            raise ValueError('Error')

        if data.status_code != 200:
            raise ValueError('Request failed')

        return parser(data.json())
        
