class node:
	def __init__(self,v=None):
		self.value=v
		self.next=None

	def isempty(self):
		return(self.value==None)

	def append(self,v):
		if self.isempty():
			self.value=v
		elif self.next==None:
			newnode=node(v)
			self.next=newnode

		else:
			(self.next).append(v)
		return()

	#inserting a node
	def insert(self,v):
		if self.isempty():
			self.value=v
			return()

		newnode=node(v)
		#exchange values on self and newnode
		(self.value,newnode.value)=(newnode.value,self.value)
		(self.next,newnode.next)=(newnode,self.next)
		return()

	#delete a node
	def delete(self,v): #There's also recursive way, skipped that part.
		if self.isempty():
			return
		if self.value==v:  #value to delete is in first node
			if self.next==None:
				self.value=None
			else:
				self.value=self.next.value
				self.next=self.next.next
				return()

		temp=self
		while temp.next!=None:
			if temp.next.value==v:
				temp.next=temp.next.next
				return()
			else:
				temp=temp.next
		return()

	def __str__(self):
		selflist=[]
		if self.value==None:
			return(str(selflist))
		temp=self
		selflist.append(temp.value)
		while temp.next!=None:
			temp=temp.next
			selflist.append(temp.value)
		return(str(selflist))

l=node(0)
print(l)
for i in range(1,100,9):
	l.append(i)
print(l)
l.delete(82)
l.insert(2)
print(l)