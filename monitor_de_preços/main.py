import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0"
}
link = ""


response = requests.get(link, headers=headers)

site = BeautifulSoup(response.text, 'html.parser')

pesquisa = site.find('span')

print(pesquisa)
