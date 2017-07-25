# -*- coding: utf-8 -*-
import spidercomm as common
import lxml
import urlparse
from lxml import etree
from StringIO import StringIO

def crawled_links(url_seed,url_root,attrs={}):
    crawled_links=set()
    html = common.download(url_seed)
    tree = etree.HTML(html)
    links= tree.xpath("//a")
    if len(links)==0:
        return crawled_links
    for link in links:
        link = link.get('href')
        if link not in crawled_links:
            realUrl = urlparse.urljoin(url_root,link)
            crawled_links.add(realUrl)
    return crawled_links

def crawled_page(crawled_url):
        html = common.download(crawled_url)
        tree = etree.HTML(html)
        title= tree.xpath("/html/body/div[1]/div[1]/div[1]/h1")
        if title == None or len(title) == 0:
            return "Title_Is_None",crawled_url
        content = tree.xpath("/html/body/div[1]/div[1]/div[1]/div[2]")
        if content == None or len(content) ==0:
            return title[0].text, "Content_Is_None"
        print "\n".join(x.text for x in content)
        return title[0].text,"\n".join(x.text for x in content)

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

