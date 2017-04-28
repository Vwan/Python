def print_2(*args):
	arg1,arg2=args
	print "this *args is called"
	print "arg1: %r, arg2:%r" % (arg1,arg2)

def print_2(arg1,arg2):
	print "this is called"
	print "arg1: %r, arg2:%r" % (arg1,arg2)

print_2("Zed","Shaw")
print_2("Zed","Shaw")
