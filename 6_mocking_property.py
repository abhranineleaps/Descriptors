#!/usr/bin/env python

# own init, maintains state
# explain similarity property and Property 


class Property(object):
	def __init__(self, fget=None, fset=None, fdel=None, doc=None):
		self.fget = fget
		self.fset = fset
		self.fdel = fdel
		self.__doc__ = doc

	def __get__(self, instance, owner):
		if instance is None:
			return self

		if self.fget is None:
			raise AttributeError("Can't get attribute")
		return self.fget(instance)
	
	def __set__(self, instance, value):
		if instance is None:
			return self

		if self.fset is None:
			raise AttributeError("Can't set attribute")
		self.fset(instance, value)

	def __delete__(self, instance):
		if instance is None:
			return self

		if self.fdel is None:
			raise AttributeError("Can't delete attribute")

		self.fdel(instance)


class Person(object):
	def __init__(self, name):
		self._name = name

	def fget(self):
		print "Fetching name attribute"
		return self._name

	def fset(self, value):
		print "Setting name attribute"
		self._name = value

	def fdel(self):
		print "Deleting name attribute"
		del self._name

	name = Property(fget, fset, fdel, "doctstring for name attribute of class Person")


if __name__ == "__main__":
	p = Person("vijay")
	print p.name
	p.name = "shanker"
	print type(Person.name)
	del p.name





