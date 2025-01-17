


import requests
from pprint import pp, pprint
import json

BASE_UL = "https://icanhazdadjoke.com/"
API_PAGE = ""

URL = BASE_UL + API_PAGE

headers_dict = {
    "Accept" : "text/plain"
}


response = requests.get(URL, headers=headers_dict)
print(type(response.text))

## r - read
## - write
## - append

with open("jokes.txt", "a") as file_handler:
    file_handler.write(response.text)
    file_handler.write("\n")