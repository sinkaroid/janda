import json
import re
from datetime import datetime

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
    """

    def __init__(
        self,
        BASE_PURURIN: str = f"{JANDA}/pururin",
        BASE_NHENTAI: str = f"{JANDA}/nhentai",
        BASE_HENTAIFOX: str = f"{JANDA}/hentaifox",
        BASE_HENTAI2READ: str = f"{JANDA}/hentai2read",
        BASE_SIMPLY_HENTAI: str = f"{JANDA}/simply-hentai",
        BASE_ASMHENTAI: str = f"{JANDA}/asmhentai",
    ):
        self.nhentai = BASE_NHENTAI
        self.pururin = BASE_PURURIN
        self.hentaifox = BASE_HENTAIFOX
        self.hentai2read = BASE_HENTAI2READ
        self.simply_hentai = BASE_SIMPLY_HENTAI
        self.asmhentai = BASE_ASMHENTAI


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
    ]
    return api_list


def auto_space(string: str):
    """Automatically adds spaces for GET requests

    Parameters
    ----------
    string : str
        The string to be formatted.

    Returns
    -------
    str

    """
    return string.replace(" ", "+")


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
    return json.dumps(parser, sort_keys=True, indent=4, ensure_ascii=False)


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
