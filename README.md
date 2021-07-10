# Python notes

<br />

### Data types
 - Datatype of a object can be checked using functions type() or isinstance()

Data types
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

<br />

---

<br />

### Pass 
pass in python represents a _null operation_.
Generally used for fillin up empty blocks of code which may be executed during runtime but has yet to be written.

<br />

---

<br />

### Copy (Shallow Copy and Deep Copy)
In python, the assignment operator `=` does not copy the object. Instead, it just creates a binding between the existing object and the target variable name.
To create copies of object, we need to use the `copy` module.
Moreover, there are two ways to copy objects.
 - Shallow copy
 - Deep copy

<br />

#### Shallow Copy
constructs a new object and then inserts the references to the elements/objects into it. Therefore, though the object is new, it still references the same elements/objects as the original object. 

```
from copy import copy

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

<br />

---
<br />

### First Class functions


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