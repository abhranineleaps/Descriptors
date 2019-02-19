#!/usr/bin/env python
import inspect


class Person(object):
	def __init__(self, name):
		self._name = name

	
	def name(self):
		return self._name
	name = property(name)

	print "id of property type name: ", id(name)
	print type(name)
	print dir(name)
	
	print "id of setter: ", id(name.setter)
	print type(name.setter)

	def setname(self, value):
		print "intercepting attribute assignment"
		self._name = value

	name = name.setter(setname) # calling name.setter(setter_method) returns snew copy of property but with setter function replaced with decorated method
	print "id of property type name after assigning setter method: ", id(name)
	
	print "id of setter: ", id(name.setter)





if __name__ == "__main__":
	p = Person("vijay")
	print p.name 
	p.name = "shanker"