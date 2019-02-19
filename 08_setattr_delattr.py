#!/usr/bin/env python


class Person(object):
	def __init__(self, name, profession):
		self.name = name
		self.profession = profession

	def __setattr__(self, attrname, value):
		print "intercepting attribute assignment, attribute name: '{}'".format(attrname)
		object.__setattr__(self, attrname, value)
		print self.__dict__.keys()


	def __delattr__(self, attrname):
		print "intercepting attribute deletion, attribute name: '{}'".format(attrname)
		object.__delattr__(self, attrname)
		print self.__dict__.keys()


if __name__ == "__main__":
	p = Person("vijay", "Developer")
	p.skills = "Python"
	del p.skills