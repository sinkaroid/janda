<div align="center">
<a href="https://sinkaroid.github.io/janda"><img width="470" src="https://cdn.discordapp.com/attachments/952117487166705747/952942740545634344/janda.png" alt="janda"></a>

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

Built on minimalist dependencies, yet it covers most of the popular doujinboards.  
Every single site has different dictionaries return, keep in mind on this

| Client        | Status                                                                                                                              | Get   | Search | Randomizer |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----- | ------ | ---------- |
| nhentai       | [![status](https://img.shields.io/badge/status-stable-green)](https://github.com/sinkaroid/janda/actions/workflows/nhentai.yml)     | `Yes` | `Yes`  | `Yes`      |
| pururin       | [![status](https://img.shields.io/badge/status-stable-green)](https://github.com/sinkaroid/janda/actions/workflows/pururin.yml)     | `Yes` | `Yes`  | `Yes`      |
| hentaifox     | [![status](https://img.shields.io/badge/status-stable-green)](https://github.com/sinkaroid/janda/actions/workflows/hentaifox.yml)   | `Yes` | `Yes`  | `Yes`      |
| hentai2read   | [![status](https://img.shields.io/badge/status-partial-blue)](https://github.com/sinkaroid/janda/actions/workflows/hentai2read.yml) | `Yes` | `Yes`  | `No`       |
| simply-hentai | [![status](https://img.shields.io/badge/status-triage-red)](https://github.com/sinkaroid/janda/actions/workflows/simplyh.yml)       | `Yes` | `No`   | `No`       |
| asmhentai     | [![status](https://img.shields.io/badge/status-stable-green)](https://github.com/sinkaroid/janda/actions/workflows/asmhentai.yml)   | `Yes` | `Yes`  | `Yes`      |


## Features

- **Easy to use**: check your intelisense
- **Neat**: object taken is re-appended to make it actionable
- **Documented**: fully documented and tested
- **All-in-one**: plenty of site support

## Prerequisites

- Python 3.7 or above
- Can parse JSON
  
<table>
	<td><b>NOTE:</b> Please always use the latest version of the module.<br>
Since this library covers a lot of sites, hence there is always a staged changes
</table>

## 🚀Installation
`pip install janda / pipenv install janda`  
- or fork this repo

To use specific site apis, You could specify import too, for example:
- `from janda import Nhentai`

then initializes the client, an [api key](https://scathach.dev/dashboard) is optional

## Quick example
Some methods require additional parameters, check your intelisense.

### get
`(method) get: (book: int, safe: bool | None = None) -> Coroutine`
```py
import asyncio
from janda import Nhentai, resolve

async def book():
    nh = Nhentai()
    data = await nh.get(274003)
    print(data) ## unresolved
    print(resolve(data)) ## resolved

async def main():
    await asyncio.gather(book())

asyncio.run(main())
```
The final step you must resolve them to works with data. See [#Unresolved JSON](#unresolved-json)  
Authorization is always optional! but if you fill it you should define through specific import

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
- [`Pururin.search(options)`](https://sinkaroid.github.io/janda/pururin.html)
  - Search doujin by tags / artist / character / parody or group


### Hentai2read
- [`Hentai2read.get(options)`](https://sinkaroid.github.io/janda/hentai2read.html)
  - Get specific doujin from hentai2read
- [`Hentai2read.search(options)`](https://sinkaroid.github.io/janda/hentai2read.html)
  - Search a doujin from hentai2read by latest only

### Simplyhentai
- [`Simplyhentai.get(options)`](https://sinkaroid.github.io/janda/simply_hentai.html)
  - Get specific doujin from simplyhentai

### Hentaifox
- [`Hentaifox.get(options)`](https://sinkaroid.github.io/janda/hentaifox.html)
  - Get specific doujin from hentaifox
- [`Hentaifox.get_random()`](https://sinkaroid.github.io/janda/hentaifox.html) 
  - Get random doujin from hentaifox
- [`Hentaifox.search(options)`](https://sinkaroid.github.io/janda/hentaifox.html)
  - Search doujin by tags / artist / character / parody or group 


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
    "data": {
        "artist": [
            "shindol"
        ],
        "characters": [],
        "group": null,
        "id": 177013,
        "image": [
            "https://i.nhentai.net/galleries/987560/1.jpg",
            "https://i.nhentai.net/galleries/987560/2.jpg",
            "https://i.nhentai.net/galleries/987560/3.jpg",
            "https://i.nhentai.net/galleries/987560/4.jpg",
            "https://i.nhentai.net/galleries/987560/5.jpg",
            "https://i.nhentai.net/galleries/987560/6.jpg",
            "https://i.nhentai.net/galleries/987560/7.jpg",
            "https://i.nhentai.net/galleries/987560/8.jpg",
            "https://i.nhentai.net/galleries/987560/9.jpg",
            "https://i.nhentai.net/galleries/987560/10.jpg",
            "https://i.nhentai.net/galleries/987560/11.jpg",
            "https://i.nhentai.net/galleries/987560/12.jpg",
            "https://i.nhentai.net/galleries/987560/13.jpg",
            "https://i.nhentai.net/galleries/987560/14.jpg",
            "https://i.nhentai.net/galleries/987560/15.jpg",
            "https://i.nhentai.net/galleries/987560/16.jpg",
            "https://i.nhentai.net/galleries/987560/17.jpg",
            "https://i.nhentai.net/galleries/987560/18.jpg",
            "https://i.nhentai.net/galleries/987560/19.jpg",
            "https://i.nhentai.net/galleries/987560/20.jpg",
            "https://i.nhentai.net/galleries/987560/21.jpg",
            "https://i.nhentai.net/galleries/987560/22.jpg",
            "https://i.nhentai.net/galleries/987560/23.jpg",
            "https://i.nhentai.net/galleries/987560/24.jpg",
            "https://i.nhentai.net/galleries/987560/25.jpg",
            "https://i.nhentai.net/galleries/987560/26.jpg",
            "https://i.nhentai.net/galleries/987560/27.jpg",
            "https://i.nhentai.net/galleries/987560/28.jpg",
            "https://i.nhentai.net/galleries/987560/29.jpg",
            "https://i.nhentai.net/galleries/987560/30.jpg",
            "https://i.nhentai.net/galleries/987560/31.jpg",
            "https://i.nhentai.net/galleries/987560/32.jpg",
            "https://i.nhentai.net/galleries/987560/33.jpg",
            "https://i.nhentai.net/galleries/987560/34.jpg",
            "https://i.nhentai.net/galleries/987560/35.jpg",
            "https://i.nhentai.net/galleries/987560/36.jpg",
            "https://i.nhentai.net/galleries/987560/37.jpg",
            "https://i.nhentai.net/galleries/987560/38.jpg",
            "https://i.nhentai.net/galleries/987560/39.jpg",
            "https://i.nhentai.net/galleries/987560/40.jpg",
            "https://i.nhentai.net/galleries/987560/41.jpg",
            "https://i.nhentai.net/galleries/987560/42.jpg",
            "https://i.nhentai.net/galleries/987560/43.jpg",
            "https://i.nhentai.net/galleries/987560/44.jpg",
            "https://i.nhentai.net/galleries/987560/45.jpg",
            "https://i.nhentai.net/galleries/987560/46.jpg",
            "https://i.nhentai.net/galleries/987560/47.jpg",
            "https://i.nhentai.net/galleries/987560/48.jpg",
            "https://i.nhentai.net/galleries/987560/49.jpg",
            "https://i.nhentai.net/galleries/987560/50.jpg",
            "https://i.nhentai.net/galleries/987560/51.jpg",
            "https://i.nhentai.net/galleries/987560/52.jpg",
            "https://i.nhentai.net/galleries/987560/53.jpg",
            "https://i.nhentai.net/galleries/987560/54.jpg",
            "https://i.nhentai.net/galleries/987560/55.jpg",
            "https://i.nhentai.net/galleries/987560/56.jpg",
            "https://i.nhentai.net/galleries/987560/57.jpg",
            "https://i.nhentai.net/galleries/987560/58.jpg",
            "https://i.nhentai.net/galleries/987560/59.jpg",
            "https://i.nhentai.net/galleries/987560/60.jpg",
            "https://i.nhentai.net/galleries/987560/61.jpg",
            "https://i.nhentai.net/galleries/987560/62.jpg",
            "https://i.nhentai.net/galleries/987560/63.jpg",
            "https://i.nhentai.net/galleries/987560/64.jpg",
            "https://i.nhentai.net/galleries/987560/65.jpg",
            "https://i.nhentai.net/galleries/987560/66.jpg",
            "https://i.nhentai.net/galleries/987560/67.jpg",
            "https://i.nhentai.net/galleries/987560/68.jpg",
            "https://i.nhentai.net/galleries/987560/69.jpg",
            "https://i.nhentai.net/galleries/987560/70.jpg",
            "https://i.nhentai.net/galleries/987560/71.jpg",
            "https://i.nhentai.net/galleries/987560/72.jpg",
            "https://i.nhentai.net/galleries/987560/73.jpg",
            "https://i.nhentai.net/galleries/987560/74.jpg",
            "https://i.nhentai.net/galleries/987560/75.jpg",
            "https://i.nhentai.net/galleries/987560/76.jpg",
            "https://i.nhentai.net/galleries/987560/77.jpg",
            "https://i.nhentai.net/galleries/987560/78.jpg",
            "https://i.nhentai.net/galleries/987560/79.jpg",
            "https://i.nhentai.net/galleries/987560/80.jpg",
            "https://i.nhentai.net/galleries/987560/81.jpg",
            "https://i.nhentai.net/galleries/987560/82.jpg",
            "https://i.nhentai.net/galleries/987560/83.jpg",
            "https://i.nhentai.net/galleries/987560/84.jpg",
            "https://i.nhentai.net/galleries/987560/85.jpg",
            "https://i.nhentai.net/galleries/987560/86.jpg",
            "https://i.nhentai.net/galleries/987560/87.jpg",
            "https://i.nhentai.net/galleries/987560/88.jpg",
            "https://i.nhentai.net/galleries/987560/89.jpg",
            "https://i.nhentai.net/galleries/987560/90.jpg",
            "https://i.nhentai.net/galleries/987560/91.jpg",
            "https://i.nhentai.net/galleries/987560/92.jpg",
            "https://i.nhentai.net/galleries/987560/93.jpg",
            "https://i.nhentai.net/galleries/987560/94.jpg",
            "https://i.nhentai.net/galleries/987560/95.jpg",
            "https://i.nhentai.net/galleries/987560/96.jpg",
            "https://i.nhentai.net/galleries/987560/97.jpg",
            "https://i.nhentai.net/galleries/987560/98.jpg",
            "https://i.nhentai.net/galleries/987560/99.jpg",
            "https://i.nhentai.net/galleries/987560/100.jpg",
            "https://i.nhentai.net/galleries/987560/101.jpg",
            "https://i.nhentai.net/galleries/987560/102.jpg",
            "https://i.nhentai.net/galleries/987560/103.jpg",
            "https://i.nhentai.net/galleries/987560/104.jpg",
            "https://i.nhentai.net/galleries/987560/105.jpg",
            "https://i.nhentai.net/galleries/987560/106.jpg",
            "https://i.nhentai.net/galleries/987560/107.jpg",
            "https://i.nhentai.net/galleries/987560/108.jpg",
            "https://i.nhentai.net/galleries/987560/109.jpg",
            "https://i.nhentai.net/galleries/987560/110.jpg",
            "https://i.nhentai.net/galleries/987560/111.jpg",
            "https://i.nhentai.net/galleries/987560/112.jpg",
            "https://i.nhentai.net/galleries/987560/113.jpg",
            "https://i.nhentai.net/galleries/987560/114.jpg",
            "https://i.nhentai.net/galleries/987560/115.jpg",
            "https://i.nhentai.net/galleries/987560/116.jpg",
            "https://i.nhentai.net/galleries/987560/117.jpg",
            "https://i.nhentai.net/galleries/987560/118.jpg",
            "https://i.nhentai.net/galleries/987560/119.jpg",
            "https://i.nhentai.net/galleries/987560/120.jpg",
            "https://i.nhentai.net/galleries/987560/121.jpg",
            "https://i.nhentai.net/galleries/987560/122.jpg",
            "https://i.nhentai.net/galleries/987560/123.jpg",
            "https://i.nhentai.net/galleries/987560/124.jpg",
            "https://i.nhentai.net/galleries/987560/125.jpg",
            "https://i.nhentai.net/galleries/987560/126.jpg",
            "https://i.nhentai.net/galleries/987560/127.jpg",
            "https://i.nhentai.net/galleries/987560/128.jpg",
            "https://i.nhentai.net/galleries/987560/129.jpg",
            "https://i.nhentai.net/galleries/987560/130.jpg",
            "https://i.nhentai.net/galleries/987560/131.jpg",
            "https://i.nhentai.net/galleries/987560/132.jpg",
            "https://i.nhentai.net/galleries/987560/133.jpg",
            "https://i.nhentai.net/galleries/987560/134.jpg",
            "https://i.nhentai.net/galleries/987560/135.jpg",
            "https://i.nhentai.net/galleries/987560/136.jpg",
            "https://i.nhentai.net/galleries/987560/137.jpg",
            "https://i.nhentai.net/galleries/987560/138.jpg",
            "https://i.nhentai.net/galleries/987560/139.jpg",
            "https://i.nhentai.net/galleries/987560/140.jpg",
            "https://i.nhentai.net/galleries/987560/141.jpg",
            "https://i.nhentai.net/galleries/987560/142.jpg",
            "https://i.nhentai.net/galleries/987560/143.jpg",
            "https://i.nhentai.net/galleries/987560/144.jpg",
            "https://i.nhentai.net/galleries/987560/145.jpg",
            "https://i.nhentai.net/galleries/987560/146.jpg",
            "https://i.nhentai.net/galleries/987560/147.jpg",
            "https://i.nhentai.net/galleries/987560/148.jpg",
            "https://i.nhentai.net/galleries/987560/149.jpg",
            "https://i.nhentai.net/galleries/987560/150.jpg",
            "https://i.nhentai.net/galleries/987560/151.jpg",
            "https://i.nhentai.net/galleries/987560/152.jpg",
            "https://i.nhentai.net/galleries/987560/153.jpg",
            "https://i.nhentai.net/galleries/987560/154.jpg",
            "https://i.nhentai.net/galleries/987560/155.jpg",
            "https://i.nhentai.net/galleries/987560/156.jpg",
            "https://i.nhentai.net/galleries/987560/157.jpg",
            "https://i.nhentai.net/galleries/987560/158.jpg",
            "https://i.nhentai.net/galleries/987560/159.jpg",
            "https://i.nhentai.net/galleries/987560/160.jpg",
            "https://i.nhentai.net/galleries/987560/161.jpg",
            "https://i.nhentai.net/galleries/987560/162.jpg",
            "https://i.nhentai.net/galleries/987560/163.jpg",
            "https://i.nhentai.net/galleries/987560/164.jpg",
            "https://i.nhentai.net/galleries/987560/165.jpg",
            "https://i.nhentai.net/galleries/987560/166.jpg",
            "https://i.nhentai.net/galleries/987560/167.jpg",
            "https://i.nhentai.net/galleries/987560/168.jpg",
            "https://i.nhentai.net/galleries/987560/169.jpg",
            "https://i.nhentai.net/galleries/987560/170.jpg",
            "https://i.nhentai.net/galleries/987560/171.jpg",
            "https://i.nhentai.net/galleries/987560/172.jpg",
            "https://i.nhentai.net/galleries/987560/173.jpg",
            "https://i.nhentai.net/galleries/987560/174.jpg",
            "https://i.nhentai.net/galleries/987560/175.jpg",
            "https://i.nhentai.net/galleries/987560/176.jpg",
            "https://i.nhentai.net/galleries/987560/177.jpg",
            "https://i.nhentai.net/galleries/987560/178.jpg",
            "https://i.nhentai.net/galleries/987560/179.jpg",
            "https://i.nhentai.net/galleries/987560/180.jpg",
            "https://i.nhentai.net/galleries/987560/181.jpg",
            "https://i.nhentai.net/galleries/987560/182.jpg",
            "https://i.nhentai.net/galleries/987560/183.jpg",
            "https://i.nhentai.net/galleries/987560/184.jpg",
            "https://i.nhentai.net/galleries/987560/185.jpg",
            "https://i.nhentai.net/galleries/987560/186.jpg",
            "https://i.nhentai.net/galleries/987560/187.jpg",
            "https://i.nhentai.net/galleries/987560/188.jpg",
            "https://i.nhentai.net/galleries/987560/189.jpg",
            "https://i.nhentai.net/galleries/987560/190.jpg",
            "https://i.nhentai.net/galleries/987560/191.jpg",
            "https://i.nhentai.net/galleries/987560/192.jpg",
            "https://i.nhentai.net/galleries/987560/193.jpg",
            "https://i.nhentai.net/galleries/987560/194.jpg",
            "https://i.nhentai.net/galleries/987560/195.jpg",
            "https://i.nhentai.net/galleries/987560/196.jpg",
            "https://i.nhentai.net/galleries/987560/197.jpg",
            "https://i.nhentai.net/galleries/987560/198.jpg",
            "https://i.nhentai.net/galleries/987560/199.jpg",
            "https://i.nhentai.net/galleries/987560/200.jpg",
            "https://i.nhentai.net/galleries/987560/201.jpg",
            "https://i.nhentai.net/galleries/987560/202.jpg",
            "https://i.nhentai.net/galleries/987560/203.jpg",
            "https://i.nhentai.net/galleries/987560/204.jpg",
            "https://i.nhentai.net/galleries/987560/205.jpg",
            "https://i.nhentai.net/galleries/987560/206.jpg",
            "https://i.nhentai.net/galleries/987560/207.jpg",
            "https://i.nhentai.net/galleries/987560/208.jpg",
            "https://i.nhentai.net/galleries/987560/209.jpg",
            "https://i.nhentai.net/galleries/987560/210.jpg",
            "https://i.nhentai.net/galleries/987560/211.jpg",
            "https://i.nhentai.net/galleries/987560/212.jpg",
            "https://i.nhentai.net/galleries/987560/213.jpg",
            "https://i.nhentai.net/galleries/987560/214.jpg",
            "https://i.nhentai.net/galleries/987560/215.jpg",
            "https://i.nhentai.net/galleries/987560/216.jpg",
            "https://i.nhentai.net/galleries/987560/217.jpg",
            "https://i.nhentai.net/galleries/987560/218.jpg",
            "https://i.nhentai.net/galleries/987560/219.jpg",
            "https://i.nhentai.net/galleries/987560/220.jpg",
            "https://i.nhentai.net/galleries/987560/221.jpg",
            "https://i.nhentai.net/galleries/987560/222.jpg",
            "https://i.nhentai.net/galleries/987560/223.jpg",
            "https://i.nhentai.net/galleries/987560/224.jpg",
            "https://i.nhentai.net/galleries/987560/225.jpg"
        ],
        "language": "english",
        "num_favorites": 97746,
        "num_pages": 225,
        "optional_title": {
            "english": "[ShindoLA] METAMORPHOSIS (Complete) [English]",
            "japanese": "",
            "pretty": "METAMORPHOSIS"
        },
        "parodies": null,
        "tags": [
            "shindol",
            "piercing",
            "pregnant",
            "mmf threesome",
            "vomit",
            "group",
            "story arc",
            "schoolgirl uniform",
            "snuff",
            "english",
            "prostitution",
            "nakadashi",
            "moral degeneration",
            "ahegao",
            "anal",
            "translated",
            "dark skin",
            "x-ray",
            "full body tattoo",
            "drugs",
            "incest",
            "double penetration",
            "stockings",
            "gyaru",
            "mind break",
            "blackmail",
            "impregnation",
            "blowjob",
            "deepthroat",
            "manga",
            "already uploaded"
        ],
        "title": "METAMORPHOSIS",
        "total": 225,
        "upload_date": "October 18, 2016 (6 years ago)"
    },
    "source": "https://nhentai.net/g/177013"
}
```

Otherwise `search` will return 25 **List Object** of search results.
```js
{
    "data": [
        {
            "cover": "https://i.nhentai.net/galleries/2244825/1.jpg",
            "id": 406651,
            "language": "english",
            "tags": [
                "oni",
                "big breasts",
                "big ass",
                "cheating",
                "english",
                "anal",
                "shemale",
                "translated",
                "yaoi",
                "muscle",
                "doujinshi",
                "dickgirl on male",
                "male on dickgirl",
                "focus anal",
                "huuten",
                "anal intercourse"
            ],
            "title": {
                "english": "[huuten (Huuten)] ♂×♂ - Demon Shemale Wife (English)",
                "japanese": "[huuten (瘋)] ♂×♂ - 鬼シーメール人妻",
                "pretty": "♂×♂ - Demon Shemale Wife"
            },
            "total": 23,
            "upload_date": "June 12, 2022 (1 day ago)"
        },
        {
            "cover": "https://i.nhentai.net/galleries/1893566/1.jpg",
            "id": 356040,
            "language": "english",
            "tags": [
                "ttf threesome",
                "futanari",
                "unusual teeth",
                "sweating",
                "big breasts",
                "unusual pupils",
                "cunnilingus",
                "group",
                "english",
                "ahegao",
                "anal",
                "hairy",
                "translated",
                "thigh high boots",
                "multi-work series",
                "double penetration",
                "tall girl",
                "blowjob",
                "stomach deformation",
                "doujinshi",
                "dickgirl on dickgirl",
                "original",
                "huuten"
            ],
            "title": {
                "english": "[huuten (Huuten)] Defeated by Futanarification Medication (Latter Part)| Drugged to Futanaridom Part 2 [English]",
                "japanese": "[huuten (瘋)] 薬を打たれふたなり化(後編)[英訳]",
                "pretty": "Defeated by Futanarification Medication| Drugged to Futanaridom Part 2"
            },
            "total": 43,
            "upload_date": "April 21, 2021 (1 year ago)"
        }
    ],
    "page": 1,
    "sort": "popular-today",
    "source": "https://nhentai.net/api/galleries/search?query=futa&sort=popular-today&page=1"
}
```

## Unresolved JSON
Instead arbitrary object, This library designed to be neat and clean returns, although it must be reparsed to the string first, that's why [`janda.resolve()`](https://sinkaroid.github.io/janda/utils/parser.html#janda.utils.parser.resolve) exist.  

Let's see an example:

```py
import asyncio
from janda import Nhentai, resolve

async def main():
    nh = Nhentai()
    data = await nh.get(274003)
    print(data) ## unresolve
    print(resolve(data)) ## resolved

asyncio.run(main())
```
- Unresolve: meant is better and neat dictionaries returns instead arbitrary JSON structure
- Resolved: bad structure, arbitary indent, unsorting but it is resolved and ready to extends works with JSON

## Known Issues
#### `UnicodeEncodeError: 'charmap' codec can't encode characters`  
- It's raised when the title contains non-ascii characters, then your console can't parse them, use real console don't Git-bash.

## Legal
This tool can be freely copied, modified, altered, distributed without any attribution whatsoever. However, if you feel
like this tool deserves an attribution, mention it. It won't hurt anybody

## Pronunciation
[`id_ID`](https://www.localeplanet.com/java/id-ID/index.html) • **/jan·da/** — gatel, nakal, dan menggoda; _(?)_ seperti siapa? adalah benar si janda gemer tomoe

## EoF
All books from those doujinboards are definitely ilegal from original authors.