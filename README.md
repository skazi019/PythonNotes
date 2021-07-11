# Python notes

Table of Content
 - [Data types](#data-types)
 - [NameSpace](#namepsace)
 - [Scope](#scope)
 - [Lambda function](#lambda-function)
 - [Pass keyword](#pass-keyword-in-pyton)
 - [Copy](#copy-shallow-copy-and-deep-copy)
   - [Shallow Copy](#shallow-copy)
   - [Deep Copy](#deep-copy)
 - [Decorators](#decorators)


<br />

### Data types
 - Datatype of a object can be checked using functions type() or isinstance()

types
 - None - represents null value
 - Numeric - there are 3 distinct numeric types: integers, floating point numbers, and complex numbers
   - int
   - float
   - complex
   - bool
 - Sequence types - have the  ```in```  and ```not in``` for checking the elements
   - list
   - tuple
   - range
   - str
 - Mapping types -
   - dict
 - Set types - 
   - set
   - frozenset


[Back to top](#)
<br />

---

<br />

### Namepsace
 - Namespace in python ensures that object names are unique and can be used without conflict.
 - Python **implements namespaces as dictionaries** with **name as key** mapped to corresponding **object as value**
 - this allows **multiple namespaces** to use the **same name and map it to separate objects**
 - Types of namespaces
   - Local namespace - local names inside a function. namespace is created temporarily for a function call and gets cleared when the function returns
   - Global namespace - includes names from imported packages/modules or names created in global scope. this lasts until the exection of the script
   - Built-in namespace - includes the built-in functions and names
 - **Lifecycle** of a namespace **depends upon the scope** of the objects they are mapped to.

[Back to top](#)
<br />

---

<br />

### Scope
 - A scope is a block of code where objects remain relevant or where you can unambiguosly access the name, such as variables, functions, objects, etc
 - the **scopes** are **implemented as dictionaries that map names to objects**. these dictionaries are called **_Namespaces_**
 - They are stored in dunder method _dict_
```
import sys
sys.__dict__keys()

dict_keys(['__name__', '__doc__', '__package__',..., 'argv', 'ps1', 'ps2'])
``` 
 - The key method on displays all the names stored in module sys i.e. _dunder dict_ holds the namespace of _sys_ and is concrete representation of the module
 - Types of scopes
   - local / function
   - nonlocal / enclosing
   - global / module
   - Built-in


[Back to top](#)
<br />

---

<br />

### Lambda function
Lambda is an anonyomous function that can accept any number of arguements, but can only have one expression.
Generally used in situations requiring an anonymous function for a short period of time.

Example-
```
mul = lambda a,b: a * b

print(mul(2, 5))
Output: 10
```

[Back to top](#)
<br />

---

<br />

### Pass keyword in pyton
pass in python represents a _null operation_.
Generally used for fillin up empty blocks of code which may be executed during runtime but has yet to be written.


[Back to top](#)
<br />

---

<br />

### Copy [(Shallow Copy and Deep Copy)](https://docs.python.org/3/library/copy.html#module-copy)

In python, the assignment operator `=` does not copy the object. Instead, it just creates a binding between the existing object and the target variable name.
To create copies of object, we need to use the `copy` module.
Moreover, there are two ways to copy objects.
 - Shallow copy
 - Deep copy

<br />

#### Shallow Copy
constructs a new object and then inserts the references to the elements/objects into it. Therefore, though the object is new, it still references the same elements/objects as the original object. 

```
from copy import copy, deepcopy

list1 = [1, 2, [3, 5], 4]
list2 = copy(list1)

list2[3] = 7
list2[2].append(6)

list2    # output => [1, 2, [3, 5, 6], 7]
list1    # output => [1, 2, [3, 5, 6], 4]
```

<br />

#### Deep Copy
copies all the values recursively from the original object to the new object i.e. creates duplicated of the objects/elements referenced by the original object

```
list_3 = deepcopy(list_1)
list_3[3] = 8
list_3[2].append(7)

list_3    # output => [1, 2, [3, 5, 6, 7], 8]
list_1    # output => [1, 2, [3, 5, 6], 4]
```

#### Copying a list
 - .copy() - `list2 = list1.copy()`
 - list() - `list2 = list(list1)`
 - slicing - `list2 = list1[:]`

[Back to top](#)
<br />

---

<br />

### Range and XRange

<br />

---
<br />

### First Class functions


[Back to top](#)

<br />

---

<br />

### Decorators

Decorators are functions that adds some functionality to the function wihtout altering the structure of the original function.

Example -
```
def lowercase(func):
    def wrapper():
        string_lowercase = func.lower()
        return string_lowercase
    return wrapper


def splitter(func):
    def wrapper():
        string_split = func.split()
        return string_split
    return wrapper


@splitter # executed second
@lowercase # executed first
def hello():
    retun "Hello World"

hello()

output: ['hello', 'world']
```
[Back to top](#)

<br />

---

### Iterators
Iterators in python is simply and object that can be _iterated_ upon.
An object which will _return data one at a time_.\
An object is called _iterable_ if we can get an _iterator_ from it.\
Example: string, list, tuples are iterables\
An iterator must implement two dunder methods: **_iter_** and **_next_**.\
 - iter() - which in turn calls the dunder iter methods returns an iterator from the iterable
 - next() - is used to iterate through all the items of an iterator.

When we reach the end of the iterator and there is no more data to be returned, calling the `next()` methods will throw `StopIteration` exception.

```
my_iter = iter(my_list)
next(my_iter)
next(my_iter)
```
#### How `for` loop is implemented
```
for i in list:
  do something
```
is implemented as -
```
iter_obj = iter(list)
while true:
  try:
    element = next(iter_obj)
    do somehting
  except StopIteration:
    break
```
So, internally for loop first creates an iterator object by calling the `iter()` method on the iterable and then goes into an infinite `while` loop with a `try except` condition to iterate over the iterable and catch the exception when we reach the end of the iterable.

#### Infinite Iterators
`iter()` can be called with two arguements -
 - callable object
 - sentinel

The iterator calls this function till the return value is equal to the sentinel.
```
inf = iter(int, 1)
```
`int` always return 0, hence this is called infinitely.

\
[Back to top](#)

---

### Generators
> A generator is a function that returns an object(iterator) which we can iterate over one value at a time.

Defining a generator is as easy as defining a normal function with atleast one `yield` statement.\
A `return` statement terminates the function entirely, whereas `yield` statement pauses the function, saving all its state, and transfers the control back to the caller.\
When the generator is called it returns an iterator object but does not start executing immediately. Once the funtion yields, the function is paused and the control is transferred back to the caller.\
Local variable and their states are remembered between successful calls.\
Generators _don't hold_ the entire _result_ in _memory_, rather it _produces one result at a time_.

#### Generator Expressions
The syntax is similar to a list comprehension except replace `[]` with `()`.\
Generator expressions create anonymous generator functions.\
List comprehensions produces the entire list whereas generator expressions produces one item at a time.\
they have **_lazy execution_** i.e. producing items only when asked for. Hence, generator expressions are much more **_memory efficient_** than list comprehensions.
```
List comp: [x**2 for x in my_list]
Generator exp: (x**2 for x in my_list)
```

\
[Back to Top](#)

---

