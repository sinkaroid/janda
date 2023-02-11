import json
from janda import __version__

JANDA = "https://janda.mod.land"


class Api:
    """Api class

    This class is used to parse the data from the api.

    Attributes:
        pururin (str): The base url of pururin api.
        hentaifox (str): The base url of hentaifox api.
        hentai2read (str): The base url of hentai2read api.
        simply_hentai (str): The base url of simply-hentai api.
        qhentai (str): The base url of qhentai api.
        asmhentai (str): The base url of asmhentai api.
        3hentai (str): The base url of 3hentai api.
        header (dict): The header for request.

        endpoint_book (str): The endpoint for get book.
        endpoint_search (str): The endpoint for search book.
        endpoint_random (str): The endpoint for get random book.
        endpoint_related (str): The endpoint for get related book.
    """

    def __init__(
        self,
        BASE_PURURIN: str = f"{JANDA}/pururin",
        BASE_NHENTAI: str = f"{JANDA}/nhentai",
        BASE_HENTAIFOX: str = f"{JANDA}/hentaifox",
        BASE_HENTAI2READ: str = f"{JANDA}/hentai2read",
        BASE_SIMPLY_HENTAI: str = f"{JANDA}/simply-hentai",
        BASE_ASMHENTAI: str = f"{JANDA}/asmhentai",
        BASE_3HENTAI: str = f"{JANDA}/3hentai",
        BASE_HEADER: dict = {
            "User-Agent": f"janda/v{__version__} (https://pypi.org/project/janda);",
            "From": "hey@sinkaroid.org",
        },
        BASE_ENDPOINT_BOOK: str = "/get?book=",
        BASE_ENDPOINT_SEARCH: str = "/search?key=",
        BASE_ENDPOINT_RANDOM: str = "/random",
        BASE_ENDPOINT_RELATED: str = "/related?book=",
     
    ):
        self.nhentai = BASE_NHENTAI
        self.pururin = BASE_PURURIN
        self.hentaifox = BASE_HENTAIFOX
        self.hentai2read = BASE_HENTAI2READ
        self.simply_hentai = BASE_SIMPLY_HENTAI
        self.asmhentai = BASE_ASMHENTAI
        self.thentai = BASE_3HENTAI
        self.header = BASE_HEADER
        self.endpoint_book = BASE_ENDPOINT_BOOK
        self.endpoint_search = BASE_ENDPOINT_SEARCH
        self.endpoint_random = BASE_ENDPOINT_RANDOM
        self.endpoint_related = BASE_ENDPOINT_RELATED


BASE_URL = Api()


def list_api():
    """Returns the api url.

    Returns
    -------
    list
    """
    # create list of api
    api_list = [
        BASE_URL.nhentai,
        BASE_URL.pururin,
        BASE_URL.hentaifox,
        BASE_URL.hentai2read,
        BASE_URL.simply_hentai,
        BASE_URL.asmhentai,
        BASE_URL.thentai,
    ]
    return api_list


def better_object(parser: dict):
    """Converts the json object to a more readable object.

    Parameters
    ----------
    parser : dict

    Returns
    -------
    str
       deserialized json as string

    """
    return json.dumps(parser, indent=4, ensure_ascii=False)


def resolve(b_object: dict) -> dict:
    """Resolves the json object meant data with bad formatting, arbitary indent, arbitary sort keys but it is resolved and ready to extends
    Parameters
    ----------
    b_object : dict
    Returns
    -------
    dict
        raw json object
    """
    return json.loads(b_object)
