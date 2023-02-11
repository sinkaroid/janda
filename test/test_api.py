import requests
from janda.utils.client import list_api

for api in list_api():
    r = requests.get(api)
    print(api, r.status_code)
    