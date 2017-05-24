# -*- coding: utf-8 -*-

class QuickUnion(object):
    id=[]
    count=0
    
    def __init__(self,n):
        self.count = n
        i=0
        while i<n:
            self.id.append(i)
            i+=1

    def connected(self,p,q):
        if self.find(p) == self.find(q):
            return True
        else:            
            return False
    
    def find(self,p):   
        while (p != self.id[p]):
            p = self.id[p]
        return p
    
    def union(self,p,q):
        idq = self.find(q)
        idp = self.find(p)
        if not self.connected(p,q):
            self.id[idp]=idq
            self.count -=1
             
                               