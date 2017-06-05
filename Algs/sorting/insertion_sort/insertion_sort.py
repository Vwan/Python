# -*- coding: utf-8 -*-
class InsertionSort(object):
    items = []
    def __init__(self,items):
        self.items = items
    def sort(self):
        for i in range(1,len(self.items)-1):
            temp = self.items[i]
            if (self.items[i] < self.items[i-1]):
                for j in range(0,i): 
                    if (self.items[j] > temp): 
                        for k in range (i,j,-1):
                            self.items[k] = self.items[k-1] 
                        self.items[j] = temp
                        break;
                        
                        
class InsertionSort1(object):
    items = []
    def __init__(self,items):
        self.items = items
    def sort(self):
        for i in range(0,len(self.items)):
            j = i;
            while (j > 0 and self.items[j] < self.items[j-1]):
               # self.items[j],self.items[j-1] = self.swap(self.items[j],self.items[j-1])
                self.items[j],self.items[j-1] = self.items[j-1],self.items[j]
                j -=1
                
                
    def swap(self,i,j):
        temp = j
        j = i
        i = temp
        return i,j