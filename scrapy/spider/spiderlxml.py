# -*- coding: utf-8 -*-
import spidercomm as common
import urlparse
from lxml import etree

# get all tags a from a single url
def a_links(url_seed,attrs={}):
    html = common.download(url_seed)
    tree = etree.HTML(html)
    alinks= tree.xpath("//a")
    return alinks

def crawled_page(crawled_url):
        html = common.download(crawled_url)
        tree = etree.HTML(html)
        title= tree.xpath("/html/body/div[1]/div[1]/div[1]/h1")
        if title == None or len(title) == 0:
            return "Title_Is_None",crawled_url
        contents = tree.xpath("/html/body/div[1]/div[1]/div[1]/div[2]/*")
        if contents == None or len(contents) ==0:
            return title.text, "Content_Is_None"
        content = ''
        for x in contents:
            if (x.text != None):
                content = content + x.xpath('string()')
        return title[0].text,content

def isMultiPaged(url):    
    html_page1 = common.download(url % 1)
    tree = etree.HTML(html_page1)    
    xp1 = tree.xpath("/html/body/div[1]/div[1]/div[1]/div[2]/*")
    xp1 = ",".join(x.text for x in xp1)
    html_page2 = common.download(url % 2)
    if html_page2 == None:
        return False
    tree = etree.HTML(html_page2)    
    xp2 = tree.xpath("/html/body/div[1]/div[1]/div[1]/div[2]/*")
    xp2 = ",".join(x.text for x in xp2)
    if xp1 == xp2:
        return False
    else:
        return True

def getNumberOfPages(url):
    count = 1
    flag = True
    if (isMultiPaged(url)):
        while flag:
            url= url % count
            print "url: %s" % url
            count += 1
            html = common.download(url)
            if html==None:
                break        
    return count

