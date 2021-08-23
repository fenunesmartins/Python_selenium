import requests
from bs4 import BeautifulSoup

url = 'https://chavantes.sp.gov.br/legislacao/decretos'

request = requests.get(url).content
soup = BeautifulSoup(request,'html.parser')
links = soup.find_all('a')

for link in links:
    print(link['href'])