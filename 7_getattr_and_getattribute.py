#!/usr/bin/env python



class Person(object):
	def __init__(self, name):
		self.name = name

	def __getattr__(self, attrname):
		print "intercepting undefined attribute access"
		if attrname == 'profession':
			return "Dev"
		else:
			raise AttributeError("Undefined attribute: '{}'".format(attrname))

	def __getattribute__(self, attrname):
		print "intercepted attribute access inside __getattribute__, looking for '{}'".format(attrname)
		return object.__getattribute__(self, attrname)


if __name__ == "__main__":
	p = Person("vijay")
	print p.name
	print p.profession
	print p.gamer