#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 08:32:18 2017

@author: wanjia
"""

from libZotero import zotero
import urllib2
import datetime
from handler import Handler

#https://api.zotero.org/users/3949286/items?page=3&key=yrQKEJNQsAKekW9GOgGVzCBG
# 

handler = Handler()
zlib = zotero.Library('user','3949286','<null>','yrQKEJNQsAKekW9GOgGVzCBG')
print zlib

# retrieve the first five top-level items.
items = zlib.fetchItemsTop({'limit': 6, 'content': 'json,bib,coins'}) 
#for item in items:
   # print 'Item Type: %s | Key: %s | Title: %s ' % (item.itemType,item.itemKey, item.title) 
    
    #create a new item of type document
newItem = zotero.getTemplateItem('encyclopediaArticle')

#sets the title of the item to Python Lesson Document
newItem.set('title', 'Python Lesson Document')
#adds a new abstract note
newItem.set('abstractNote', 'Created using a zotero python library and the write api')

#sets date to current date
now = datetime.datetime.today().strftime("%Y-%m-%d")
newItem.set('date', now)
# make the request to the API to create the item
# a Zotero Item object will be returned
# if the creation went okay it will have a writeFailure property set to False
createdItem = zlib.createItem(newItem) 
if createdItem.writeFailure != False:
   print(createdItem.writeFailure['code'])
   print(createdItem.writeFailure['message'])
handler.addTag(zlib,createdItem,"Python Lesson")

url="https://en.wikipedia.org/wiki/Test"
req = urllib2.Request(url)
print req.data