'''
Created on Jul 29, 2019

@author: tfu
'''
import requests
from bs4 import BeautifulSoup
from werkzeug import urls
import os

url='https://www.woodenears.com/list?category=5b6171cf823aea488f19e1d0&name=%E8%80%B3%E6%9C%BA%E6%B5%8B%E9%87%8F%E6%8A%A5%E5%91%8A&pageIndex=1'
jumproot='https://www.woodenears.com/article/'

def getHtmlUrl(url):
    r= requests.get(url)
    r.raise_for_status()
    r.encoding= r.apparent_encoding
    return r.text

def getjumplink(jumproot,html):
    soup=BeautifulSoup(html,"html.parser")
    boxes=soup.find('div',id="listContent").find_all('a')
    for box in boxes:
        print(box['href'])

    
html=getHtmlUrl(url)
getjumplink(jumproot,html)