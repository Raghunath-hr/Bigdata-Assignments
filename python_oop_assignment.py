"""
Q1) Purpose of OOP
>>>		*modularity for easier trubleshooting
		*reuse of code through inheritance
		*flexibility through polymorphism
		*effective problem solving

Q2)	where dose inheritance search look for an attribute
>>>		*first occurance of object by looking in object, then in all classes above it
		from bottom to top and left to right.

Q3) Class obj vs Instance obj
>>>		*At the time of class creation the  CLASS OBJECT is automatically created line(23)
		*whenever we class class with paramthesis as like in below example
		then the INSTANCE OBJECT for that class is created at line(24)

class Test:
	x = 10 #this is static member variable
	def __init__(self, a, b):
		self.a= a
		self.b= b

print(Test.x) #Here we are accessing static member variable with class object
obj_instance = Test() #this is called as instance object for Test class
					   Once this instance object is created the __init__ is called.



Q4) What makes the first argument in a class’s method function special?
>>>		the class itself

Q5) what is the purpose of init method
>>>		It is used for assigning values for newly created objects

Q6) Process for creating class instance
>>>		Call the class using class name and pass the arguments mentioned inside
		__init__ method.

Q7) Process for creating class
>>>		First write the name 'class' and give the name for the class 
		with 1st letter of itself in capital and the (:) colon at the end

Q8) Define superclass of class
>>>		Consider two classes:- class A and class B(A)
		here properties from class A are inherited in class B
		So class A is the Superclass or Parent class and
		class B will be subclass or child class.

Q9) Relationship between Class and Modules
>>>		Class in python act as blueprint on the basis of which we define objects
		whereas Modules are the predefined entities which can be imported by import statement
		for reusing of code in another program.
		Even we can import our own defined class inside other programm files
ex:		import FileName
		obj1 = FileName.ClassName()

Q10)Make instances and classes
>>>		class Student:
			def __init__(self, name):
				self.name = name
		instance_of_class = Student(Raghul)

Q11)Where and how should be CLASS ATTRIBUTES created
>>>		class attributes are created right after the class declaration
		and before initializing the __init__ method. ex as below

		class Country:
			country_code = 91 #this is called as class attribute

			def __init__(self, state):
				self.state = state

			def show_state(self):
				return (self.state + " " flag)

		country_obj = Country("Maharashtra")
		print(country_obj.country_code)  #accessing class attr with obj name
		print(Country.country_code)		 #accessing class attr with class name

Q12)where and how should be INSTANCE ATTRIBUTES created
>>>		Class attributes are created after declaration of class and before defining __init__ method
		instance attributes are created inside __init__ method with name self
		Example:-

		Class Aeroplane:
			speed = 5000 #this is class attr
			def __init__(self, name):
				self.name = name #this is instance attr
			def plane_detail(self):
				print("the plane is: ", self.name "and the speed is: ", Aeroplane.speed)
		plane = Aeroplane("Tejas")
		plane.plane_details()

Q13)"self" in Python
>>>		self is an instance of a class itself
		the first parameter of __init__ method is always self
		with using tis self we can access the attributes and methods of the class

Q14)How python class handles operator overloading
>>>		Suppose we declared two objects for the class A
		in this case there are two values and rquirement is to add them
		As we use binary operator + to add values but here it'll throw an error
		because compiler dont know how to add two objects.
		*When we use an operator on user defined data types then 
		automatically a special function or magic function associated with tha operator
		is invoked. You define methods in your class and operator works according to
		that behavior defined in methods.
		*When you change behavior of existing operator through operator overloading
		you have to rededfine the special function that is invoked automatically
		when the operator is used with the objects. 
		See the example below

		class Addnum:
			def __init__(self, a):
				self.a = a

			def __add__(self, b):
				return self.a + b.a

		obj1 = Addnum(30)
		obj2 = Addnum(50)

		(obj1+obj2)

Q15)When do you consider allowing operator overloading of your class?
>>>		when we describe any special or magic method for corrosponding operation
		like __add__ , __lt__, __mul__, __sub__, __pow__

Q16)What is the most popular form of operator overloading

Q17)What are the two most important concepts to grasp in order to comprehend Python OOP code
>>>		Inheritance and Polymorphgism are two main concpets of OOP

Q18)define three applications for exception handling
>>>		1) Try and Except Statement

a = [1,2,3]
try:
	print(f"4rth element is {(a[3]}")
except:
	print("error")
		
		2) Try with else clause

def try_with_else(a, b):

	try:
		c = ((a+b)/(a-b))
	except ZeroDivisionError:
		print("result gives zero")
	else:
		print(c) 

try_with_else(2,3) #will give output as -5.o i.e printing c from else block
try_with_else(2,2) #as output is zero it will print result gives zero.

		3)Finally Keyword in python

def try_finally(x):
	try:
		v = x//0
		print(v)
	except ZeroDivisionError:
		print("cant divide by zero")

	finally:
		print("if all cases fails this block will execute")


Q19)What happen if you dont do something extra to treat an exception?
>>>		Will not be able to seperate error handling code from normal code
		Exceptions reminds of what the program expects
		it will not clarify code and can reduce readability

Q20)What are your options for recovering from an exception in your script?
>>>		Try and except
		try and finally
		try and else	

Q21)Methods for triggering exceptions in script
>>>		try/except
		try/finally
		assert
		raise
		with/as

Q22)Purpose of try statement
>>>		Try block is used to ckeck any kind of errors for the perticular code
		at first the code inside try block runs and checks for errors

Q23)Try statement variations
>>>		Try/Except ; Try/Finally

Q24)Purpose of raise statement
>>>		raise statement raises an error and stops the current flow of the program
		while raising error we can also specify what kind of error to raise
		and can print out the same


Q25)What assert statement do and what other statement is it like?
>>>		If the assert condition is false of dose not satisfy the condition then
		it will halt the program and show the assertion error.

Q26)with/as statement in python
>>>		In python with statement is used in exception handlingto make code cleaner
		and much more readable. the with statement is popularly used with file streams

Q27)args* kwargs** in python
>>>		args* - It allowa you to take in more arguments than the number of 
		formal arguments that you previously defined.

		kwargs** - a keyword argument is where you provide a name to the variable
		kwargs is like being a dictionary that maps each keyword to the value that we pass

Q28)pass keyword arg from one func to another func


def pass_kwargs(**):
	dict1 = {'name':rahul', 'roll_no':23, 'city':'pune', 'pin':041}
	or
	dict1 = dict(name='rahul', roll_no=23, city='pune', pin=041)

	pass_into(dict1**) #dict1 wll be passed as keyword arg inside func pass_into

def pass_into(**kwargs):
	for i in kwargs:
		print(i, kwargs[i]) #printing key and value
pass_kwargs()		


Q29)what are lambda functions
>>>		lambda function can be defined withou declaring (def) keyword i.e without any name
		this function can have any number of arguments but only one expression
		*example

my_name = "raghunath"
reverse_upper = [lambda my_name: my_name.upper()[::-1]]
print(reverse_upper(my_name))


Q30)Inheritance in python
>>>		

class Person:

	def __init__(self, name):
		self.name = name

	def display(self):
		print(self.name)

emp1 = Person("Raghu")
emp1.display()

class Employee(Person):

	def display(self):
		print("he is employee: ", self.name)

emp2 = Employee("Rajesh")
emp2.display()


Q31)Class A, class B, class C with inheritance
>>> explained bellow

class A:
	def func(self):
		print("inside class A")

class B:
	def func(self):
		print("inside class B")

class C(A,B):
	def func(self):
		print("inside class C")

obj_c = C()
obj_c.func()
		* in above case it will print the "inside class C"
		* if we do nothing with class C (i.e pass) then it will print("inside class A")
			because class A is the first argument we passed in C
		* if we pass class B at first it will invoke func() method from class B


Q33)Which methods/functions do we use to determine the type of instance and inheritance
>>>		Following are methods to determine instance and subclass

		isinstance(object, classinfo)
			returns True if the object argument is an instance of a classinfo argument

		issubclass(class, classinfo)
			returns True if class is subclass of classinfo. Any class is subclass of itself


Q34)'nonlocal' keyword in python
>>>		the "NONLOCAL" keyqord is uder to work with variables inside nested func
		where the variable should not belong to the inner function.

		example:-

def func():
	a = 20
	def nested_func():
		nonlocal a
		a = 30
	nested_func()
	return a

print(func())

Q35)Global keyword in python
>>>		As we know we can access global variables inside functions but we can not modify it
		In this case we can use global keyword inside functions

		Example:-

r = "raghu"
def global_use():
	
	global r
	r = r + "panse"

	print(r)

global_use()
"""	

