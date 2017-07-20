#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 15:12:45 2017

@author: wanjia
"""

from HTMLParser import HTMLParser

class WikiParser(HTMLParser):
    tag=""
    mdstr=""
    def handle_starttag(self, tag, attrs):        
        self.tag = tag
        self.attrs = attrs
        #print "Encountered a start tag:", tag            
            
    def handle_data(self,data):
        if self.tag == 'h1':
            self.mdstr = self.mdstr + "# "+ data + "\n"
        if self.tag == 'h2':
            self.mdstr = self.mdstr +"## "+data + "\n"
            
        if self.tag == 'h3':
            self.mdstr = self.mdstr +"### "+data + "\n"
        
        if self.tag == 'li':
            self.mdstr = self.mdstr + "- " + data + "\n"
        
        if self.tag == 'p':
            print "blockquote:" + data

def parse(htmlstr):
    parser = WikiParser()
    parser.feed(htmlstr)
    parser.close()
    
    
if __name__=='__main__':   

    filename="https://en.wikipedia.org/wiki/Test"
    htmlstr = open(filename,'r').read()
    parse(htmlstr)
    