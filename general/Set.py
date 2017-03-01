animal = {'cat','dog'}

print 'cat' in animal
print 'pig' in animal

animal.add('pig')

print 'pig' in animal

print len(animal)

animal.add('cat')
print len(animal)
animal.remove('cat')
print len(animal)
