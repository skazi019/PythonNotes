# Python

- Try except else finally
- [OOPS and Classes](#oops-and-classes) | [material](https://www.python-course.eu/python3_object_oriented_programming.php)
  - [`__init__`](#__init__)
  - [Data Encapsulation, Information Hiding, and Data Abstraction](#data-encapsulation-information-hiding-and-data-abstraction)
  - [Public, Protected, and Private access modifiers](#public-protected-and-private-access-modifiers)
  - [Destructor](#destructor)
  - [Instance methods, Class methods, and Static methods](#instance-methods-class-methods-and-static-methods-link)
  - properties
  - [Dataclass](#dataclass)
  - Meta Class
  - interface
  - Method resolution order of classes
- [Linter in python](#linter-in-python)
- Messaging queues - rabbitmq, redis, kafka
- Topic in Kafka
- caching
- async programming
- wsgi
- asgi
- [Swagger](#swagger)
- [Design patterns](https://python-patterns.guide/)
- Status code HTTP
- Git conflicts
- PEP8 | [material](https://www.python.org/dev/peps/pep-0008/)
- [duck typing](#duck-typing)
- [type hinting in python](#type-hinting)
- Documenting code in python
- changing functionalities of packages in python
- `eval()`
- REST APIs
- Pickling and unpickling
- Hooks(either in django or http)
- Event driven programming
- itertools
- functools
- pass by value, pass by reference
- `walrus` operator
- bitwise operations

<br />

---

### Try except else finally
 - try: this block is the code for which the error is supposed to be catched.
 - except: Here the code for when the exception occurs.
 - else: if there is no exception then this block will be exceuted.
 - finally: this block always gets exceuted whether the exception is generated or not.
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
### OOPS and Classes
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
**Data Abstraction** is present if both _Data Encapsulation_ and _Information Hiding_ is used.

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
<br />

#### Destructor
Theres no real destructor, but the `__del__` is called when you `del object`.So you can type in any block of code that you want to execute before deleting an object.

<br />

#### Instance methods, Class methods, and Static methods [(RealPython.com)](https://realpython.com/instance-class-and-static-methods-demystified/#delicious-pizza-factories-with-classmethod)
 - Instance method - most common type of method that is used most of the time. Takes in the first arguement as `self` which is the instance of the class.\
 through the `self` parameter, you can freely access other attributes and methods of the same object. this gives them a lot of power when it comes to modifying the state of an object.
 - Class method - Instead of accepting `self`, it takes `cls` which points to the class and not the object.\
 It can't modify an instance's state. They can modify a class's state that would apply across all the instances.\
 Python only allows one `__init__` method per class. Using class methods, it's possible to add many alternative constructors as necessary.
 - Static method - These methods neither take `self` or `cls` as an arguement but can accept any number of other arguements.\
 Therefore static methods can neither modify object state or class state. They are restricted to what data they can access, primarily they are a way to `namespace` your methods.\
 When the `@staticmethod` decorator is used, even python runtime won't let that methods modify attributes of the class or instance.

<br />

#### Properties
Allow us to define a method that can be accessed as an attribute.\
If we need to set/update some attribute without changing the code, we can do that using the `@property` decorator to change a method into an attribute.\
```
class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
    
    @property
    def email(self):
        return f'{self.first}.{self.last}@email.com'
    
    @property
    def fullname(self):
        return f'{self.first} {self.last}'


emp_1 = Employee('John', 'Smith')

print(emp_1.first) # John
print(emp_1.email) # John.Smith@email.com
print(emp_1.fullname) # John Smith
```
Allows us to dynamically set attribute values, using method, if some attribute are updated.\
To update this property, you'll have to create a setter.

```
@fullname.setter
def fullname(self, name):
    first, last = name.split(' ')
    self.first = first
    self.last = last

emp_1.fullname = 'Kaushal Sharma'

Output -
Kaushal
Kaushal.Sharma@email.com
Kaushal Sharma
```

<br />

#### Dataclass ([material](https://docs.python.org/3/library/dataclasses.html#module-level-decorators-classes-and-functions))
This module provides a decorator and functions for automatically adding generated *special methods* like `__init__()` and `__repr__()` to the user defined class.\

```
from dataclasses import dataclass

@dataclass
class InventoryItem:
    """Class for keeping track of of an item in Inventory"""
    name: str
    unit_price: float
    quantity_on_hand: int = 0

    def total_cost(self) -> float:
        return self.unit_price * self. quantity_on_hand
```
The preceeding code will create an `__init__()` constructor for the class _InventoryItem_, among other things, which would look like the following. This will be done automatically.

```
def __init__(self, name: str, unit_price: float, quantity_on_hand: int = 0):
    self.name = name
    self.unit_price = unit_price
    self.quantity_on_hand = quantity_on_hand
```
Dataclass decorator can have parameters as follows
```
@dataclass(init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False)
class A:
    ...
```
 - init - if true `__init__()` will be generated. if it is already present in the class then this parameter is ignored
 - repr - if true `__repr__()` will be generated. The generated repr string will have the class name and the name and repr of each field. in the order they are defined in the class.
 - eq - If true `__eq__()` methods is generated. This methods compares the class as if it were a tuple of its fields, in order. Both instances in the comparison must be of the identical type.
 - order - if true, `__lt__()`, `__le__()`, `__gt__()`, and `__ge__()` methods will be generated. (same explanation as above)

<br />

#### Meta class
A class whose instances are other classes is called a Metaclass.\
Usecases for metaclasses -
 - logging and profiling
 - interface checking
 - registering classes at creation time
 - automatically adding new methods
 - automatic property creation
 - proxies
 - automatic resource locking/synchronization



---

### Linter in Python
We all make mistakes why writing code and you can't expect yourself to catch all of them. Mistyped variable names, forgetting closing bracket, incorrect indentation, calling function with wrong number of arguements, etc. Linters help you identify such problems in your code.\
Most editors/IDEs run linters in the background, highlighting, underlining, or otherwise identifying the problems in the code before you run it. Like a spell-check for code.\
Two types of linting -
 - Logical lint
   - code errors
   - indentation issues
   - dangerous code patterns
 - Stylitic lint

VsCode uses Pylance which is powered by Microsoft's Pyright which is a static type checking tool. 

---

### Swagger
Swagger allows you to describe the structure of your APIs so that machines can read them.\
It is basically a set of rules(specifications and tooling for how to semantically describe APIs.\
Advantages-
 - Comprehensible for both developers and non-developers
 - Human readable and machine readable
 - Easily adjustable 

**Makes the APIs more consumable**.

---

### Duck typing

Duck typing is a concept related to dynamic typing, where the type or class of an object is less important than the methods it define.\
When you use duck typing, you do not check for type at all. Instead, you check for the presence of a given method or attribute.\
example - `len()` in python\
it looks for `__len__()` method for the object it is called upon.
```
class Hobbit:
    def __len__(self):
        return 95022

my_str = "Hello World"
my_list = [34, 54, 65, 78]
my_dict = {"one": 123, "two": 456, "three": 789}

len(Hobbit) # 95022
len(my_str) # 11
len(my_list) # 4
len(my_dict) # 3
```
Therefore, In order for you to call `len(obj)`, the only real constraint on obj is that it must define a `__len__()` method. Otherwise, the object can be of types as different as str, list, dict, or Hobbit.\
Another example could be `str()`.

---

### Type hinting
It is basically done to indicate the type of the arguements being passed into a function and what will be the type of the ouput of the function.
```
def greet(name: str, align: bool = True) -> str:
    return "Hello" + name
```

---

### Status codes in HTTP

#### Successful Responses
 - `200 OK` - The request has succeeded. 
 - `201 Created` - The request has succeeded and a new resource has been created. Typically response sent after `Post` request and some `Put` requests.
 - `202 Accepted` - The request has been received but not yet acted upon. It is intended for casese where another process or server handles the request, or batch processing.
 - `203 Non-Authoritative Information` - the returned meta-information is not exactly the same as is available from the origin server, but is collected from a local or third-party copy. Mostly used for mirrors or backups of another resource.