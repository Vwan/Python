# -*- coding: utf-8 -*-

class SelectionSort(object):
    items=[]
    def __init__(self,items):
        self.items = items
        
    def sort(self):
        print "iten len: %d" % len(self.items)
        for i in range(len(self.items)-1,0,-1):
            maximum = i
            #print "-" * 10 
            #print "i: %d, item[%d]: %d" % (i,i,self.items[i])
            for j in range(0,i):
                #print "item[%d]: %d" % (j,self.items[j])                    
                if (self.items[i] < self.items[j]):
                    #print "j: %d, item[%d]: %d" % (j,j,self.items[j])
                    maximum = j
                    #self.items[i],self.items[maximum]=self.swap(self.items[i],self.items[maximum]) 
                    self.items[i],self.items[maximum] = self.items[maximum],self.items[i]
    
    
    def swap(self,i,j):
        temp = j
        j = i
        i = temp
        return i,j