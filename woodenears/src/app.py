'''
Created on Jul 29, 2019

@author: tfu
'''
import requests
from bs4 import BeautifulSoup
from werkzeug import urls
import os

url='https://www.woodenears.com/list?category=5b6171cf823aea488f19e1d0&name=%E8%80%B3%E6%9C%BA%E6%B5%8B%E9%87%8F%E6%8A%A5%E5%91%8A'
baseJumpRoot='https://www.woodenears.com'

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

def getHtmlUrl(url,pageRange):
    indexList=[]
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



def savePics(pageList):
    for pagelink in pageList:
        html=getHtml(pagelink)
        soup=BeautifulSoup(html,"html.parser")
        all_img=soup.find('div',class_='content-container').find_all('img')    
        for img in all_img:
            src=img['src']
            print(src)
            root='D:/wormgetpic/'
            path=root + src.split('/')[-1]+'.jpg'
            try:
                if not os.path.exists(root):
                    os.mkdir(root)
                if not os.path.exists(path):
                    r= requests.get(src)
                    with open(path,'wb') as f:
                        f.write(r.content)
                    print('Success')   
                else:
                    print('Already Exist')       
            except Exception as e:
                print(e)
            
pagelist=['https://www.woodenears.com/article/5bed14bbbcd7ab780aff6e0e']
savePics(pagelist)

'''
pageRange=getPageRange(url)
indexList=getHtmlUrl(url,pageRange)
pageList = getjumplink(baseJumpRoot,indexList)
print(pageList)
'''   


