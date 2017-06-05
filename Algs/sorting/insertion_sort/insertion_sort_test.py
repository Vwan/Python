# -*- coding: utf-8 -*-
import random
from timeit import default_timer as timer

from insertion_sort import InsertionSort

print "-"*10 + "sorting numbers" + "-"*10
items = []
for i in range(0,10):
    items.append(random.randint(2,999))
print "original items: %r" % items
items=items_worse = range (10-1,-1,-1)
ssort = InsertionSort(items)

# calculate execution time for our selection sort method
start = timer()
ssort.sort()
end = timer() 
duration1 = end - start
# calculate execution time for python built-in sort method
start = timer()
items.sort()
end = timer()
duration2 = end - start

assert ssort.items == items
print "sorted items: %r" % ssort.items
print "Duration: our selection sort method - %ds, python builtin sort - %ds" % (duration1, duration2)
