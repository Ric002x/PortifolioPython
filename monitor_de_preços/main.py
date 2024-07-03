import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 OPR/109.0.0.0"
}
link = "https://www.amazon.com.br/dp/B07DTNB6SY?aref=mGTLdvJoGs&aaxitk=f1e1ef300eafad50b1896a34ab997059&language=pt_BR&pd_rd_plhdr=t&smid=A1ZZFT5FULY4LN&ref=dacx_dp_590273137287179661_583568053879526436"


response = requests.get(link, headers=headers)

site = BeautifulSoup(response.text, 'html.parser')

pesquisa = site.find('span')

print(pesquisa)
