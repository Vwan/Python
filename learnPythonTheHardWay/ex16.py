from sys import argv

script, filename=argv

raw_input("?")
target = open(filename,"w")

target.truncate()

line1=raw_input("line 1:")
line2=raw_input("line 2:")

target.write(line1+"\n")
target.write(line2+"\n")

target.close()
