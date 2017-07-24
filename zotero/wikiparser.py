#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 14 10:37:35 2017

@author: wanjia
"""
import os
from urllib import urlopen
try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup
    
class WikiParser(object):
    term = "Blinded_experiment"
    url="https://en.wikipedia.org/wiki/"+term
    req = urlopen(url)#.readlines()
    filename=os.getcwd()+"/urlcontent.html"
    
    content= req.read()
    
    def getAbstractNote(self,filename):
        abstract_note=""
        with open(filename, 'rw+') as f:
            soup = BeautifulSoup(f.read()).body.find('div', attrs={'class':'mw-parser-output'})
            if (soup<>None):
                for tag in soup.children:
                    if (tag.name == "div"):
                        break
                    elif (tag.name <> None):
                        abstract_note = abstract_note + tag.text
                return abstract_note
            else:
                return "Not Found Abstracts"
            
    def getFooterUrl(self,filename):
        with open(filename, 'r') as f:
            
            soup = BeautifulSoup(f.read()).body.find('div',attrs={'class':'printfooter'})
            return soup.a.text
            