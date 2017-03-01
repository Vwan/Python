d={'cat':'cute', 'dog':'furry'}

for animal, strait in d.iteritems():
    print 'A %s is %s' % (animal,strait)

nums=range(5)
#nums.add(6) error
even_num_to_square = { x:x**2 for x in nums if x%2==0}
print even_num_to_square
