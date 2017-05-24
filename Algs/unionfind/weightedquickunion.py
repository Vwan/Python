# -*- coding: utf-8 -*-

class WeightedQuickUnion(object):
    id=[]
    count=0
    sz=[]
    
    def __init__(self,n):
        self.count = n
        i=0
        while i<n:
            self.id.append(i)
            self.sz.append(1) # inital size of each tree is 1
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
        idp = self.find(p)
        print "id of %d is: %d" % (p,idp)
        idq = self.find(q)
        print "id of %d is: %d" % (q,idq)
        if not self.connected(p,q):            
            print "Before Connected: tree size of %d's id is: %d" % (p,self.sz[idp])
            print "Before Connected: tree size of %d's id is: %d" % (q,self.sz[idq])
            if (self.sz[idp] < self.sz[idq]):
                print "tree size of %d's id is smaller than %d's id" %(p,q)
                print "id of %d's id (%d) is set to %d" % (p,idp,idq)
                self.id[idp] = idq
                         
                print "tree size of %d's id is incremented by tree size of %d's id" %(q,p)
                self.sz[idq] += self.sz[idp]    
                print "After Connected: tree size of %d's id is: %d" % (p,self.sz[idp])
                print "After Connected: tree size of %d's id is: %d" % (q,self.sz[idq])         
            else:                  
                print "tree size of %d's id is larger than or equal with %d's id" %(p,q)
                print "id of %d's id (%d) is set to %d" % (q,idq,idp)
                self.id[idq] = idp
                print "tree size of %d's id is incremented by tree size of %d's id" %(p,q)
                self.sz[idp] += self.sz[idq]   
                print "After Connected: tree size of %d's id is: %d" % (p,self.sz[idp])
                print "After Connected: tree size of %d's id is: %d" % (q,self.sz[idq])         
        
            self.count -=1    