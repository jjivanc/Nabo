import requests
from bs4 import BeautifulSoup

#from selenium import webdriver
url = 'https://mangayabu.top/'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0'}
soup = BeautifulSoup(requests.get(url,cookies={'__hs_opt_out': 'no'},  headers=headers).content, 'html.parser')

pageFind = soup.find_all(class_='card')

print(pageFind)

#page = requests.get("https://superhentais.com/")
#page = requests.get("https://mangayabu.top/").content



#soup = BeautifulSoup(page, 'html.parser')

#grid_box = soup.find_all('div', class_='grid_image')

#T = soup.find_all('a', itemprop="url",limit=12)
#T = soup.find_all('h2',class_='grid_title',itemprop='name',limit=6)
#pageFind = soup.find_all('div')
#for link in soup.find_all('a'):
#    print(link.get('href'))

#def link_s():
#  teste = []
#  for link in T:
#   teste.append(link.a.get(''))
#  return teste
#print(link_s())
#print(pageFind)
