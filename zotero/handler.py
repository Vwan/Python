#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 10:06:13 2017

@author: wanjia
"""
class Handler(object):
    def addTag(self,zlib,item,tagname):
        #adds a new tag to the new item
       # tagname = 'python lesson'
        
        #in the bracket (tagname, '<tag type:0>')
        item.addTag(tagname, '0')
        #updates the item with the new tag
        updatedItem = zlib.writeUpdatedItem(item)
        if updatedItem.writeFailure != False:
           print("Error updating item")
           print(updatedItem.writeFailure['code'])
           print(updatedItem.writeFailure['message'])