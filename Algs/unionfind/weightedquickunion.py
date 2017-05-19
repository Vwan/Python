# -*- coding: utf-8 -*-

class WeightedQuickUnion(object):
    root=[]
    count=0
    sz=[]
    
    def __init__(self,n):
        self.count = n
        i=0
        while i<n:
            self.root.append(i)
            self.sz.append(i)
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
        rootp = self.find(p)
        print "root of %d is: %d" % (p,rootp)
        rootq = self.find(q)
        print "root of %d is: %d" % (q,rootq)
        if not self.isConnected(p,q):            
            print "Before Connected: tree size of %d's root is: %d" % (p,self.sz[rootp])
            print "Before Connected: tree size of %d's root is: %d" % (q,self.sz[rootq])
            if (self.sz[rootp] < self.sz[rootq]):
                print "tree size of %d's root is smaller than %d's root" %(p,q)
                print "root of %d's root %d is set to %d" % (p,rootp,rootq)
                self.root[rootp] = rootq
                print "tree size of %d's root is incremented by tree size of %d's root" %(q,p)
                self.sz[rootq] += self.sz[rootp]    
                print "After Connected: tree size of %d's root is: %d" % (p,self.sz[rootp])
                print "After Connected: tree size of %d's root is: %d" % (q,self.sz[rootq])         
            else:                  
                print "tree size of %d's root is larger than or equal with %d's root" %(p,q)
                print "root of %d's root %d is set to %d" % (q,rootq,rootp)
                self.root[rootq] = rootp
                print "tree size of %d's root is incremented by tree size of %d's root" %(p,q)
                self.sz[rootp] += self.sz[rootq]   
                print "After Connected: tree size of %d's root is: %d" % (p,self.sz[rootp])
                print "After Connected: tree size of %d's root is: %d" % (q,self.sz[rootq])         
            