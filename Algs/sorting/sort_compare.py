# -*- coding: utf-8 -*-

from insertion_sort.insertion_sort import InsertionSort
from selection_sort.selection_sort import SelectionSort
import time
import copy
import random

sizes = [
        1000,
        10000,
        50000
        ]

for size in sizes:
    # random generation of items to be sorted
    items = range
    print "-"*10 + "sorting numbers" + "-"*10
    items = []
    for i in range(0,size):
        items.append(random.randint(2,99999))
    #print "original items: %r" % items
    # the worse case
    items_worse = range (size-1,-1,-1)
    # the best case
    items_best = range(0,size)
    
    to_be_sorted = [
            ("random case",items),
            ("worse case",items_worse),
            ("best case",items_best)
            ]
    
    def duration(sort_method):    
        # calculate execution time for our selection sort method
        start = time.clock()
        sort_method.sort()
        end = time.clock()
        duration = end - start
        return duration
    
    for item in to_be_sorted:
        temp = copy.deepcopy(item) # for reversing use after a certain sort
        print "-"*10 + item[0] + "-"*10
        # calculate duration for insertion sort
        
        insertion_sort = InsertionSort(item[1])
        dinsertion = duration(insertion_sort)
        item = temp
        # calculate duration for selection sort    
        selection_sort = SelectionSort(item[1])
        dselection = duration(selection_sort)
        item = temp
        # calculate duration for python builtin sort
        dpython = duration(item[1])
        print "%s: %ds" % ("insertion sort",dinsertion)
        print "%s: %ds" % ("selection sort",dselection)
        print "%s: %ds" % ("python built-in",dpython)