# -*- coding: utf-8 -*-
import os
import spiderlxml as lxml
import spidercomm as common

# set up             
url_root = 'http://www.jianshu.com/'
url_seed = 'http://www.jianshu.com/p/e0bd6bfad10b?page=%d'
spider_path='spider_res/lxml/'
if os.path.exists(spider_path) == False:
    os.makedirs(spider_path)
    
# get total number of pages
print "url %s has multiple pages? %r" % (url_seed,lxml.isMultiPaged(url_seed))
page_count = lxml.getNumberOfPages(url_seed)
print "page_count is %s" % page_count

# get all links to be crawled and write to file    
links_to_be_crawled=set()
for count in range(page_count):
    links = common.to_be_crawled_links(lxml.a_links(url_seed % count),count,url_root,url_seed)
    print "Total number of all links is %d" % len(links)
    links_to_be_crawled = links_to_be_crawled | links
with open(spider_path+"_all_links.txt",'w+') as file:
    file.write("\n".join(unicode(link).encode('utf-8',errors='ignore') for link in links_to_be_crawled))

# capture desired contents from crawled_urls
print "count of links to be crawled is: %d" % len(links_to_be_crawled)
if len(links_to_be_crawled) >= 1:
    for link in links_to_be_crawled:           
      title,content=lxml.crawled_page(link) 
      print "content is %s" % content                
      file_name = spider_path + title +'.txt'
      common.writePage(file_name,content)

