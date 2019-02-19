#!/usr/bin/env python

# attribute interception, attribute computed dynamically
# can't set < 0, data validation use case
# omit set, data descriptors

class SquaredDesc(object):
	def __get__(self, instance, owner):
		return instance._value**2

	def __set__(self, instance, value):
		if value <0 :
			raise AttributeError("Value too small")
		instance._value=value


class SquaredValue(object):
	def __init__(self, value):
		self._value=value
	value = SquaredDesc()


if __name__ == "__main__":
	s = SquaredValue(4)
	print s.value
	s.value = -2