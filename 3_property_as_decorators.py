#!/usr/env/bin python

class Person(object):
	def __init__(self, name):
		self._name = name

	@property
	def name(self):
		"""
		Name property docsting
		"""
		print "Fetching name"
		return self._name

	@name.setter
	def name(self, value):
		print "setting name attribute"
		self._name = value

	@name.deleter
	def name(self):
		print "deleteing name attribute"
		del self._name


if __name__ == "__main__":
	p = Person("vijay")
	print p.name
	p.name = "Shanker"
	del p.name
