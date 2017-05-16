class Meta(object):
	def __init__(self,name,base,subcls):
		print(self,name,base,subcls)

Base=Meta('','','')

class Test(Base):
	prop1='hello'
