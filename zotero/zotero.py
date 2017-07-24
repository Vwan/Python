#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 08:32:18 2017

@author: wanjia
"""

from libZotero import zotero
from urllib import urlopen
import datetime
from handler import Handler
import os
from wikiparser import WikiParser
import hashlib

#https://api.zotero.org/users/3949286/items?page=3&key=yrQKEJNQsAKekW9GOgGVzCBG
# 

handler = Handler()
wikiparser = WikiParser()
zlib = zotero.Library('user','3949286','<null>','yrQKEJNQsAKekW9GOgGVzCBG')
print zlib

# retrieve the first five top-level items.
#items = zlib.fetchItemsTop({'limit': 6, 'content': 'json,bib,coins'}) 
#for item in items:
   # print 'Item Type: %s | Key: %s | Title: %s ' % (item.itemType,item.itemKey, item.title) 
    


term = "Blinded_experiment"
url="https://en.wikipedia.org/wiki/"+term
req = urlopen(url)#.readlines()
filename = os.getcwd()+"/urlcontent.html"
file=open(filename,"w")
file.write(req.read())

item_type='encyclopediaArticle'
item_title=term
abstract_note= wikiparser.getAbstractNote(filename)
#create a new item of type document
newItem = zotero.getTemplateItem(item_type)
#sets the title of the item to Python Lesson Document
newItem.set('title', term)
newItem.set('encyclopediaTitle', term)
#adds a new abstract note
newItem.set('abstractNote', abstract_note)
#sets date to current date
now = datetime.datetime.today().strftime("%Y-%m-%dT%H:%m:%s")
newItem.set('date', now)
newItem.set('accessDate',now)
newItem.set('edition',now)
#sets url
url=wikiparser.getFooterUrl(filename)
print "url is: %s" % url
pageVersionID = url.split("=")[-1]
print pageVersionID
newItem.set('url',url)
newItem.set('language','en')
newItem.set('libraryCatalog','Wikipedia')
newItem.set('rights','Creative Commons Attribution-ShareAlike License')
newItem.set('extra','Page Version ID: '+pageVersionID)
# make the request to the API to create the item
# a Zotero Item object will be returned
# if the creation went okay it will have a writeFailure property set to False
#attach snapthost

filestat = os.stat(filename)
nf = open(filename, 'rb')
nfdata = nf.read()
m = hashlib.md5()
m.update(nfdata)
digest = m.hexdigest()
attachmentinfo = {#'md5': digest,
         'title':"index.html",
         'url': url
        # 'filesize': filestat.st_size,
        # 'mtime': filestat.st_mtime  # the zotero api accepts mtime in ms, os.stat may return seconds depending on operating system
         }
#create item
createdItem = zlib.createItem(newItem)
createdItem = zlib.createAttachmentItem(createdItem,attachmentinfo)
if createdItem.writeFailure != False:
   print(createdItem.writeFailure['code'])
   print(createdItem.writeFailure['message'])
handler.addTag(zlib,createdItem,term)