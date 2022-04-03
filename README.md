<div align="center">
<a href="https://sinkaroid.github.io/janda"><img width="450" src="https://cdn.discordapp.com/attachments/952117487166705747/952942740545634344/janda.png" alt="janda"></a>

<h4 align="center">A featureful Python library covers most popular doujin API</h4>

<p align="center">
	<a href="https://github.com/sinkaroid/janda/actions/workflows/build.yml"><img src="https://github.com/sinkaroid/janda/actions/workflows/build.yml/badge.svg"></a>
	<a href="https://github.com/sinkaroid/janda/actions/workflows/api.yml"><img src="https://github.com/sinkaroid/janda/actions/workflows/api.yml/badge.svg"></a>
	<a href="https://codeclimate.com/github/sinkaroid/janda/maintainability"><img src="https://api.codeclimate.com/v1/badges/7c53330c7a3c0c2a2006/maintainability"></a>
</p>

Built on minimalist dependencies to resolves and interacts with ease.
It takes a much more dictionaries rather than just raw data, and hope will be extendable. Janda has plenty api support apart from nhentai.

<a href="https://github.com/sinkaroid/janda/blob/master/CONTRIBUTING.md">Contributing</a> •
<a href="https://sinkaroid.github.io/janda">Documentation</a> •
<a href="https://github.com/sinkaroid/janda/issues/new/choose">Report Issues</a>
</div>

---

## Janda vs. the Competition

Built on minimalist dependencies, yet it covers most of the popular doujin API.  
Every single site has different dictionaries returns. Keep in mind on this

