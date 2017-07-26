elements=[1,2]
for i in range(0,6):
    elements.append(3+i)
    #print i

for i in elements:
    print i

elements = range(0,6)
for i in elements:
    print elements.pop()
    print "----%d" % i