#!/usr/bin/env python



class Name(object):
	"""
	Docstring for name object
	"""
	def __get__(self, instance, owner):
		print "Fetching name"
		return instance._name

	def __set__(self, instance, value):
		print "setting name"
		instance._name = value

	def __delete__(self, instance):
		print "deleteing attribute"
		del instance._name


class Person(object):
	def __init__(self, name):
		self._name = name
	name = Name()



if __name__ == "__main__":
	p = Person("vijay")
	print p.name
	p.name = "shanker"
	print p.name
	del p.name