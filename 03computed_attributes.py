#!/usr/bin/env python


class PropSquare(object):
	def __init__(self, value):
		self.value = value

	def squaredx(self):
		return self.value**2

	def setvalue(self, value):
		self.value = value

	def delvalue(self):
		del self.value
 	x = property(squaredx, setvalue, delvalue, "computed attribute example")


if __name__ == "__main__":
	p = PropSquare(4)
	print p.x
	p.x = 6
	print p.x
	print dir(PropSquare.x)
