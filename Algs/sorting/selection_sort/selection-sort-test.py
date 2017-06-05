# -*- coding: utf-8 -*-
import random
import string
from timeit import default_timer as timer

from selection_sort import SelectionSort

print "-"*10 + "sorting numbers" + "_"*10
items = []
for i in range(0,10):
    items.append(random.randint(2,999))
print "original items: %r" % items
ssort = SelectionSort(items)

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

print "-"*10 + "sorting alpha characters" + "_"*10
items=[]
for i in range(0,10):
    items.append(random.choice(string.ascii_letters))
print "original items: %r" % items
ssort = SelectionSort(items)
ssort.sort()
items.sort()
assert ssort.items == items
print "sorted items: %r" % ssort.items

print "-"*10 + "sorting strings" + "_"*10
items=[]
for i in range(0,10):
    items.append("".join(random.choice(string.ascii_letters+string.digits) for s in range(0,10) ))
print "original items: %r" % items
ssort = SelectionSort(items)
ssort.sort()
items.sort()
assert ssort.items == items
print "sorted items: %r" % ssort.items