# -*- coding: utf-8 -*-

class QuickFind(object):
    id=[]
    count=0
    
    def __init__(self,n):
        self.count = n
        i=0
        while i<n:
            self.id.append(i)
            i+=1
            
    def isConnected(self,p,q):
        return self.find(p) == self.find(q)
    
    def find(self,p):    
        return self.id[p]
    
    def union(self,p,q):
        idp = self.find(p)
        if not self.isConnected(p,q):
            for i in range(self.count):
                if self.id[i]==idp:
                    self.id[i] = self.id[q]
                                