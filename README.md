# Descriptors

what are attributes?

Object attribute are central to most python programs, that is where we store information about our entities.
attributes are names for objects, accessed and modified by dot notation.

Managing attributes:
by managing attribute access i mean Adding attribute accessor logic.
attribute accessor logic is something that we want to run when an attribute is retrieved/modified or is going to get deleted.

Use Cases:
 1. computing dynamic attributes
 2.	validation, bound checking
 3. stopping attributes getting changed
 4. allowing only certain set of attributes to be set on class
 5. stopping deletion of attributes.


I am going to discuss 4 attribute accessor techniques.


1. the property built-in, for routing specific attribute access to get and set handler methods.
2. the descriptor protocol, for routing specific attribute access to instance of classes having get/set/delete methods.
3. using __getattr__ and __setattr__, for routing all udefined attribute fetches and assignment to a generic handler method
4. using __getattribute__, for routing all attribute fetches to a generic handler method

the first two of these accessor techniques are generic handlers while last two are specific to particular attributes.


the code i will be showing will work in python 3 and python 2 versions when classes are new-styled classes.
new style classes are classes that inherit from object.

Properties:

1. Property protocol helps us to introduce attribute accessor logic at get, set and delete operations for specific attribute and we can also provide with attribute
docstring. 
2. Properties are created with property built-in and assigned to class attributes, and like all class attributes can be inherited by their base classes.
3. The property built-in accepts four arguments, lets call them fget, fset, fdel and doc. All of these arguments can be passed as None, which will
mean None of the get, set or delete operations are permitted on attribute and accessing any of them will result in AttributeError. 
4. If doc is not provided, the doc of fget will be used and fget does not have a docstring, it will default to None.
5. the built-in property call returns a property object assigned as class attribute and can be inherited.

run 01property.py

Points to make:
1. print statements when accessing attributes
2. properties are inheritable
3. class attribute is of <type 'property'>
4. has three methods of interest getter, setter and deleter.

run 02_property_as_decorator.py
Points to make:
1. when we define property with built-in, it takes 3 funcs (optional) as an argument, this makes way for using property as decorators.	
2. the property type have three methods -> getter, setter and deleter, these methods assign corresponding property accessor methods and return a copy of property itself.
3. getter component is filled by act of creating the property.
4. we can use these methods as decorators to introduce accessor logic.   


run 03computed_attribute.py
Points to make:
1. properties can be used to compute attributes dynamically when fetched.

--------------------------------------------------------------------------------------------------------------

Descriptors
1. Descriptors allows us to route get, set and delete operation of a specific attribute to instance of some class.
2. Descriptors are coded as independent classes, can have three methods, __get__, __set__ and __delete__ and are assigned to class attributes. 
3. These methods allows us to insert code to be automatically run when getting, setting or deleteing an attribute.
4. Descriptor class instance is assigned as class attribute and is inheritable.

run 04Descriptors.py

Points to make:
1. all attribute access is getting routed to descriptors get, set and delete method
2. modify the program, raise AttributeError when __set__ is called it a data descriptor

run 05computed_attributes_with_descriptors.py

Points to make:
1. getting value have been intercepted and is computed dynamically
2. in setting value, we raised AttributeError if value is less than 0.

run 06_mocking_property.py
Property class catches attribute access with descriptor protocol and routes access request to methods saved in descriptor state.

Points to make:
1. property are convinient way to create a descriptor
2. descriptors can maintain state of their own
3. go through the code. 

__________________________________________________________________________________________________________________

 "__getattr__" and "__getattribute__"

 these are generic attribute handlers. we override them in order to intercept attribute fetching operation and run our custom accessor logic.
 using these two, we can only intercept attribute fetches.
 (can override __setattr__ for attribute assignment, __delattr__ for attribute deletion.) 

"__getattr__"

  1. runs for undefined attribute, attributes not stored on an instance or inherited from Parent classes

"__getattribute__"
	
   1. runs for every attribute access
   2. it gets called first, if call fails, __getattr__ get called

run 07_getattr_and_getattribute.py

Points to make:
1. control flow of attribute access interception.

"__setattr__" and "__delattr__"

run 08_setattr_delattr.py

Points to make:
1. how inside init, how initialization calls setattr which modifies namespace, __dict__ and on calling del, key is removed from namespace dict.











































