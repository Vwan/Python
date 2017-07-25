# -*- coding: utf-8 -*-
import urllib2
import time
import urlparse

def download(url,retry=2):
   # print "downloading %s" % url
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

def writePage(filename,content):
    content = unicode(content).encode('utf-8',errors='ignore')+"\n"
    if ('Title_Is_None.txt' in filename):
        with open(filename,'a') as file:
            file.write(content)
    else:
        with open(filename,'wb+') as file:
            file.write(content)

# get urls to be crawled
#:param alinks: list of tag 'a' href, dependent on implementation eg. bs4,lxml
def to_be_crawled_link(alinks,url_seed,url_root):
    links_to_be_crawled=set()
    if len(alinks)==0:
        return links_to_be_crawled
    print "len of alinks is %d" % len(alinks)
    for link in alinks:
        link = link.get('href')            
        if link != None and 'javascript:' not in link:
            if link not in links_to_be_crawled:
                realUrl = urlparse.urljoin(url_root,link)
                links_to_be_crawled.add(realUrl)
    return links_to_be_crawled

def to_be_crawled_links(alinks,count,url_root,url_seed):
    url = url_seed % count
    links = to_be_crawled_link(alinks,url_root,url)#,{'class':'title'})
    links.add(url)
    return links