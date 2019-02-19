#!/usr/bin/env/ python


# order of fget, fset and fdel is important
# pay attention to type of Person.name and method of this property object
# properties are inheritable, see Employee class.
# dir(Person.name) -> setter, getter, deleter
# property can act as decorator

class Person(object):
	def __init__(self, name):
		self._name = name

	def fget(self):
		"""
		get me person's name
		"""
		print "Fetch name"
		return self._name

	def fset(self, value):
		print "Set name"
		self._name = value

	def fdel(self):
		print "Deleteing name attribute"
		del self._name

	name = property(fget, fset, fdel, "Name property doc")


class Employee(Person):
	pass


if __name__ == "__main__":
	person = Person("Vijay")
	print "Docstring for person's name attribute: {}".format(Person.name.__doc__)
	print "Printing person's name : {}".format(person.name)
	person.name = "Shanker"
	del person.name
	print "------------------------------- "
	emp = Employee("Hari")
	print emp.name

	print "-------------------------------"
	print type(Person.name)
	print "-------------------------------"
	print dir(Person.name)
	print "-------------------------------"	
