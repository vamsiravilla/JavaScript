'''class Employee:
	emp_id = 101
	def display(self):
		print(self.emp_id)
em =Employee()
print(em)'''
#---------------------------------------------------------------------------------
from abc import ABC
class abcclass(ABC):
	def Father(self,x):
		print("passed value",x)
	def task(self):
		print("This is inside the abcclass")
class task(abcclass):
	def one(self):
		print("We are inside the task")
class example(abcclass):
	def two(self):
		print("we are inside the example class")
obj=abcclass()
obj.Father(100)
obj.task()
print(obj)

obj1 = task()
obj1.one()
print(obj1)