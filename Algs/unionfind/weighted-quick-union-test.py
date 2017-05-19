# -*- coding: utf-8 -*-

import weightedquickunion

qf = weightedquickunion.WeightedQuickUnion(10)

print "initial root list is %s" % (",").join(str(x) for x in qf.root)

list = [
        (4,3),
        (3,8),
        (6,5),
        (9,4),
        (2,1),
        (8,9),
        (5,0),
        (7,2),
        (6,1),
        (1,0),
        (6,7)
        ]

for k in list:
    p =  k[0]
    q =  k[1]
    print "." * 10 + "unioning %d and %d"  % (p,q)  + "." * 10
    qf.union(p,q)
    print "%d and %d is connected? %s" % (p,q,str(qf.isConnected(p,q)    ))
    

print "final root list is %s" % (",").join(str(x) for x in qf.root)