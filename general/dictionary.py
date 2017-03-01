d={'cat':'cute', 'dog':'furry'}

print d['cat']
print 'cat' in d

d['fish']='wet'
print d['fish']

print d.get('monkey','N/A')
print d.get('fish','N/A')
print d.get('cat')

del d['fish']
print d.get('fish','N/A')
