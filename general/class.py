class test():
    def __init__(self,name):
        self.name=name

    def test(self,loud=False):
        if loud:
            print self.name
        else:
            print "wrong"


t = test('hello')
t.test()
t.test(True)
t.test(loud=False)
        
