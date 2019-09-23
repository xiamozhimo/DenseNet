'''
Created on Jul 29, 2019
# -*- coding: utf-8 -*-  
@author: tfu
'''

from indextool.indexhtml import getHtmlUrl,getjumplink
from filesystem.folderManage import savePics


url='https://www.woodenears.com/list?category=5b6171cf823aea488f19e1d0&name=%E8%80%B3%E6%9C%BA%E6%B5%8B%E9%87%8F%E6%8A%A5%E5%91%8A'
baseJumpRoot='https://www.woodenears.com'
root='D:/wormgetpic/'

def main():
    indexlist=getHtmlUrl(url)
    pageList=getjumplink(baseJumpRoot,indexlist)
    savePics(pageList,root)
# savePics(pageList,root,contidueMode=0,startPoint=0,endPoint=9999):
# To activate continue mode, change the value to 1 and input a start point.

main()
                






