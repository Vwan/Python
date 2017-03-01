nums=range(5)

squares = []

for x in nums:
    squares.append(x**2)

print squares

squares1 = [x **2 for x in nums];
print squares1

squares2=[x**2 for x in nums if x%2==0]
print squares2
