import json
import re
from datetime import datetime


class Api():
    """Api class

    This class is used to parse the data from the api.

    Attributes:
        api (str): The base url of nhentai api.
        img (str): The base url of nhentai image.
        pururin (str): The base url of pururin api.
        hentaifox (str): The base url of hentaifox api.
        hentai2read (str): The base url of hentai2read api.
        simply_hentai (str): The base url of simply-hentai api.
        qhentai (str): The base url of qhentai api.
        asmhentai (str): The base url of asmhentai api.
    """

    def __init__(self,
                 BASE_URL: str = "https://nhentai.net",
                 BASE_IMG: str = "https://i.nhentai.net/galleries",
                 BASE_THUMBNAIL: str = "https://t.nhentai.net/galleries",
                 BASE_PURURIN: str = "https://scathach.redsplit.org/v4/pururin/",
                 BASE_NHENTAI_UNBLOCK: str = "https://nhentai.sinxdr.workers.dev",
                 BASE_HENTAIFOX: str = "https://scathach.redsplit.org/v4/hentaifox/",
                 BASE_HENTAI2READ: str = "https://scathach.redsplit.org/v4/hentai2read/",
                 BASE_SIMPLY_HENTAI: str = "https://scathach.redsplit.org/v4/simply-hentai/",
                 BASE_QHENTAI: str = "https://scathach.redsplit.org/v4/qhentai/",
                 BASE_ASMHENTAI: str = "https://scathach.redsplit.org/v4/asmhentai/"):

        self.api = BASE_URL
        self.img = BASE_IMG
        self.thumbnail = BASE_THUMBNAIL
        self.pururin = BASE_PURURIN
        self.hentaifox = BASE_HENTAIFOX
        self.hentai2read = BASE_HENTAI2READ
        self.nhentai_unblock = BASE_NHENTAI_UNBLOCK
        self.simply_hentai = BASE_SIMPLY_HENTAI
        self.qhentai = BASE_QHENTAI
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
        BASE_URL.api,
        BASE_URL.pururin,
        BASE_URL.hentaifox,
        BASE_URL.hentai2read,
        BASE_URL.simply_hentai,
        BASE_URL.qhentai,
        BASE_URL.asmhentai
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
    return string.replace(' ', '+')


def just_number(string: str):
    """Remove the non-numeric characters from a string.

    Parameters
    ----------
    string : str
        The desired string.

    Returns
    -------
    str
    """
    return re.sub(r'\D', '', string)


def better_object(parser: dict):
    """Converts the json object to a more readable object.

    Parameters
    ----------
    parser : dict

    Returns
    -------
    dict

    """
    return json.dumps(parser, sort_keys=True, indent=4, ensure_ascii=False)


def readable_timestamp(timestamp: int):
    """Converts a timestamp to a datetime object.

    Parameters
    ----------
    timestamp : int
        The timestamp to be converted.

    Returns
    -------
    str
    """
    return datetime.utcfromtimestamp(int(timestamp)).strftime('%Y-%m-%d %H:%M:%S')


def preg_match_tags(tags: dict):
    """Parses the tags and returns a list of tags.

    Parameters
    ----------
    tags : dict
        Tags object

    Returns
    -------
    list
    """

    tags_name = []
    for tag in tags:
        tags_name.append(tag['name'])
    return tags_name


def get_language_in_tags(tags: dict):
    """Parses language value

    Parameters
    ----------
    tags : dict
        Tags object

    Returns
    -------
    str
    """

    for tag in tags:
        if tag['type'] == 'language':
            return tag['name']


def parser(obj: dict):
    """Make better list

    Parameters
    ----------
    obj : dict
        The object to be parsed.

    Returns
    -------
    list
    """

    raw_object = json.loads(better_object(obj), encoding="utf-8")
    media = raw_object['media_id']

    book_object = {
        'details': {
            'id': raw_object['id'],
            'title': raw_object['title'],
            'link': f'https://nhentai.net/g/{raw_object["id"]}',
            'upload_date': readable_timestamp(raw_object['upload_date'])
        },
        'scanlator': raw_object['scanlator'],
        'num_pages': raw_object['num_pages'],
        'num_favorites': raw_object['num_favorites']}

    tags = []
    for tag in raw_object['tags']:
        tags.append(tag['name'])
    book_object['tags'] = tags

    for tag in raw_object['tags']:
        if tag['type'] == 'language':
            book_object['language'] = tag['name']
            break

    image_urls = []
    for image in raw_object['images']['pages']:

        if image['t'] == 'p':
            image_urls.append(
                f'{BASE_URL.img}/{media}/{len(image_urls) + 1}.png')

        elif image['t'] == 'j':
            image_urls.append(
                f'{BASE_URL.img}/{media}/{len(image_urls) + 1}.jpg')

        elif image['t'] == 'g':
            image_urls.append(
                f'{BASE_URL.img}/{media}/{len(image_urls) + 1}.gif')

    book_object['image_urls'] = image_urls

    thumbnail_urls = []
    for image in raw_object['images']['pages']:
        if image['t'] == 'p':
            thumbnail_urls.append(
                f'{BASE_URL.thumbnail}/{media}/{len(thumbnail_urls) + 1}t.png')

        elif image['t'] == 'j':
            thumbnail_urls.append(
                f'{BASE_URL.thumbnail}/{media}/{len(thumbnail_urls) + 1}t.jpg')

        elif image['t'] == 'g':
            thumbnail_urls.append(
                f'{BASE_URL.thumbnail}/{media}/{len(thumbnail_urls) + 1}t.gif')

    book_object['thumbnail_urls'] = thumbnail_urls
    return better_object(book_object)


def neat_result(obj: dict):
    """Make better list

    Parameters
    ----------
    parser : dict
        The json object to be parsed.

    Returns
    -------
    dict

    """
    raw_object = json.loads(better_object(obj), encoding="utf-8")
    results = raw_object['result']

    results_object = []
    for result in results:
        results_object.append({
            'id': result['id'],
            'title': result['title'],
            'link': f'https://nhentai.net/g/{result["id"]}',
            'upload_date': readable_timestamp(result['upload_date']),
            'num_pages': result['num_pages'],
            'num_favorites': result['num_favorites'],
            'language': get_language_in_tags(result['tags']),
            'tags': preg_match_tags(result['tags'])
        })

    return better_object(results_object)
