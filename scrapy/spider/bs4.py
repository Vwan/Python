# -*- coding: utf-8 -*-
import os
import time
import urllib2
import urlparse
from bs4 import BeautifulSoup
from os.path import exists

def download(url,retry=2):
    print "downloading %s" % url
    header = {
            'User-Agent':'Mozilla/5.0'
            }
    try:
        req = urllib2.Request(url,headers=header)
        html = urllib2.urlopen(req).read()
    except urllib2.HTTPError as e:
            print "download error: %s" % e.reason
            html = None
            if retry >0:
                print e.code
                if hasattr(e,'code') and 500 <= e.code < 600:
                    print e.code
                    return download(url,retry-1)
                    time.sleep(1)
    return html

def crawled_links(url_seed,url_root,attrs={}):
    crawled_links=set()
    html = download(url_seed)
    soup = BeautifulSoup(html,'html.parser')
    links= soup.find_all('a',attrs)
    if len(links)==0:
        return crawled_links
    for link in links:
        link = link.get('href')
        if link not in crawled_links:
            realUrl = urlparse.urljoin(url_root,link)
            crawled_links.add(realUrl)
    return crawled_links

def crawled_page(crawled_url):
        html = download(crawled_url)
        soup = BeautifulSoup(html,'html.parser')
        title = soup.find('h1',{'class':'title'})
        if title== None:
            return "Title_Is_None",crawled_url
        content = soup.find('div',{'class':'show-content'})
        if content == None:
            return title.text, "Content_Is_None"
        return title.text,content.text

def isMultiPaged(url):    
    html_page1 = download(url % 1)
    soup = BeautifulSoup(html_page1,'html.parser')
    body1 = soup.find('body')   
    body1.script.decompose()
       
    html_page2 = download(url_seed % 2)
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
            url= url_seed % count
            print "url: %s" % url
            count += 1
            html = download(url)
            if html==None:
                break        
    return count

def writePage(filename,content):
    content = unicode(content).encode('utf-8',errors='ignore')+"\n"
    print "-----"+filename
    print 'Title_Is_None.txt' in filename
    if ('Title_Is_None.txt' in filename):
        with open(filename,'a') as file:
            file.write(content)
    else:
        with open(file_name,'wb+') as file:
            file.write(content)

# set up             
url_root = 'http://www.jianshu.com/'
url_seed = 'http://www.jianshu.com/p/e0bd6bfad10b?page=%d'
spider_path='c:/temp/spider_res/'
if os.path.exists(spider_path) == False:
    os.mkdir(spider_path)
    
# get total number of pages
print isMultiPaged(url_seed)
page_count = getNumberOfPages(url_seed)

# get all urls to be crawled
to_be_crawled_urls=set()
for count in range(page_count+1):
    links = crawled_links(url_seed % count,url_root)#,{'class':'title'})
    links.add(url_seed % count)
    print "All links: %s" % links 
    to_be_crawled_urls= to_be_crawled_urls | links
print "len is %d" % len(to_be_crawled_urls)

# capture pages from crawled_urls
if len(to_be_crawled_urls) >= 1:
    with open(spider_path+"_all_links.txt",'w+') as file:
        for link in to_be_crawled_urls:
            if('javascript:' not in link):
                file.write(unicode(link).encode('utf-8',errors='ignore')+"\n")
                title,content=crawled_page(link) 
                print "title is %s" % title                
                file_name = spider_path + title +'.txt'
                writePage(file_name,content)

