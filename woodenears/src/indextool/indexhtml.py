import requests
from bs4 import BeautifulSoup



def getHtml(url):
    r= requests.get(url)
    r.raise_for_status()
    r.encoding= r.apparent_encoding
    return r.text

def getPageRange(url):    
    pageRange=[]    
    html=getHtml(url)
    soup=BeautifulSoup(html,"html.parser")
    numbers = soup.find('ul',class_="el-pager").find_all('li')
    for number in numbers:
        pageRange.append(number.text)
    return pageRange

def getHtmlUrl(url):
    indexList=[]
    pageRange=getPageRange(url)
    for i in pageRange:
        urljump=url+'&pageIndex='+i
        indexList.append(getHtml(urljump))
    return indexList

def getjumplink(baseJumpRoot,indexList):
    pageList=[]
    for html in indexList:
        soup=BeautifulSoup(html,"html.parser")
        links=soup.find('div',id="listContent").find_all('a')
        for link in links:
            pageList.append(baseJumpRoot+link['href'])
    return pageList