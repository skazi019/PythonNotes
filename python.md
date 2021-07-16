# Python

- Try except else finally
- OOPS and Classes
- `__init__`
- Data Encapsulation, Information Hiding, and Data Abstraction
- Public, Protected, and Private access modifiers
- Destructor
- Instance methods, Class methods, and Static methods link
- Linter in python
- Messaging queues - rabbitmq etc
- async programming
- Method resolution order of classes
- wsgi
- asgi
- Data Class
- Swagger
- Design patterns
- Status code HTTP
- Git conflicts
- PEP8
- type hinting in python
- Documenting code in python
- changing functionalities of packages in python
- `eval()`
- REST APIs

<br />
<br />

### Try except else finally
- try: this block is the code for which the error is supposed to be catched.\
except: Here the code for when the exception occurs.\
else: if there is no exception then this block will be exceuted.\
finally: this block always gets exceuted whether the exception is generated or not.
```
try:
	...
except:
	...
else:
	...
finally:
	...
```
---
#### OOPS and Classes
Everything in python is "First Class" i.e. is a class so that everthing can be treated the same way. can be assigned to variables, stored in lists, stored in dictionaries, passed as arguements and so forth.\
Accessing a non-existing attribute(variable) will throw `AttributeError`. Use `getattr()` method to to prevent this error and set a default value for the attribute.
```
getattr(instance, attribute, deault_value)

getattr(x, 'energy', 100)
```
A **_method_** is just a **_function_** defined inside of a _class_.\
_self_ is not a keyword, you can basically use anything in place of that. It's only there as a **reference** to the _instance_ that is calling the class's _method_.

#### `__init__`
We need to create attributes of an instance right after it is created, this is done using the `__init__()` method.\
Example-
```
class Robot:
 
    def __init__(self, name=None):
        self.name = name   
        
    def say_hi(self):
        if self.name:
            print("Hi, I am " + self.name)
        else:
            print("Hi, I am a robot without a name")

x = Robot()
x.say_hi()
y = Robot("Marvin")
y.say_hi()

Output -
Hi, I am a robot without a name
Hi, I am Marvin
```
#### Data Encapsulation, Information Hiding, and Data Abstraction
**Data Encapsulation** - refers to the bundling of the data with the methods that operate on that data, or the restricting of the direct access to some of an object's components.\
**Information hiding** on the other hand is the principle that some internal information or data is _hidden_, so that it cannot be accidently changed.\
**Data Abstraction** is present if both _Data Encapsulation_ and _Information Hiding_ is used.\
<br />

_Encapsulation_ is often accomplished by providing two types of attributes: _getters_(accessors) and _setters_(mutators).\
**getters**: as the name suggests, these methods are used for accessing the values of the attributes.\
**setters**: these methods are used for changing the values of the attributes.\
example-
```
class Robot:
 
    def __init__(self, name=None):
        self.name = name   
        
    def say_hi(self):
        if self.name:
            print("Hi, I am " + self.name)
        else:
            print("Hi, I am a robot without a name")
            
    def set_name(self, name):
        self.name = name
        
    def get_name(self):
        return self.name
    

x = Robot()
x.set_name("Henry")
x.say_hi()
y = Robot()
y.set_name(x.get_name())
print(y.get_name())
Hi, I am Henry
Henry
```

<br />

`__str__` and `_repr__`\
Both of these methods are used to output a string representation of the object.\
`str()` is used for creating output for end user while `repr()` is mainly used for debugging and development. _repr’s_ goal is to be _unambiguous_ and _str’s_ is to be _readable_. For example, if we suspect a float has a small rounding error, repr will show us while str may not.\
`repr()` would give out the _official representation_ of the object, whereas `str()` would give out an output that the user can understand.

<br />

#### Public, Protected, and Private access modifiers

 - Public - these attributes can be freely used inside or outside of a class.\
 example - `name`
 - Protected - these attributes should not be used outside the class it is created in, unless it is a subclass.\
 example - `_name`
 - Private - These attributes are inaccessbile and invisible. It's not possible to either read or write these attributes except inside of the class.\
 example - `__name`
```
class A:
	def __init__():
	self.__priv = "I am private"
	self._prot = "I am protected"
	self.pub = "I am public"
```
#### Destructor
Theres no real destructor, but the `__del__` is called when you `del object`.So you can type in any block of code that you want to execute before deleting an object.

<br />

#### Instance methods, Class methods, and Static methods [link](https://realpython.com/instance-class-and-static-methods-demystified/#delicious-pizza-factories-with-classmethod)
 - Instance method - most common type of method that is used most of the time. Takes in the first arguement as `self` which is the instance of the class.\
 through the `self` parameter, you can freely access other attributes and methods of the same object. this gives them a lot of power when it comes to modifying the state of an object.
 - Class method - Instead of accepting `self`, it takes `cls` which points to the class and not the object.\
 It can't modify an instance's state. They can modify a class's state that would apply across all the instances.\
 Python only allows one `__init__` method per class. Using class methods, it's possible to add many alternative constructors as necessary.
 - Static method - These methods neither take `self` or `cls` as an arguement but can accept any number of other arguements.\
 Therefore static methods can neither modify object state or class state. They are restricted to what data they can access, primarily they are a way to `namespace` your methods.\
 When the `@staticmethod` decorator is used, even python runtime won't let that methods modify attributes of the class or instance.