| Site                                              | Status                                                                                | Process      |
|---------------------------------------------------|---------------------------------------------------------------------------------------|--------------|
| ✅ [nhentai](https://nhentai.net/)                 | [![status](https://img.shields.io/badge/status-stable-green)](janda/nhentai.py)       | official api |
| ✅ [pururin](https://pururin.to/)                  | [![status](https://img.shields.io/badge/status-stable-green)](janda/pururin.py)       | proxified    |
| ✅ [hentaifox](https://hentaifox.com/)             | [![status](https://img.shields.io/badge/status-triage-red)](janda/hentaifox.py)       | proxified    |
| ✅ [hentai2read](https://hentai2read.com/)         | [![status](https://img.shields.io/badge/status-partial-blue)](janda/hentai2read.py)   | official api |
| ✅ [simply-hentai](https://www.simply-hentai.com/) | [![status](https://img.shields.io/badge/status-partial-blue)](janda/simply_hentai.py) | proxified    |
| ✅ [qhentai](https://qhentai.net/)                 | [![status](https://img.shields.io/badge/status-partial-blue)](janda/qhentai.py)       | proxified    |
| ✅ [asmhentai](https://asmhentai.com/)             | [![status](https://img.shields.io/badge/status-stable-green)](janda/asmhentai.py)     | proxified    |

> **Stable**: works well | **Triage**: has some issues | **Partial**: works normally with limited endpoints

## Features

- **Easy to use**: check your intelisense
- **Neat**: object taken is re-processed to make it actionable
- **Documented**: fully documented and tested
- **All-in-one**: plenty of site support

## Prerequisites

- Python 3.7 or above
- Can parse JSON
  
<table>
	<td><b>NOTE:</b> Please always use the latest version of the module.
Since this library covers a lot of sites, hence there is always a staged changes
</table>

## Installation
`pip install janda / pipenv install janda`  
- or fork this repo

To use specific API, you could use `from janda import Nhentai`

## Quick example
Some methods require additional parameters, check your intelisense.

### get
`(method) get: (book: int, safe: bool | None = None) -> Coroutine`
```py
import asyncio
from janda import Nhentai

async def book():
    nh = Nhentai()
    data = await nh.get(274003)
    print(data)

async def main():
    await asyncio.gather(book())

asyncio.run(main())
```

### search
`(tags: str, page: int = 1, popular: str = 'today') -> Coroutine`

```py
await nh.search("jeanne alter", 1, "all")
```

## Documentation
The documentation can be found [https://sinkaroid.github.io/janda](https://sinkaroid.github.io/janda)

### Nhentai
- [`Nhentai.get(options)`](https://sinkaroid.github.io/janda/nhentai.html)
  - Get specific doujin from nhentai
- [`Nhentai.search(options)`](https://sinkaroid.github.io/janda/nhentai.html)
  - Search doujin by tags / artist / character / parody or group
- [`Nhentai.search_related(options)`](https://sinkaroid.github.io/janda/nhentai.html)
  - Get related book or almost alike from Id given
- [`Nhentai.get_random()`](https://sinkaroid.github.io/janda/nhentai.html)
  - Get random doujin from nhentai

### Pururin
- [`Pururin.get(options)`](https://sinkaroid.github.io/janda/pururin.html)
  - Get specific doujin from pururin
- [`Pururin.get_random()`](https://sinkaroid.github.io/janda/pururin.html)
  - Get random doujin from pururin
- [`Pururin.get_random_with_query(options)`](https://sinkaroid.github.io/janda/pururin.html)
  - Get random doujin from pururin with query
- [`Pururin.search_by_highest_rated(options)`](https://sinkaroid.github.io/janda/pururin.html)
  - Search highest rated doujin from pururin
- [`Pururin.search_by_most_popular(options)`](https://sinkaroid.github.io/janda/pururin.html) 
  - Search most popular doujin from pururin
- [`Pururin.search_by_most_viewed(options)`](https://sinkaroid.github.io/janda/pururin.html)
  - Search most viewed doujin from pururin
- [`Pururin.search_by_newest(options)`](https://sinkaroid.github.io/janda/pururin.html) 
  - Search newest doujin from pururin
- [`Pururin.search_by_random(options)`](https://sinkaroid.github.io/janda/pururin.html)
  - Search random doujin with query from pururin
- [`Pururin.search_by_title(options)`](https://sinkaroid.github.io/janda/pururin.html)
  - Search doujin by title given from pururin

### Hentai2read
- [`Hentai2read.get(options)`](https://sinkaroid.github.io/janda/hentai2read.html)
  - Get specific doujin from hentai2read
- [`Hentai2read.get_random()`](https://sinkaroid.github.io/janda/hentai2read.html)
  - Get random doujin from hentai2read
- [`Hentai2read.search(options)`](https://sinkaroid.github.io/janda/hentai2read.html)
  - Search a doujin from hentai2read by latest only

### Simplyhentai
- [`Simplyhentai.get(options)`](https://sinkaroid.github.io/janda/simply_hentai.html)
  - Get specific doujin from simplyhentai
- [`Simplyhentai.get_related(options)`](https://sinkaroid.github.io/janda/simply_hentai.html)
  - Get doujin related from specific path given
- [`Simplyhentai.get_random()`](https://sinkaroid.github.io/janda/simply_hentai.html)
  - Get random doujin from simply-hentai

### Hentaifox
- [`Hentaifox.get(options)`](https://sinkaroid.github.io/janda/hentaifox.html)
  - Get specific doujin from hentaifox
- [`Hentaifox.get_random()`](https://sinkaroid.github.io/janda/hentaifox.html) 
  - Get random doujin from hentaifox
- [`Hentaifox.search_by_latest(options)`](https://sinkaroid.github.io/janda/hentaifox.html)
  - Search latest doujin from hentaifox
- [`Hentaifox.search_by_popular(options)`](https://sinkaroid.github.io/janda/hentaifox.html)
  - Search popular doujin from hentaifox

### Qhentai
- [`Qhentai.get(options)`](https://sinkaroid.github.io/janda/qhentai.html)
  - Get specific doujin from qhentai
- [`Qhentai.search(options)`](https://sinkaroid.github.io/janda/qhentai.html)
  - Search a doujin from qhentai, can providing with page number
- [`Qhentai.get_random()`](https://sinkaroid.github.io/janda/qhentai.html)
  - Get random doujin from qhentai

### Asmhentai
- [`Asmhentai.get(options)`](https://sinkaroid.github.io/janda/asmhentai.html)
  - Get specific doujin from asmhentai
- [`Asmhentai.search(options)`](https://sinkaroid.github.io/janda/asmhentai.html)
  - Search a doujin from asmhentai, can providing with page number
- [`Asmhentai.get_random()`](https://sinkaroid.github.io/janda/asmhentai.html)
  - Get random doujin from asmhentai

## Returns example
`get` method will represent as **Book Object** and packed with actionable image urls
```js
{
    "details": {
        "id": 274003,
        "link": "https://nhentai.net/g/274003",
        "title": {
            "english": "(COMIC1☆15) [Koniro Kajitsu (Konka)] Setsudo no Nai Onee-chan de Gomen ne | Onee-chan is sorry she has no restraint (Fate/Grand Order) [English]",
            "japanese": "(COMIC1☆15) [紺色果実 (紺菓)] 節度のないお姉ちゃんでごめんね♡ (Fate/Grand Order) [英訳]",
            "pretty": "Setsudo no Nai Oneechan is sorry she has no restraint"
        },
        "upload_date": "2019-06-01 02:09:13"
    },
    "image_urls": [
        "https://i.nhentai.net/galleries/1423853/1.png",
        "https://i.nhentai.net/galleries/1423853/2.png",
        "https://i.nhentai.net/galleries/1423853/3.png",
        "https://i.nhentai.net/galleries/1423853/4.png",
        "https://i.nhentai.net/galleries/1423853/5.png",
        "https://i.nhentai.net/galleries/1423853/6.png",
        "https://i.nhentai.net/galleries/1423853/7.png",
        "https://i.nhentai.net/galleries/1423853/8.png",
        "https://i.nhentai.net/galleries/1423853/9.png",
        "https://i.nhentai.net/galleries/1423853/10.png",
        "https://i.nhentai.net/galleries/1423853/11.png",
        "https://i.nhentai.net/galleries/1423853/12.png",
        "https://i.nhentai.net/galleries/1423853/13.png",
        "https://i.nhentai.net/galleries/1423853/14.png",
        "https://i.nhentai.net/galleries/1423853/15.png",
        "https://i.nhentai.net/galleries/1423853/16.png",
        "https://i.nhentai.net/galleries/1423853/17.png",
        "https://i.nhentai.net/galleries/1423853/18.png",
        "https://i.nhentai.net/galleries/1423853/19.png",
        "https://i.nhentai.net/galleries/1423853/20.png",
        "https://i.nhentai.net/galleries/1423853/21.png",
        "https://i.nhentai.net/galleries/1423853/22.png",
        "https://i.nhentai.net/galleries/1423853/23.png",
        "https://i.nhentai.net/galleries/1423853/24.png",
        "https://i.nhentai.net/galleries/1423853/25.png",
        "https://i.nhentai.net/galleries/1423853/26.png"
    ],
    "language": "english",
    "num_favorites": 6164,
    "num_pages": 26,
    "scanlator": "",
    "tags": [
        "english",
        "translated",
        "fate grand order",
        "tomoe gozen",
        "koniro kajitsu",
        "konka",
        "shotacon",
        "sole male",
        "big breasts",
        "footjob",
        "horns",
        "lactation",
        "lingerie",
        "oni",
        "sole female",
        "stockings",
        "doujinshi",
        "gudao",
        "schoolgirl uniform",
        "kissing",
        "leg lock",
        "breast feeding",
        "x-ray",
        "unusual pupils"
    ],
    "thumbnail_urls": [
        "https://t.nhentai.net/galleries/1423853/1t.png",
        "https://t.nhentai.net/galleries/1423853/2t.png",
        "https://t.nhentai.net/galleries/1423853/3t.png",
        "https://t.nhentai.net/galleries/1423853/4t.png",
        "https://t.nhentai.net/galleries/1423853/5t.png",
        "https://t.nhentai.net/galleries/1423853/6t.png",
        "https://t.nhentai.net/galleries/1423853/7t.png",
        "https://t.nhentai.net/galleries/1423853/8t.png",
        "https://t.nhentai.net/galleries/1423853/9t.png",
        "https://t.nhentai.net/galleries/1423853/10t.png",
        "https://t.nhentai.net/galleries/1423853/11t.png",
        "https://t.nhentai.net/galleries/1423853/12t.png",
        "https://t.nhentai.net/galleries/1423853/13t.png",
        "https://t.nhentai.net/galleries/1423853/14t.png",
        "https://t.nhentai.net/galleries/1423853/15t.png",
        "https://t.nhentai.net/galleries/1423853/16t.png",
        "https://t.nhentai.net/galleries/1423853/17t.png",
        "https://t.nhentai.net/galleries/1423853/18t.png",
        "https://t.nhentai.net/galleries/1423853/19t.png",
        "https://t.nhentai.net/galleries/1423853/20t.png",
        "https://t.nhentai.net/galleries/1423853/21t.png",
        "https://t.nhentai.net/galleries/1423853/22t.png",
        "https://t.nhentai.net/galleries/1423853/23t.png",
        "https://t.nhentai.net/galleries/1423853/24t.png",
        "https://t.nhentai.net/galleries/1423853/25t.png",
        "https://t.nhentai.net/galleries/1423853/26t.png"
    ]
}
```

Otherwise `search` will return 25 **List Object** of search results.
```js
[
    {
        "id": 394795,
        "language": "speechless",
        "link": "https://nhentai.net/g/394795",
        "num_favorites": 962,
        "num_pages": 5,
        "tags": [
            "big breasts",
            "swimsuit",
            "mmf threesome",
            "group",
            "uncensored",
            "nakadashi",
            "dark skin",
            "bikini",
            "x-ray",
            "double penetration",
            "blowjob",
            "muscle",
            "collar",
            "body writing",
            "doujinshi",
            "speechless",
            "text cleaned",
            "fate grand order",
            "sole female",
            "jeanne alter",
            "yanje"
        ],
        "title": {
            "english": "[Yanje] Jeanne d'Arc Alter (FGO) [Textless]",
            "japanese": "",
            "pretty": "Jeanne d'Arc Alter"
        },
        "upload_date": "2022-03-08 01:00:47"
    },
    {
        "id": "394794",
        "language": "japanese",
        "link": "https://nhentai.net/g/394794",
        "num_favorites": 1103,
        "num_pages": 5,
        "tags": [
            "big breasts",
            "swimsuit",
            "japanese",
            "mmf threesome",
            "group",
            "uncensored",
            "nakadashi",
            "dark skin",
            "bikini",
            "x-ray",
            "double penetration",
            "blowjob",
            "muscle",
            "collar",
            "body writing",
            "doujinshi",
            "fate grand order",
            "sole female",
            "jeanne alter",
            "yanje"
        ],
        "title": {
            "english": "[Yanje] Jeanne d'Arc Alter (FGO) [Japanese]",
            "japanese": "",
            "pretty": "Jeanne d'Arc Alter"
        },
        "upload_date": "2022-03-07 23:32:20"
    }
]
```

## Known Issues
#### `UnicodeEncodeError: 'charmap' codec can't encode characters`  
- It's raised when the title contains non-ascii characters, then your console can't parse them, use real console don't Git-bash.

## Legal
This tool can be freely copied, modified, altered, distributed without any attribution whatsoever. However, if you feel
like this tool deserves an attribution, mention it. It won't hurt anybody

## Pronunciation
[`id_ID`](https://www.localeplanet.com/java/id-ID/index.html) • **/jan·da/** — wanita yang menjanda karena ditinggal suaminya; _(?)_ the mascot is tomoe gozen FGO

## EoF
All books from those doujinboards are definitely ilegal from original authors.