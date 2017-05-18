# -*- coding: utf-8 -*-

class QuickUnion(object):
    root=[]
    count=0
    
    def __init__(self,n):
        self.count = n
        i=0
        while i<n:
            self.root.append(i)
            i+=1

    def isConnected(self,p,q):
        if self.find(p) == self.find(q):
            return True
        else:            
            return False
    
    def find(self,p):   
        while (p != self.root[p]):
            p = self.root[p]
        return p
    
    def union(self,p,q):
        rootq = self.find(q)
        rootp = self.find(p)
        if not self.isConnected(p,q):
            self.root[rootp]=rootq
             
                               