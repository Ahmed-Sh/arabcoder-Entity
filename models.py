class member():
	"""docstring for ClassName"""
	def __init__(self, name,age,id):
		self.name = name
		self.age=age
		self.id=id
	def __str__(self):
		return "id: "+str(self.id) +"\nname:" +self.name+"\n=================="	
class post():
	def __init__(self, title,subject):
		self.title = title
		self.subject=subject
	def __str__(self):
		return "Title: "+self.title +"\n" +self.subject+"\n=================="
		
						
		