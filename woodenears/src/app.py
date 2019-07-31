'''
Created on Jul 29, 2019
# -*- coding: utf-8 -*-  
@author: tfu
'''

import requests
from bs4 import BeautifulSoup
from werkzeug import urls
import os
import re
from indextool.indexhtml import getHtml,getHtml,getHtmlUrl,getjumplink
from subpagetool.subpagehtml import getReportName,savePics

url='https://www.woodenears.com/list?category=5b6171cf823aea488f19e1d0&name=%E8%80%B3%E6%9C%BA%E6%B5%8B%E9%87%8F%E6%8A%A5%E5%91%8A'
baseJumpRoot='https://www.woodenears.com'





                
'''                   
html=getHtml('https://www.woodenears.com/article/5bed14bbbcd7ab780aff6e0e')                
name=getReportName(html)
print(name)

pageRange=getPageRange(url)
indexList=getHtmlUrl(url,pageRange)
pageList = getjumplink(baseJumpRoot,indexList)
print(pageList)                
                
                
                
'''            
pagelist=['https://www.woodenears.com/article/5bed14bbbcd7ab780aff6e0e']
savePics(pagelist)






