# -*- coding: utf-8 -*-
import os
import spiderlxml as lxml
import spidercomm as common

# set up             
url_root = 'http://www.jianshu.com/'
url_seed = 'http://www.jianshu.com/p/e0bd6bfad10b?page=%d'
spider_path='spider_res/lxml/'
if os.path.exists(spider_path) == False:
    os.mkdir(spider_path)
    
# get total number of pages
print lxml.isMultiPaged(url_seed)
page_count = lxml.getNumberOfPages(url_seed)

# get all urls to be crawled
to_be_crawled_urls=set()
for count in range(page_count+1):
    links = lxml.crawled_links(url_seed % count,url_root)#,{'class':'title'})
    links.add(url_seed % count)
    print "All links: %s" % links 
    to_be_crawled_urls= to_be_crawled_urls | links
print "Total number of all links is %d" % len(to_be_crawled_urls)

# capture desired contents from crawled_urls
if len(to_be_crawled_urls) >= 1:
    with open(spider_path+"_all_links.txt",'w+') as file:
        for link in to_be_crawled_urls:
            if('javascript:' not in link):
                file.write(unicode(link).encode('utf-8',errors='ignore')+"\n")
                title,content=lxml.crawled_page(link) 
                print "title is %s" % title                
                file_name = spider_path + title +'.txt'
                common.writePage(file_name,content)

