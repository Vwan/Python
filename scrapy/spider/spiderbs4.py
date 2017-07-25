# -*- coding: utf-8 -*-
import spidercomm as common
from bs4 import BeautifulSoup

# get all tags a from a single url
def a_links(url_seed,attrs={}):
    html = common.download(url_seed)
    soup = BeautifulSoup(html,'html.parser')
    alinks= soup.find_all('a',attrs)
    return alinks

def crawled_page(crawled_url):
        html = common.download(crawled_url)
        soup = BeautifulSoup(html,'html.parser')
        title = soup.find('h1',{'class':'title'})
        if title== None:
            return "Title_Is_None",crawled_url
        content = soup.find('div',{'class':'show-content'})
        if content == None:
            return title.text, "Content_Is_None"
        return title.text,content.text

def isMultiPaged(url):    
    html_page1 = common.download(url % 1)
    soup = BeautifulSoup(html_page1,'html.parser')
    body1 = soup.find('body')   
    body1.script.decompose()
       
    html_page2 = common.download(url % 2)
    if html_page2 == None:
        return False
    soup = BeautifulSoup(html_page2,"html.parser")
    body2 = soup.find('body')
    #print [x.extract() for x in body2.findAll('script') ]
    body2.script.decompose()
    if str(body1) == str(body2):
        return False
    else:
        return True

def getNumberOfPages(url):
    count = 1
    flag = True
    if (isMultiPaged(url)):
        while flag:
            url= url % count
            # print "url: %s" % url
            count += 1
            html = common.download(url)
            if html==None:
                break        
    return count

