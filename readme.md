# Udemy Course: Complete Python Bootcamp. Go from Zero to Hero in Python
[Course](https://www.udemy.com/complete-python-bootcamp/learn/v4/content)
[Repo python3](https://github.com/Pierian-Data/Complete-Python-3-Bootcamp)
[Repo python2](https://github.com/jmportilla/Complete-Python-Bootcamp)

## Section 1 - Course Overview

### Lecture 3 - Python 2 vs Python 3

* [diffs](http://sebastianraschka.com/Articles/2014_python_2_3_key_diff.html)
* [p3 support](http://py3readiness.org/)
* p3 is almost 100% supported and python 2 security support stops at 2020

### Lecture 4 - How to approach the course

* Programmers coming from an other lang
	* Read the lecture notebooks and follow along
	* if sthing is not clear , watch the screencast
	* take the quiz/test/hwork
	* check your understanding

### Lecture 5 - Course FAQs

* after installing anaconda->start anaconda navigator->launch jupyter notebook-> find the directory where are the .ipynb files
* to do it in command line we need python and jupyter notebook system installed
* [intallation manual](http://jupyter.readthedocs.io/en/latest/install.html)
* in the folder that we have our  .pynb files we run jupyter notebook

### Lecture 7 - Installing Python

* 1991 guido van rossum (NL)
* many benefits. huge amnt of libs
* we will use the free anaconda distro
* anaconda includes python and other libs (Jupyter)
* easy install (portable) on win, mac, ux
* jupyter notebook for scripts & later txt editors
* miniconda (small size anaconda)
* there are anaconda installers for every op system (step buy step instructions)
* for linux we download a script that we run
* for windows: Anaconda does not recommend adding it as a path env variable. tutor says do it. we dont
* once installed launch anaconda navigator and see the different available environments

### Lecture 8 - Running Python Code

* there are various ways to run python. the 3 main are
	* text editors
	* full ides
	* notebook envs
* test editors: can be customized with plugins, not python specific (sublime)
* full ides: python specific, extra funct. paid (PyCharm, Spyder-matlab style)
* notebook envs:  great to learn, support inline markdown notes, special file formats that are not .py, see in and out next to each other (Jupyter Notebook). they are used in data chinece and machine learning as you can see the visualizations next to code
* we run our first .py script in sublime (myexample.py)

```
print('hello world')
```

* we run `python myexample.py`
* running `python` starts the cli of python (interpreter)
* we now launch anaconda navigator and launch jupiter notebook (it is a webapp that runs on port 8889 or 8890)
* in jupiter notebook we can view all the files on the computer. also edit .py files
* in jupiter3 we can add a new notebook. once we do it it creates an unamde.ipynb file in the folder where we do it. if we rename it in the webapp file is renamed
* the notebook uses a cell based system. we write code in a cell run it and see the output. we do it click the play button and see the console output  right below.
* shift+enter runs the cell code
* the system cell can hold markdown text. we simply have to change its type from the dropdown list

## Section 3 - Python Object and Data Structure Basics

### Lecture 11 - Intro to Python Data Types

* Python Datatypes
	* integers(int)
	* floating point(float) : nums wit5h decimals
	* strings(str) : ordered sequence of chars
	* list(list) : ordered sequence of objects [10,"hello", 200.3]
	* dictionaries(dict) : unordered key:value pairs {"mykey":"value", "name","bob"}
	* tuples(tup) : ordered immutable sequence of objects  (10, "hello", 200.3)
	* sets(set) : unordered collection of unique objects {"a","b"}
	* booleans(bool)

### Lecture 12 - Numbers

* Basic numeric calculations same like any language
* Power is ** so ` 2 ** 3  = 8`
* Root can be represented as  `9 ** 0.5 = 3` (sqrt)
* Floor division is // returns πηλικο so ` 7 // 5 = 1 `
* order of operations: () >  * / > + - 

### Lecture 13 - Numbers FAQ

* [why 0.1+0.2-0.3 is not equal to 0.0](https://docs.python.org/2/tutorial/floatingpoint.htm)
* python performs true division by default (has decimals)

### Lecture 14 - Variable Assignments

* Rules for var names: names cannot start with number, no psaces allowed, no special symbols (yes to underscore _ )
* python name style: no uppercase, no special meaning words
* Python uses Dynamic Typing,  you can reassign vars to different data types, but: be careful for bugs, use type() to see the current datatype
* no var types. straight assignement in python `a = 1`
* in python for strings we can use double quotes or single quotes


* Strings are ordered sequences. we can use indexing and slicing to grab sub-sections

### Lecture 15 - Intro to Strings

* indexing in python strings uses index and reverse index. index starts at 0 till length-1. reverse index is 0 at start and then counts reverese from end to start. so last char will have rev index -1. and 2nd char will have -(length-1)
* slicing uses indexes [start:stop:step] start is numerical index, stop is the index we go up to (not include). step is the size of the jump we take
* in out of interpreter returns strings with quotes. as is. we can use print() to see the console output (no quotes). eg outputing 2 strings shows only the last in output. escape sequences allow adding special chars  \n \t
* length of string is returned with len() `len("hello") = 5`
* slicing in action

```
mystring = "abcdefghijk"
mystring[2:] => "cdefghijk"   // implicit Default stop=end , no jump
mystring[:2] => "ab"          // implicit Default start=0 , no jump
mystring[2:5] => "cde"			// implicit Default  no jump
mystring[::2] => "acegik"   // jump =2(skip 1) implicint default start =0 , stop = end 
mystring[::-1] => "kjihgfedcba" // jump -1 reverses char order, back steping
```

* performing indexing or slicing on literals is legal `"Hello World"[8]`

### Lecture 17 - String Properties and Methods

* Strings are Immutable. we cannot mutate a char, an element. `name = "Sam"` `name[0] = "P` is not allowed
* comments in Python start with hashtag #
* We can use string concatenation instead (adding strings with +)

```
name = "Sam"
last_letters = name[1:]
name = "P" + last_letters
```

* also * is allowed in strings "z" * 10 => "zzzzzzzzzz" (string multiplication)
* we cannot do concatenation with numbers
* if i type . after the string var and press tab i get all string available methods and attributes. some useful are e.g strvar ="Hello World"
	* stringvar.upper() => "HELLO WORLD" (does not reasign)
	* stringvar.lower() => "hello world"
	* stringvar.split() => ['Hello','World'] (list of strings) default splits on whitespace. we can set the char to do the split on e.g split(','), split remoives the char it splits on

### Lecture 19 - Print Formating w/ Strings

* string interpolation (put var in the string)
* format method. "string here var1: {} var2: {}".format('val1','val2') `print("this is a string {}".format(' fun loving STRING'))`
* in format i can set order `print("the {2} {1} {0}".format('fox','brown','quick')` => the quick brown fox
* ican use variables in format insttead of index. `print("the {f} {b} {b} {q}".format(f='fox',b='brown',q='quick')` => the fox brown brown quick
* float formating follows "{value:width.precision f}"

```
result = 100 / 777 => 0.1285635867932789
print('The result was {r:1.3f}'.format(r=result)) => The result was 0.129
```

* setting width 1 of a val with more than 1 digits does not cut integer digits
* fstrings new in 3.6 (no need for format)

```
name = 'Sakis'
print(f"Hello, my name is {name}")=> Hello, my name is Sakis
```

### Lecture 21 - Lists in Python

* lists in python are order sequences that can hold a variety of object types.
they support indexing slicing and nesting
* MIX TYPE LISTS ARE SUPPORTED
* len(my_list) return the length. indexing and slicing is the same as strings
* also concatenation is same and multiplication
* = assignment saves the result somewhere
* lists are muttable
* .append() method is like JS push. adds an element to the end
* .pop() method is lik in JS . removes an element from the end. returns it and modifies the list (removes the item). i cann pop by index passing the index.
* sort, reverse. sort() sorts alphabetically or numerical modfying a list. does not return anything. revverse() reverses the list.
* NoneType is NaN. no value
* indexing nested lists works like `mylist[1][2]` 

### Lecture 23 - Dictionaries in Python

* dictionaries are unordered maps for storing objects
* they use key:value pairs. we can use key to quickly grab objects without knowing the index location
* they use curly braces and : `my_dict = {'key1':'value1','key2':'val2'}`
* dictionaries: unordered cannot be sorted, lists: ordered,sliced,indexed
* to get a value from a dictionary we pass the key `my_dict['key1']` => 'value1'
* we can nest dictionatries and cascade keys to access val `d['key1']['subkey1']`
* value can be anything
* i can extend the dictionary by directly setting new keyvalue pairs `my_dict['key3'] = 'val3'`, we can use this notation to overwrite a value on an existing key value pair. 
* i can use .keys() or .values() to extract the keys or values of a dictionary in a list. `my_dict.keys()` => dict_keys(['key1','key2','key3']). if i want the pairing i write .items()
* keys should always be strings

### Lecture 25 - Tuples in Python

* tuples are like lists but immutable. once an element is in tuple cannot be reasigned.
* tuples use parenthesis: `t = (1,2,3)`. slicing, indexing, mix types are allowed
* t.count(1) counts the occurence of an element in a tuple t.index(1) returns the first occurence of an element in a tuple

### Lecture 26 - Sets in Python

* sets are unordered collections of unique elements
* it uses curly braces like dictionaries but without key value pairs.
* how to create them `myset = set()` to add an element `myset.add(1)`
* adding again same element does not throw error but is ignored,
* if i have alist with duplicates and cast it into a set `set(mylist)` what i get back is a set of the unigue elements

### Lecture 26 - Booleans in Python

* in python True and False reserved words must be capitalized
* b = None defines the val a s non value NoneType element

### Lecture 28 - IO with basic Files in Python

* in jupiter textbook i can create a file with 

```
%%writefile test.txt
first line of text
second line of text
third line of text
```

* i can open a file with `myfile = open('test.txt')` it creates a stream.
* if the file i try to access does not exist i get a FileNotFoundError Error 2
* i can get this error if file is in other dir. i can check the dir in jupiter notebook with pwd
* after opening the file we can read it with `myfile.read()`. it returns a string with what is the file. we see that the output contains pecial characters like \n. 
* if y run the command again i get empty string. this is because this is a stream or buffer of data and the pointer is moving when we read. 
* to set the pointer back to the start we use `myfile.seek(0)` and then i can read again. if i pass a value in read. i read a specified number of chars from the file
* if instead of read() i use readlines() i get a list of strings , one per line. the string still contain special chars
* up to now we ve worked with files that are in the same location as our script (python notebook). to open a file from an other directory in our file system we need to pass the complete filepath. we can see our current path with pwd (maybe we should check relative paths)
* when i open a filestream with open() i have to close the stream when finishing `myfile.close()`
* the new style of opening file streams is with the following syntax. whatever is in the indented space use the my_new_file stream. when i leave the indented commands the stream closes without us needing to manually close it. the params in the indented space are visible outside

```
with open('myfile.txt') as my_new_file:
	contents = my_new_file.read()
print(contents)
```

* up to now we were only reading from files. we will now write and overrite files
* open command supports various arguments like mode (r=read, w=write etc). i can see in Python Jupiter notebook the docs for each method by Shift+Tab in the function  args section (). if i want to just read i write

```
with open('test.txt', mode='r') as my_new_file:
	contents = my_new_file.read()
print(contents)
```

* if i set mode='w' and try to read() i get an error (non readable). the available modes are
	* mode='r' read only
	* mode='w' write only (ovewrite file  oe create new)
	* mode='a' write only (append)
	* mode='r+' read+write
	* mode='w+' write + read (overwrite files or create new)

```
with open('test.txt', mode='a') as f:
	f.write('Third Line')
```

* test solution

```
with open('test.txt', mode='w') as f:
    f.write('Hello World')
```

* Links dor practice

* [Basic Practice](http://codingbat.com/python)
* [More Mathematical (and Harder) Practice](https://projecteuler.net/archive)
* [List of Practice Problems](http://www.codeabbey.com/index/task_list)
* [A SubReddit Devoted to Daily Practice Problems](https://www.reddit.com/r/dailyprogrammer)
* [A very tricky website](http://www.pythonchallenge.com/)

### Lecture 30 - Python objects and Data Struct Assesment Test Overview

* we open Objects and Data Structures Assessment Test Jupiter Notebook from Course Repo

## Section 4 - Python Comparison Operators

### Lecture 31 - Comparison Operators in Python

* basic operators same as any language (see assesmet in previous section)
* in strings capitalization counts
* no typecasting between strings and nums in comparison `'2' != 2`
* comparison between floats and integers? integer is treated a s float `2.0 == 2`
* comparison operators can be chained priority left to right `1 < 3 > 2 is True` 

### Lecture 32 - Chaining Comparison Operators in Python withg Logical Operators\

* Logical operators, AND `and`, OR `or`, NOT `not` like any other language 
* parentheses are not necessary. comparison operators take precendence over logical operators

## Section 5 - Python Statements

### Lecture 33 - If Elif and Else statements in Python

* flow control with if, elif else
* control flow sysntax makes use of colons and indentations (whitespace) no brackets

```
if some_condition:
	# execute code
elif some_other_condition:
	# do sthing different
else: 
	# do something else
```

* we can have multiple elif

### Lecture 34 - For Loops in Python

* many objects in Python are iterable. we can iterate over every element in the object
* tuples, sets, lists and strings are iterable
* for loop is used to execute block of code for every iteration
* syntax

```
my_iterable=[1,2,3]
for item_name in my_iterable:
	print(item_name)
```

* i can add control logic in the looped code
* INDENTATION IS CRITCAL IN PYTHON
* i can pass external vars in the loop by using them (e.g calculate sum)

```
list1 = [1,2,3,4,5,6,7,8,9,10]
list_sum = 0 

for num in list1:
    list_sum = list_sum + num # or +=

print(list_sum)
```

* if i dont intend to use a variable in the loop a common pattern in python is to name it _ (for _ in list:)
* i can do tuple unpacking froma list using for loop to extract individual elements from tuples in a list

```
mylist = [(1,2),(3,4),(5,6),(7,8)]
len(mylist)
for (a,b) in mylist: #parenthesis is not necessary
	print(a)
	print(b)
```

* for loop can be used to iterate in a dictionary, but it iterates through the keys

```
d = {'k1':1,'k2':2,'k3':3}
for item in d:
	print(item)
>> k1
>> k2
>> k3
```

* to get the items we need to iterate through the dictionary intems with d.item()

```
d = {'k1':1,'k2':2,'k3':3}
for item in d.items():
	print(item)
>> ('k1',1)
>> ('k2',2)
>> ('k3',3)
```

* i can use typle unpacking to get the values back

```
d = {'k1':1,'k2':2,'k3':3}
for key,value in d.items():
	print(value)
>> 1
>> 2
>> 3

# or use 

for value in d.values():
	print(value)
```

* dictionaries are unordered. there is no guarantee i will get items in the order they are inserted

### Lecture 35 - While Loops in Python

* while loops will continue to execute a block of code while a condition is true
* we can combine while with else so that an other block is executed while the opossite condition is true (else is executed only once!!!!!!!!!!!!!!!)
* syntax:

```
while some_boolean_condition:
	# do something
else:
	# do something different
```

* with while loop it is common to get into an infinite loop. we do KERNEL interrapt or restart notebook to stop it, or Ctr+C

```
x = 0
while x < 5:
	print(f'The current value of x is {x}'')
	x+=1
else:
	print("X is not less than 5")
>>> The current value of x is 0
>>> The current value of x is 1
>>> The current value of x is 2
>>> The current value of x is 3
>>> The current value of x is 4
>>> X is not less than 5
```

* 3 keywords useful with loops *break* *continue* *pass*
	* break: Breaks out of the current closest enclosing loop. (skip and exit)
	* continue: Goes to the top of the closest enclosing loop. (skip)
	* pass: Does nothing at all.
* if i dont put anything after a loop control statement i get error , i can use pass instead

```
for item in x:
	pass
```
### Lecture 36 - Useful Operators in Python

*  range can be used in for loops as a literal list of numbers range(startval,endval,step) endval is exluded. range is a generator built in

```
for num in range(2,8,2):
	print(num)
>>> 2
>>> 4
>>> 6
```

* the operation below is so common we will use the enum function to make it simpler

```
index_count=0
for letter in 'abcde':
	print('At index {} the letter is {}'.format(index_count,letter))
	index_count +=1
>>> At index 0 the letter is a
...
```

```
index_count=0
word='abcde'
for letter in word:
	print(word[index_count])
	index_count +=1
>>> a
>>> b
...
```

* with enumerate function things are simple, what we get back is tuples, i can use tuple unpacking to extract the info i want `for item,letter in eneumerate(word):`

```
word='abcde'
for item in enumerate(word):
	print(item)
	index_count +=1
>>> (0,'a')
>>> (1,'b')
...
```

* zip function is opposite of enumerate, it zips together multiple lists in a list of tuples. of course i can use unpacking on it

```
mylist1 = [1,2,3]
mylist2 = ['a','b','c']
for item in zip(mylist1,mylist2):
	print(item)
>>> (1,'a')
>>> (2,'b')
>>> (3,'c')
```

* i can see the list with `list(zip(mylist1,mylist2))`
* the in operator checks if a value is in a list, string or dictionary

```
'x' in [1,2,3]
False
```

```
d={'mykey':345}
345 in d.values()
>>> True
```

* other operators is min,max

```
mylist = [1,2,3,4,5]
min(mylist)
>>> 1
max(mylist)
>>> 5
```


* random is a library with multiple functions in it. we see shuflle which scrambles any time we call it. randint(lowrange,highrange) returns a random int between the two vals

```
from random import shuffle
mylist = [1,2,3,4,5,6]
shuffle(mylist)
>>> [3,1,6,2,4,5]
```

* we can capture user input by using input() to store input in a var. input considers anything we type as a string. we need to use casting

```
number = input('Enter a number here: ')
>>> Enter a number here: 50
result
>>> '50'
float(result)
>>> 50.0
```

### Lecture 37 - List Comprehensions in Python

* list comprehensions is a unique way of quickly creeating a list in Python
* so no more .append() in a for loop

```
# novice way to convert a string to list
mystring = 'Hello'
mylist = []
for letter in mystring:
	mylist.append(letter)

# one liner
mylist =[letter for letter in mystring]
```

* this one liner flattens the for loop `mylist = [x for in 'hi there']`
* we can use to make strings out of range `mylist = [x for x in range(0,100)]`
* in this flattened syntax i can perform operations to the temp var i use in the for loop to mutate the elements prior to constructing the list e.g square them `mylist = [x**2 for x in range(0,100)]`
* we can chain if statements to this flattened syntax e.g square only even nums `mylist = [x**2 for x in range(0,100) if x%2 == 0]`
* we can even set literal math formulas to mutate the element putting them in parenthesis. `fahr = [((9/5)*x + 32) for x in celc]`
* we can put if and else statement in a list comprehension although is ugly and unreadable. not recomended

```
results = [x if x%2== 0 else 'ODD' for x in range(0,11)]
>>> [0, 'ODD',2,'ODD',4,'ODD,6,'ODD',8,'ODD',10]
```

* also we can put nested loops in list comprehension

```
# using typical for loop
mylist = []
for x in [2,4,6]:
	for y in [1,10,100]:
		mylist.append(x*y)

# using list comprehension
mylist = [x*y for x in [2,4,6] for y in [1,10,100]]
```

## Section 6 - Methods and Functions

### Lecture 40 - Methods and the Pthon Documentation

* built in objects in Python have various methods we can use
* methods a re functions built-in objects
* when we instatiate a builtin obeject type its methods are avaialable for use. for list we have seen .append() and .pop()
* in jupyter notebook i can get a list of the avaiable methods by writing the variable name . and hitting tab (i get the attributes and methods of its data type or obect type)
* after insrting the method name in jupyter tab i can hot shift+tab and get help for the method
* in normal python to get the help in console i ban wrap it all in help() e.g help(mylist.insert)
* the other option is to visit [python docs](https://docs.python.org/3/)

### Lecture 41 - Functions in Python

* functions like any other language (reusable and modular)
* syntax (use indentation to define limits)
* function name must be lowercase
* functions can take params
* we use the return keyword to send back result of the function 
* return allows to assing the outtput of the function to a new var 
```
def function_name(param):
	'''
	Dockstring explains function
	DOCKSTRING: Information about the function
	INPUT: name
	OUTPUT: Hello
	'''
	print("Hello "+param)
	return 1
# we call it
>> ret = function_name('Sakis')
>> Hello Sakis
>> print(ret)
>> 1
```

* if i just run the function name with out () python will console out info about it
* geting info on function is the same as getting info for a method (shift+tab)
* i can set default params to avoid runtime errors when i dont pass arguments. `def sy_hello(name='NAME`):
* the result of a function that does not return anything is of NoneType
* i can return if statements if i only care about the bollean result

### Lecture 42 - Overview of Quick Function Exercises 

* [solutions](https://docs.google.com/document/d/181AMuP-V5VnSorl_q7p6BYd8mwXWBnsZY_sSPA8trfc/edit)

### Lecture 43 - `*args` and `**kwargs` in Python

* `*args` stands for arguments and `**kwargs` for keyword arguments. both are special params in python functions
* they are used to pass arbitrary number of params in a function
* normally if i pass more than the specified params when i call a function it hrows an error. when i use `*args` python treats it a tuple of arbitrary size. then if i use it in my function as a tuple by calling it `args` then i cave dynamic params in the func

```
def myfunc(*args):
	return sum(args) * 0.05
```

* what python does is it takes all the param i pass in and puts them in a tuple
* i f i print the args in the function i get a tuple
* i can use any other name instead of args the * is what does the job

```
def myfunc(*args):
	for item in args:
		print(item)
```

* `**kwargs` converts input params to a dictionary and treats input params as key value pairs. param name is the key and value is the value.

```
def myfunc(**kwargs):
	if 'fruit' in kwargs:
		print('My fruit choice is {}'.format(kwargs['fruit']))
	else:
		print('I did not find any fruit here')
>> myfunc(fruit='apple', veggie='brocoli')
>> 'My fruit choice is apple
```

* we can use them in combination 

```
def myfunc(*args,**kwargs):
	print('I would like {} {}'.format(args[0],kwargs['food']))
>> myfunc(10,20,30,fruit='orange',food='eggs')
>> I would like 10 eggs
```

* python func distinguises args from kwargs , if they are named or unnamed params
* order of definition of args, kwargs must be respected

### Lecture 44 - Lamda Expressions, Map and Filter Functions

* lamda functions are anonymous functions we use one time and never reference them again
* to understand their use we talk aboud map anf filter functions
* map is a built in function. it takes a function and an iterable object. so it applies the function on each element of the iterable object

```
def square():
	return num**2
my_nums = [1,2,3,4,5]
map(square,my_nums) # this creates it does not execute. i need to iterate
for item in map(square,my_nums):
	print(item)
>> 1
>> 4
>> 9
>> 16
>> 25
```

* if i just want the list back `list(map(square,my_nums))`
* functions are passed in map by their name not as func() as we dont want them executed right away but we pass the pointer to map to execute them latrer (JS callback style)
* filter uses the same syntax as map filter(func,iterable) BUT. filter filters the iterable rturning only the elements that when passed in the function as arguments return True. so the function passed MUST return a boolean

```
def check_even(num):
	return%2 == 0
my_nums = [1,2,3,4,5,6]
filter(check_even,my_nums) # this creates it does not execute. i need to iterate or transform to a list
```

* to understand lamda functions we transform a nurmal function into a lamda

```
def square(num):
	result =  num**2
	return result
square(3)
>> 9
```
* this is equivalent to 
```
def quare(num): return num ** 2
```

* or 

```
square = lambda num: num ** 2
```

* usually we dond assign lanbdas to vars but pass it in filter or map function in one time calls `list(map(lambda num: num **2, mynums)))`

```
names = ['Andy','Eve','Sally']
list(map(lanbda name: name[0],names))
>> ['A','E','S']
# reverse names
list(map(lanbda name: name[::-1],names))
```

### Nested Statements and Scope

* when we create a variable name in python this is stored in what is called a namespace 
* variable names have a scope

```
x = 25
def printer():
	x = 50
	return x
print(x)
>> 25
print(printer())
>> 50
```

* vars defined in a function scope is the function itself
* LEGB variable rule applies (Local, Enclosing Functional, Globals and Built-Ins)
	* L: Local - Names assigned in a ny way within a function (def or lambda) and not declared global in that function
	* E: Enclosing Function locals - Names in teh local scope of any and all enclosing functions (def or lambda) from inner to outer
	* G: Global (module) - Nmaes assigned at the top-level of a module file or declared global in a def within the file
	* BL Built-in (Python) - Names preassigned in the built-in names module: open, range, SyntaxError ...
* LEGB rule is the order in which python will look for the vars

* local example `lambda num:num**2`
* enclosing function local example (after local and before global it searches in the enclosing function if there is one)
```
name = 'THIS IS A GLOBAL STRING'

def greet():
	name = 'Sammy'
	def hello():
		print('Hello'+name)
	hello()
greet()
>> Hello Sammy
```

* setting a variable in a function as global changes its scope to global. but it takes effect only if ht efunction is called
* avoid globals. pass them in the func and return them . its much cleaner and safer

### Lecture 52 - Functions and Methods - Homework Assignemnt

## Section 7 - Milestone Project - 1

### Lecture 54 - First Python Milestone Project Overview

* TicTacToe Game for 2 players

### Lecture 58 - Advanced Solution

## Section 8 - Object Oriented Programming

### Lecture 59 - OOP Introduction

* with OOP we can create our own objects that have methods and attributes
* after defining a list or string (object instantiation) we are able to call their methods with .mathod() syntax 
* theseuse info about the object or the object itself to return results or change the current object e.g append() to a list or count occurences of an element in a tuple
* syntax example:
```
class NameOfClass():
	def __init__(self,param1,param2):
		self.param1 = param1
		self.param2 = param2
	def some_method(self):
		# perform some action
		print(self.param1)
```
* a class is defined with class keyword and the name (typical camelcase) with parentheses
* then we have the contrstructor (__init__) method called when we make an instance of an object, self refers to the object instance itself (like this in JS). typically in a constructor we pass in external params that we attach to the object instance
* by passin in the method the self obejct we let python know the method is connectecd to the class.

### Lecture 60 - OOP: Attributes and Class Keyword

* by seting a variable name `mylist = [1,2,3]` i create an object literal of that type. the fact that is an object is proven if he hit shift+tab in jupiter after `mylist.` and get all the atributes and methods avaialble because of its class(aka type)

* we create an empty class, instantiate an object out of it and check the object's type with the built in type() method. it is of Sample type

```
class Sample():
	pass
my_sample = Sample()
type(my_sample)
>> __main__.Sample
```

* in the constructor i pass the params and i can assing to self. they become attributes i can call later. if i define attrributes as constructor params andd dont pass them i get an error

```
class Dog():
	def __init__(self,breed,name,spots):
		self.bree = breed
		self.name = name
		self.spots = spots
my_dog = Dog(breed='Lab',name='Sammy',spots=False)
my_dog.breed
>> 'Lab'
my_dog.name
>> 'Sammy'
my_dog.spots
>> False
```

### Lecture 61 - OOP: Class Object Attributes and Methods

*  in previous lecture we saw how a number of params can passed when creating a object instance from a class and be assigned as attributes of the object
* there are attributes common for all objects. these are class attributes same for every object instance . they are defined above the init method. for these we dont assign them to the self keyword as this refers to the object instance

```
class Dog():
	# CLASS OBJECT ATTRIBUTE
	species = 'mammal'
	my_dog = Dog(breed='Lab',name='Sammy',spots=False)
	...
```

* no need to pass it. i can get it with `my_dog.species`
* methods are function defined in the class that typically operate on object instance data. they are put after the init function and they are passed the self (object instance ref) to access it attributes and methods

```
...
	def __init__(self,breed,name,spots):
		self.bree = breed
		self.name = name
		self.spots = spots
	# Operactions/Actions --> Methods
	def bark(self):
		print("WOOF! My name is {}".format(self.name))
...
my_dog.bark()
>> 'WOOF! My name is Sammy'
```

* attributes we call them without () methods arre functions so to execute we need the ()
* methods can take external params that are passed whenb they get called, they are passed by their name no self. needed. if not passed when called python throws error

```
...
def bark(self,number):
...
```
* we write a new class to wrap up

```
class Circle():
	# CLASS OBJECT ATTRIBUTE
	pi = 3.14
	# constructor with one param defaulting to 1 to avoid runtimes
	def __init__(self,radius=1):
		self.radius = radius
		self.area  = radius*radius*Circle.pi

	# METHOD
	def get_cicumference(self):
		retun 2*pi*self.radius

my_circle = Circle()
```

* my_circel has pi.radius and get_circumference and area
* better call class attributes as Class.attribute and not just attribute

### Lecture 62 - OOP: Inheritance and Polymorphism

* inheritance is to define new classes using existing classes
* we create a sample class that will serve as base/parnet class to show inheritance

```
class Animal():
	def __init__(self):
		print("ANIMAL CREATED")
	def who_am_i(self):
		print("I am an animal")
	def eat(self):
		print("Iam eating")
myanimal = Animal()
>> ANIMAL CREATED	
myanimal.eat()
>> Iam eating
```

* i will create now dog class (derived class) inheriting or extending the animal class to inherit its methods and attibutes

```
class Dog(Animal):
	def __init__(self):
		Animal.__init__(self)
		print("Dog Created")
	def who_am_i(self):
		print("I am a dog!")
	def bark(self):
		print("Woof")
mydog = Dog()
>> ANIMAL CREATED
>> Dog Created
mydog.who_am_i()
>> I am a dog
mydog.eat()
>> I am eating
mydog.bark()
>> Woof
```

* to extend a base class i pass its name in the definition of the chiled class `def Child(Parent):`
* also int he contructor of the child i have to call the construnctor f the parent passing the object instance reference
* all methods and attributes are inherited to the child
* if i want to overrite a method i simply rewrite it using the same name

* Polymorphism refers to the way that different object classes can share the same method name. and these mathods can be called from the same place even thogh different object might be passed in (?!?!)

* example

```
# Dog Class
class Dog():
	def __init__(self,name):
		self.name = name
	def speak(self):
		return self.name + " says woof!"

# Cat Class
class Cat():
	def __init__(self,name):
		self.name = name
	def speak(self):
		return self.name + " says meow!"

niko = Dog("niko")
felix = Cat("felix")
print(niko.speak())
>> niko says woof!
print(felix.speak())
>> felix says meow!
```

* both dog class and cat class have the speak method, when called each obejts speak method returns the result that is unique to the object class. also their names are unique to the object instance(passed as params at creation)
* an exampl of polymorphism is demonstrated in a for loop. i can write common code using both of them as they share common output and commonly named methods

```
for pet in [niko,felix]:
	print(typpe(pet))
	print(pet.speak())
>> <class '__main__.Dog'>
>> niko says woof!
>> <class '__main__.Cat'>
>> felix says meow!
```

* or through a function. python does not care about the class we will pass (after all they all derive from the same root built-in class) as long as both have the method .speak

```
def pet_speak(pet):
	print(pet.speak())
pet_speak(niko)
>> niko says woof!
pet_speak(felix)
>> felix says meow!
```

* A more concrete way of polymorphism is performed using Abstract classes and inheritance
* an abstract class is one that never expects to be instantiated rather than inherited/extended

```
class Animal():
	def __init__(self,name):
		self.name = name
	def speak(self):
		raise NotImplementedError("Subclass must implement this abstract method")
myanimal = Animal("fred")
myanimal.speak()
>> ERROR..		
```

* we see that Animal although intented to be used as abstract cannot prevent it from being instationated. however when we implement abstract class methods we throw an error when called as we are not supposed to call mehtods of the abstract class. the reason for abstract methods is to form a blueprint an interface. they are meant to be overwritten by children

### Lecture 63 - OOP: Special(Magic/Dunder) Methods

* special methods allow us to use some built-in operations in python

```
mylist = [1,2,3]
len(mylist)
>>3

class Sample():
	pass

mysample = Sample()
len(mysample)
>> ERROR
print(mysample)
>> <__main__.Sample object at >
print(mylist)
[1,2,3]
```

* so i see that imy class does not inherit python built in methods where python build in classes (or datatypes) do. this is where special or magic or dunder (because they start with __ ) come to place, __init__ is such as special method:

```
class Book():
	def __init__(self,title,author,pages):
		self.author = author
		self.title = title
		seld.pages = pages
b = Book('Python Rocks', 'Jose',200)
print(b)
>> <__main__.Book object at >
```

* print asks for the string representation of b. i get the same result if i cast b into string

```
str(b)
>> <__main__.Book object at >
```

* if i overwrite the special method __str__ in Book i can overcome this issue

```
class Book():
	def __init__(self,title,author,pages):
		self.author = author
		self.title = title
		seld.pages = pages
	def __str__(self)
		return f'{self.title} by {self.author}'
b = Book('Python Rocks', 'Jose',200)
print(b)
>> Python Rocks by Jose
str(b)
>> Python Rocks by Jose
```

* i can do the same for length len()

```
def __len__(self):
	return self.pages
```

* i can delete an object with the built in del `del b`
* we can overwrite this method as well. overwriting does not remove the default behaviour of deleting though its just enhances it... (how? no call to parent inside...)

```
def __del__(self):
	print('A book object has been dleted')
```

### Lecture 64 - OOP: Homework

### Lecture 66 - OOP: Challenge

## Section 9 - Modules and Packages

### Lecture 68 - Pip install and PyPI

* PyPI is a repository for open-source 3rd party Python packages. like RubyGems, NPM for node.js
* so far we have used only libs that come with Python (standard libs)
* there are much more libs on PyPI
* we can use `pip install` at the command line to install these packages
* with python or anaconda python install we have pip. pip is a cli tool
* firewall might block pip
* in my project folder I write `pip install <package>`. seems that packages are globally available (python lloks if we have already the packlage)
* so we installl them and use them in python (check documentation)

```
pip install colorama
python
>>> from colorama import init
>>> init()
>>> from colorama import Fore
>>> print(FOore.RED + "some red text")
```

* how to search: google "python package for "=> usually =ownload link takes us to PyPI

```
pip install openpyxl
python
>>> import openpyxl
```

### Lecture 69 - Modules and Packages

* now we will learn how to write our own modules and packages
* modules  are .py scripts that we call in another .py script
* packages are a collection of .py scripts (but there is a special __init__.py script that needs to be in the folder along with the rest of the scripts to let python know that these .py scripts should be treated as a package )
* in a text editor i create a mymodule.py file and a myprogram.py that will call the module
* in mypmodule I write

```
def myfunc():
	print("Hey I am in mymodule.py")
```

* in myprogram i import the function from module and call it

```
from mymodule import myfunc

myfunc()
```

* in the folder of the files i run `python myprogram.py` and get `Hey I am in mymodule.py ` printed in console
* with modules under our belt lets go to packages. we create a MyMainPackage folder in the project dir and in it a SubPackage folder
* we need to tell python to treat these folders as packages. to do so in each package folder (main and sub) i add an __init__.py file
* we dont have to write anything in the file
* in the package and subpackage folder we add a script file/module with a dummy function
* in my main program the waty to import modules from packages is `from <Package> import <module>` or `from <Package>.<SubPackage> import <module>` . after importing i can call the module or script (we refer to the .py files in the package folder) function with `<module>.<function>()`

```
from MyMainPackage.SubPackage import mysubscript
mysubscript.sub_report()
```

### Lecture 70 - __name__ and "__main__"

* we stuble upon the follwing LoC in python scripts

```
if __name__ == "__main__":
	<block of code>
```

* sometimes when we are importing from a module we would like to know whether a modules function is being used as an import, or if we are using the  original .py file of that module
* to see this in action in a folder we add two .py files (one.py, two.py)
* when we run a .py script from command line what happen is
	* all code with no indentation gets run. there is no main function like other languages
* in python there is a built-in var called *__name__*. this var gets assigned a string depending how we run the script
	* if i run a script directly `python <script>.py` python will assign to this var the "__main__" string
* so we can add an if statement `if __name__ == "__main__":` to check if a script is being run directly
* so how it is used is that functions are defined above thsi if statement and only functions we want to run when we call this are added below this if statement (import many run few)

* we test it by implementing two files the imported and the importer
* imported

```
def func():
	print("FUNC() IN ONE.PY")

print("TOP LEVEL IN ONE")

if __name__ == '__main__':
	print('ONE.PY is beign run directly!')
else:
	print('ONE.PY has been imported!')
```

* importer

```
import one

print('TOP LEVEL IN TWO.PY')

one.func()

if __name__ == '__main__':
	print('TWO.PY is beign run directly!')
else:
	print('TWO.PY has been imported!')
```

* first test

```
python one.py
>>> TOP LEVEL IN ONE
>>> ONE.PY is beign run directly!
```

* second test

```
python two.py
>>> TOP LEVEL IN ONE
>>> ONE.PY has been imported!
>>> TOP LEVEL IN TWO.PY
>>> FUNC() IN ONE.PY
>>> TWO.PY is beign run directly!
```

* so when we import a module it gets run (top level) without __name__=="__main__"

## Section 10 - Errors and Exceptions Handling

### Lecture 71 - Errors and Exception handling

* we use error handling to plan for possible errors, let the script continue with the other code 
* unhandled errors stop the program
* we use 3 keywords for error handling:
	* try: This is the block of code to be attempted (may lead to an error)
	* except: block of code will execute if there is an error in the try block
	* finally: a final block of code to be executed regardless of an error

```
def add(n1,n2):
	print(n1+n2)
add(20,10)
>>> 30
number1 = 20
number2 = input("Please enter a num: ")
add(number1,number2)
print("Sthing happened")
>>> ERROR: number2 is a string # print is never reached and not called
```

* error handling in action. we can add else: statemnt to except: for when things go ok

```
try:
	# WANT TO ATTEMPT THIS CODE
	# MAY HAVE AN ERROR
	result = 10+10
except:
	print("Hey it looks like you aren't adding correctly!")
else:
	print("Add went well!")
	print(result)
```

* try,except and finally in action (we can except by type of error)

```
try:
	f = open('testfile','w')
	f.write("Write a test line")
except TypeError: 
	print("There was a type error!")
except OSError:
	print("Hey you have an OS Error")
except:
	print("All other exceptions")
finally:
	print("I always run")
```

* puting try/except in a while loop to get imput correclty

```
while True:
	try:
		result = int(input("Plese provide number: "))
	except:
		print("Whoops! That is not a number")
		continue
	else:
		print("Yes thank you")
		break
	finally:
		print("End of try/except/finally")
		print("I will always run at the end")
```

### Lecture 72 - Errors and Exceptions Homework

* 

### Lecture 74 - Pylint Overview

* as our projects grow its important to have unit tests in place
* as we change our code we run the test to make sure previous code is ok
* testing tools:
	* pylint: this is a library that looks at our code and reports back possible issues
	* unittest: this built-in lib will allow us to test our own programs and check we are getting desired output
* PyLint enfores PEP8 python set of style convention
* we install it with `pip install pylint`
* we create a py script file with a simple error

```
a = 1
b = 2
print(a)
print(B)
```
* we run pylint on it `pylint simple1.py` and get a report in console

```
No config file found, using default configuration
************* Module simple1
C:  4, 0: Final newline missing (missing-final-newline)
C:  1, 0: Missing module docstring (missing-docstring)
C:  1, 0: Constant name "a" doesn't conform to UPPER_CASE naming style (invalid-name)
C:  2, 0: Constant name "b" doesn't conform to UPPER_CASE naming style (invalid-name)
E:  4, 6: Undefined variable 'B' (undefined-variable)

-------------------------------------
Your code has been rated at -12.50/10
```

* for a full report i have to use the -r flag `pylint -r y simple1.py`

```
"""Example Google style docstrings.
"""
A = 1
B = 2
print(A)
print(B)

```

* 10/10

```
No config file found, using default configuration

-------------------------------------------------------------------
Your code has been rated at 10.00/10 (previous run: 7.50/10, +2.50)

```

### Lecture 75 - Running Tests with the Unittest Library

* to learn unittest we will create 2 script files. one that capitalizes strings (cap.py) and one that tests the first script using unittest lib (test_cap.py) 
* unittesting is done in a test class.
* we first implement our module to be tested (cap.py) containing a simple function that capitalizes text using the string.capitalize() method
* then we implement the test module (test_cap.py)
	* we impoer unittest library
	* we import the module to test (cap)
	* we create a class (TestCap) that extends the uniittest.TestCase class
	* in it we define our tests as methods. we add 2 tests/methods. one to test single word and one to test pultiword text.
	* the tests are structured. a) we set the method under test expected param. b) we call the method and get the result `result = cap.cap_text(text)`
	* we check if the result is what we want with parent class (TestCase) assertEqual method
	* we run the methods witht eh ifmain check and running unittest.main()

```
import unittest
import cap

class TestCap(unittest.TestCase):

	def test_one_word(self):
		text = 'python'
		result = cap.cap_text(text)
		self.assertEqual(result,'Python')

	def test_multiple_words(self):
		text = 'monty python'
		result = cap.cap_text(text)
		self.assertEqual(result,'Monty Python')

if __name__ == '__main__':
	unittest.main()
```

* we run the test with `python test_cap.py` and get the test result

```
  File "test_cap.py", line 11
    def test_multiple_words(self)
                                ^
SyntaxError: invalid syntax
achliopa@achliopa-ThinkPad-T530 ~/workspace/udemy/python/myFolder/Section10/unittest $ python test_cap.py 
F.
======================================================================
FAIL: test_multiple_words (__main__.TestCap)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "test_cap.py", line 14, in test_multiple_words
    self.assertEqual(result,'Monty Python')
AssertionError: 'Monty python' != 'Monty Python'
- Monty python
?       ^
+ Monty Python
?       ^


----------------------------------------------------------------------
Ran 2 tests in 0.001s

FAILED (failures=1)

```

* seems the capitalize() method does not word on multi word texts . we change it to the more relevant string.title() method and rerun. SUCCESS

```
..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK

```

## Section 11 - Milestone Project - 2

### Lecture 76 - Milestone Project 2 Overview

* Use OOP to create a blackjack project in python
* computer dealer and human player
* we create with anormal deck of cards represented in python
* player places a bet -> dealer starts with 1 card face up and one face down / player starts with 2 cards face up -> player goal get closer to a value of 21 than the dealer. possible player actions: hit (get another card) staty (stop receiving cards) -> after player turn: if player is over 21 is burned , if he is under 21 dealer hits untill it beats the player or gets burned, player bust money to dealer, player win/dealer bust money to player
* face values (J,K,Q) counta s 10, aces count1 or 11 whichever value is preferable to player

### Lecture 77 - Solution Walkthrough - Card and Deck classes

* we import the random module and set the globals and a boolean to control the loops
* values is a dictionary, suits and rank a tuple

```
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

playing = True
```

* we create a card class (constructor and serializer) w/ 2 params suit and rank

```
class Card():

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return self.rank + ' of ' + self.suit
```

* we create a Deck class with a list of Card class instances

```
class Deck():
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))  # build Card objects and add them to the list
    
    def __str__(self):
        deck_comp = ''  # start with an empty string
        for card in self.deck:
            deck_comp += '\n '+card.__str__() # add each Card object's print string
        return 'The deck has:' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        single_card = self.deck.pop()
        return single_card
```

* test deck

```
test_deck = Deck()
test_deck.shuffle()
print(test_deck)
```

### Lecture 78 - Solution Walkthrough - Hand and Chip Classes

* we create a Hand class. the Hand class represents which cards are at ones hands. it starts with an empty list of Cards and the list grows with add_card function
* the hand has a total value of the hands cards values. also the number of aces plays a role (to set ti 1 or 11)
```
class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
    	# card passed in
    	# from Deck.deal() --> single Card(suit,rank)
        self.cards.append(card)
        self.value += values[card.rank]
    
    def adjust_for_ace(self):
        pass
```
* testing it
```
test_deck = Deck()
test_deck.shuffle()
# Player
test_player = Hand()
# Deal 1 card from the deck
pulled_card = test_deck.deal()
print(pulled_card)
test_player.add_card(pulled_card)
print(test_player.value)
```
* we tackle the issue with aces. in add card we track the number of aces
```
class Hand:
    
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1  # add to self.aces
    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1 
```
* we create the chips class counting the money or chips
```
class Chips:
    
    def __init__(self,total=1000):
        self.total = total  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet
```

### Lecture 79 - Functions for Game Play

* we write the function to take bets
```
def take_bet(chips):
    
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except ValueError:
            print('Sorry, a bet must be an integer!')
        else:
            if chips.bet > chips.total:
                print("Sorry, your bet can't exceed",chips.total)
            else:
                break
```
* we write a function for taking hits
```
def hit(deck,hand):
    
    hand.add_card(deck.deal())
    hand.adjust_for_ace()
```
* after every hit we ask to hit or stand
```
def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    
    while True:
        x = input("Would you like to Hit or Stand? Enter 'h' or 's' ")
        
        if x[0].lower() == 'h':
            hit(deck,hand)  # hit() function defined above

        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            playing = False

        else:
            print("Sorry, please try again.")
            continue
        break
```
* we write a set of outcome helper function
```
def player_busts(player,dealer,chips):
    print("Player busts!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Dealer busts!")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.lose_bet()
    
def push(player,dealer):
    print("Dealer and Player tie! It's a push.")
```
* and more helper functions
```
def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])  
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)
```
* and the main game control function
```
while True:
    # Print an opening statement
    print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
    Dealer hits until she reaches 17. Aces count as 1 or 11.')
    
    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
            
    # Set up the Player's chips
    player_chips = Chips()  # remember the default value is 100    
    
    # Prompt the Player for their bet
    take_bet(player_chips)
    
    # Show cards (but keep one dealer card hidden)
    show_some(player_hand,dealer_hand)
    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck,player_hand) 
        
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand,dealer_hand)  
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break        


    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17 
    if player_hand.value <= 21:
        
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)    
    
        # Show all cards
        show_all(player_hand,dealer_hand)
        
        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)

        else:
            push(player_hand,dealer_hand)        
    
    # Inform Player of their chips total 
    print("\nPlayer's winnings stand at",player_chips.total)
    
    # Ask to play again
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
    
    if new_game[0].lower()=='y':
        playing=True
        continue
    else:
        print("Thanks for playing!")
        break
```
## Section 12 - Python Declarators

### Lecture 81 - Decorators with Python Overview

* decorators allow us to decorate a function
* imagine a simple func
* say we want to add new logic to the function
* we have 2 options: add the extra code into the old function (i cannot call the old function), create a new function that contains the old code and add new code there (code duplication)
* what if we want to remove the extra functionality one day.
*  an on/off switch to add/remove extra functionality would be optimal
* decorators offer that. the use the @ operator and are placed on top of the original function. it is pretty abstract. we will build a decorator to see it in action

```
def hello():
	return "Hello!"
hello()
>>> "Hello!"
hello
>>> <function __main__.hello>
greet = hello
greet()
>>> "Hello!"
del hello
hello()
>> ERROR
greet()
>>> "Hello!"
```

* so copying a func name makes a new copy of the function is not just a pointer. i can use that to return functions from inside other functions. this is useful to overcome the scope limitetion of function emclosed functions

```
def heelo(name='Jose'):
	print('The hello() function has been executed!')

	def greet():
		return '\t This is the greet() func inside hello!'
	def welcome():
		return '\t This is the welcome() func inside hello!'

	print("I am going to return a function!")

	if name == 'Jose':
		return greet
	else:
		return welcome
my_new_func = hello('Jose')
>>> The hello() function has been executed!
>>> I am going to return a function!
my_new_func
>>> <function __main__.hello.<locals>.greet>
print(my_new_func())
>>>		This is the greet() func inside hello!
```

* we see that my_new_funct points to the greet fucntion inside hello
* we will use this concept in decorators. instead of exporting (returning the function we import it, pass it as a aparameter. we define a function that gets another function as an arguemnt and executes it. we call it passing in an existing function and see it executed. NOTE we pass in raw function not with ()

```
def hello():
	return 'Hi Jose!'

def other(some_def_fuc):
	print("Other code runs here!")
	print(some_other_func())

other(hello)
>>> Other code runs here!
>>> Hi Jose!
```

* decorator (we implement both import and export) we get a function wrap it up and send the wrapped function

```
def new_decorator(original_func):

	def wrap_func():
		
		print("Some extra code, before the originam function")

		original_func()

		print("Some extra code, after the original function")

	return wrap_func

def func_needs_decorator():
	print("I want to be decorated")

decorated_func = new_decorator(func_needs_decorator)
decorated_func()
>>> Some extra code, before the originam function
>>> I want to be decorated
>>> Some extra code, after the original function
```

* instead of the traditional way of wrapping and executing i can use the operator decorator and execute the wrapped func. if i remove the operator i dont have wrapping.

```
@new_decorator
def func_needs_decorator():
	print("I want to be decorated")

func_needs_decorator()
>>> Some extra code, before the originam function
>>> I want to be decorated
>>> Some extra code, after the original function
```

## Section 13 - Python Generators

### Lecture 83 - Generators with Python

* we ve learned how to create function with def and return statement
* generator functions allow us to write a func that can send back a value and later pick up where it left off
* generator func let us generate sequence of nums over time
* the difference in syntax is the yield statement
* generateor func when compiled becomes an object that supports an iteration protocol
* when they are called they dont just return a value and exit
* generator functions automatically suspend and resume execution and state at last point of val generation
* instead of having to compute an entire series of values upfront genrator computes one val and waits untill next val is called for
* e.g the range() func does not produce a list in memory for all the vals. it keeps track of the last number and the step size to provide a flow of nums. if i indeed need a list i need to cast the range to a list.

```
def create_cubes(n):
	result = []
	for x in range(n):
		result.append(x**3)
	return result
create_cubes[10]
>>> [1,8,27,64,125,216,343,512,729]
```

* in previous example i want the whole list so the code makes sense. but if i want to iterate through the results, there is no reason to store the complete list upfront. generators  come into play. i need prev value and the formula

```
for x in create)cubes(10):
	print(x)
>>> 0
>>> 1
>>> 8
>>> 27
>>> 64
>>> 125
>>> 216
>>> 343
>>> 512
>>> 729
```

* using yield has the same result like before. but i cannot just call the func i need to use it in a loop. it is much more mem efficient

```
def create_cubes(n):
	for x in range(n):
		yield x**3
```

* if i just call `create_cubes(10)` i get `<generator object create_cubes at )x00004324>` to get the list i need to cast it to a list `list(create_cubes(10))`

* this concept is good for math series

```
def gen_fibon(n):
	a = 1
	b = 1
	for i in range(n):
		yield a
		a,b = b,a+b # tuple matching , avoid reassign a,b while they are worked with
for number in gen_fibon(10)
	print(number)
1
1
2
3
5
8
13
21
34
55
```

* i can apply built in methods on generators like next()

```
def simple_gen():
	for x in range(3):
		yield x
g = simple_gen()
next(g)
>> 0
next(g)
>> 1
next(g)
>> 2
next(g)
>> EROOR StopInteration # For loop catches this error and stops lopp
```

* iter() lets us iterate in a normal object

```
s = "Hello"
next(s)
>>> ERROR not an iterator
s_iter = iter(s)
next(s_iter)
H
```

* generators support comprehension like list comprehension

## Section 15 - Advanced Python Modules

### Lecture 87 - Collections Module - counter

* built-in that implements specialized container datatypes
* Counter is a dictionary subclass that helps count hashable objects

```
# Counter
from collections import Counter
l = [1,1,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5]
Counter(l)
>>> Counter({1: 6, 2: 4, 3: 4, 4: 4, 5: 2})
```

* as we see if we pass in a list, it creates a counter object wrapping a dictionary  with key value pairs. the keys are the list elements and the values the num of occurences of the elements in the list. this can work on strings

```
s = 'wterwtsfgtrewuioyteoiuygkhvdskjhfggjhkloituvdnjd'
Counter(s)
>>> Counter({'d': 3,
         'e': 3,
         'f': 2,
         'g': 4,
         'h': 3,
         'i': 3,
         'j': 3,
         'k': 3,
         'l': 1,
         'n': 1,
         'o': 3,
         'r': 2,
         's': 2,
         't': 5,
         'u': 3,
         'v': 2,
         'w': 3,
         'y': 2})
```

* we can also count word occurences in a sentence. the drill is obvious. apply string.split() to make an array of substrings (words and apply counter on it)
* Counter supports a number of methods `Counter.most_common(how_many_from_top)` returns the top scorers in tuples
* .sum(Counter.values()) gives the total values of occurences. (original list length) so we can derive metrics from it.
* we can cast the Counter to the standard datatypes

### Lecture 88 - Collections Module - defaultdict

* is a dicitionary like object providing all its methods and takes the first argument as the default datatype. defaultdict will never raise a KeyError. any key that does not exist, gets the value freom the defualt factory

```
from collections import defaultdict
d = {'k1':1}
d['k1']
>> 1
d['k2']
>> KeyError
# with defaultdict
d = defaultdict(object)
d['one']
>>> <object at 0x434344>
for item in d:
	print item
>> one
# its added
```

* in the prev example i set the defaultkey to the object type. so whenever i ask for a nonexisting key it gets created with the default type (object) and a reference to it is returned
* i can use defaultdict to assign default vals

```
d = defaultdict(lambda: 0)
d['one']
>> 0
# i alwys can assign my pref val as standard dict
d['two'] = 2
d
>> defaultdict(<function <lambda> at 0x43453>, {'two': 2, 'one': 0})
```

### Lecture 89 Collections Module - OrderedDict

* an OrderedDict is a dictioanry subclass that remembers the order in which its contents are added. a standard dict is an unordered collection

```
# normal dict
d = {}
d['a']=1
d['b']=2
d['c']=3
d
>> {'a':1,'b':2,'c':3}
for k,v in d.items():
	print k,v
>> a 1
>> c 3
>> b 2 # no order

# OrderedDict
from collections import OrderedDict
d = OrderedDict()
d['a']=1
d['b']=2
d['c']=3
for k,v in d.items():
	print k,v
>> a 1
>> b 2
>> c 3 # order is retained
```

* boolean expressions on dictionaries return True regardless of orrder. in ordered ones return False unless order is same

### Lecture 90 - Collections Module - namedtuple

* tuples are ordered 

```
t = (1,2,3)
t[0]
>> 1
```

* a named tuple assigns names apart from the indices to the tuple elements
* namedtuple creation is like a standard class creation. the tupleinstances i create with this datatype are like constarined  objects from a class object. the named tuple ahas the 2 basic tuple methods

```
from collections import namedtuple
Dog = namedtuple('Dog', 'age breed name')
sam = Dog(age=2,breed='Lab',name='Sammy')
sam
>> Dog(age=2,breed='Lab',name='Sammy')
sam.age
>> 2
sam[0]
>> 2
```

### Lecture 91 - Datetime

* module to handle dates in python
* we go through the time attribute

```
import datetime
t = datetime.time(5,25,1) # time takes (hours,minutes,seconds,microsecond,timezone info)
print t
>> 05:25:01
t.hours
>> 5
print datetime.time.min
00:00:00
print datetime.time.max
23:59:59.999999
print datetime.time.resolution
00:00:00.000001
```

* now we go to the date attribute

```
today = datetime.date.today()
print today
>> 2018-04-24
today.timetuple() # like a named tuple
>> time.struct_time(tm_year=2018,tm_mon=04 etc)
datetime.date.min
>> datetime.date(1,1,1)
print datetime.date.min
1-1-1
print datetime.date.max
>> 9999-12-31
print datetime.date.resolution
1 day, 0:00:00
```

* i can create dates replacing attributes of an existing date
* aalso i can do math on them

```
d1 = datetime.date(2018,4,16) (year,month,day)
d2 = d1.replace(year=1990)
print d2
>> 1990-04-16
```

```
d1-d2
datetime.timedelta(9131) # days diff
```

### Lecture 92 - Python Debugger - pdb

* intreoduces interactive debugger module

```
import pdb
x = [1,3,4]
y = 2
z = 3

result = y + z
print result
>> 5
pdb.set_trace()
result2 = y+x
print result2
>> TypeError
```

with pdb we set traces `pdb.set_trace()` (breakpoints)
* When i run the program and it passes the breakpoint it enters the pdb and i get console line (pdb cli) toenter pdb commands
* interacting with the pdb debugger, q for quit

```
(Pdb) x
[1,3,4]
(Pdb) y
2
(Pdb)x+z
TypeError
q
```

### Lecture 93 - Timeing our code -timeit

* profiling, performance metrics 
* jupyter notebook supports special methods `%timeit` for this module

```
import timeit
# want to time different methods to create the string '0-1-2-3-4...99'
"-".join(str(n) for n in range(100))
>> '0-1-2-3-4...99'
timeit.timeit(' "-".join(str(n) for n in range(100)) ',number=10000)
0.247889
```

* what i did is i passed my code a s a sting to the timeit method and entered a number=10000 that is i want to run it 10000 times to get my metrics. what i get is the time it took to execute
* i run it as list comprehension and get faster time

```
timeit.timeit(' "-".join([str(n) for n in range(100)]) ',number=10000)
0.217889
```

* i use the map function which is the fastest

```
timeit.timeit(' "-".join(map(str,range(100))) ',number=10000)
0.1554765476
```

* in jupyter i use jupyters buil-in magic aka the % symbol, jupyter reduces the number of loops the more time our code consumes to run

```
%timeit "-".join(map(str,range(100)))
10000 loops, best of 3: 15.5 μs per loop
```

### Lecture 94 - Regular Expressions -re

* text matching patterns, described with formal syntax.
* they are used for finding repetition,matching text etc
* a lot of parsing problems can be solved with regex
* we use the "re" module
* searching for patterns in text

```
import re
re.search('hello','hello world!')
>> <_sre.SRE_Match at 0x41d5648>
```

* se.search(term,text) swearches for a term in text and returns a Match object, if nothing is found, None is returned

```
import se
patterns = ['term1','term2']
text = 'This is a string wi th term1, but not the other term'
for pattern in patterns:
    print('Searching for "%s" in:\n "%s"\n' %(pattern,text))
    
    #Check for match
    if re.search(pattern,text):
        print('Match was found. \n')
    else:
        print('No Match was found.\n')
>>
>>
match.re.search(patterns[0],text)
type(match)
>> _sre.SRE_Match
match.start()
>> 22
```

* we will look deeper in the *_sre.SRE_Match* object. it contains various methods. start() returns the index of first occurence in the string , end() the last match index
* we can split with regex, the example below is like normal split (nothing fancy)

```
split_term = '@'
phrase  = 'What iis your email, is it hello@gmail.com?'
re.split(split_term,phrase)
>> ['What is your email, is it hello', 'gmail.com?']
```

* we can find all occurencies with findall

```
re.findall('match','Here is one match, here is another match')
>> ['match','match']
```

* NOw we dive into normal Regex syntax
* repetition syntax
	* `'sd*'` s followed by 0 to n d's
	* `'sd+'` s followed by 1 to n d's
	* `'sd?'` s followed by 0 to 1 d's
	* `'sd{3}'` s followed by 3 d's
	* `'sd{2,3}'` s followed by 2 to 3 d's
* character sets (match anyone of a group of chars at a point in the input). we use brackets
	* `'[sd]'` match either s or d
	* `'s[sd]+'` match s   followed by 1 to n  s or d
* exclusion: use ^ to exclude terms by insering it to the brackewt syntax notation
	* `'[^...]'` match any char not in the brackets
	* `'[^!.? ]+'` match any char not in the !.! group 1 or more (find the words)
* character ranges: contiguous chars with - start-end
	* `'[a-z]+'` sequences of lower case letters
	* `'[A-Z]+'` sequences of upper case letters
	* `'[a-zA-Z]+'` sequences of lower or upper case letters
	* `'[A-Z][a-a]+'` sequences of lower upper case letters folowed by lower case letters
* escape codes
	* `r'\d+'` sequence of a digit
	* `r'\D+'` sequence of a non-digit
	* `r'\s+'` sequence of whitespace
	* `r'\S+'` sequence of non-0withespace
	* `r'\w+'` sequence of alphanumeric
	* `r'\W+'` sequence of non-alphanumeric

### Lecture 95 - StringIO

* StringIO module implements an in-memory file like object.  it can be used as input-output to most funcs that would expect a standard file object

```
import StringIO
f = StringIO.StringIO('this is a normal string')
f.read() # cursor moved to ewnd by write
''
f.write('second line')
f.seek(0)
f.read()
```

* we can perfoirm normal file operations
* cStringIO() method is faster, impleemtned in C

## Section 16 - Advanced Python Objects and Data Structures

### Lecture 97 - Advanced Numbers

* different representations
	* Hex `hex(246) => '0xf6'` returns string
	* Binary `bin(1234) => '0b10011010010'` returns string
* built in methods.
	* pow = power `pow(2,4) => 16` third argument is mod % of result
	* abs = absolute val `abs(-3) => 3`
	* round `round(4.6) => 5.0` returns float. rounded num decimals are defined with a second arguemnt

### Lecture 98 - Advanced Strings

* different methods supported as built in to String class

```
s = 'hello world'
s.capitalize()
>> 'Hello world'
s.upper()
>> 'HELLO WORLD'
s.lower()
>> 'hello world'
s.title()
>> 'Hello World'
s.count('o') # count occurences of char
>> 2
s.find('o') # index of first occurence
>> 4
```

* formating methods - weird

```
s.center(20,'z') # center string and add padding of given char(s) to a total length of 20
>> 'zzzzhello worldzzzzz'
```

```
print 'hello\thi'
>> hello   hi
print 'hello\thi'.expandtabs()
>> hello   hi
```

* .isalnum() checks if all chars in a string are alphanumeric
* .isalpha() checks if all chars in a string are alphabetic
* .islower() checks if all chars in a string are  lower case
* .isspace() checks if all chars in a string are  whitespace
* .istitle() checks if all words in a string are capitalized
* .endswith('o') checks if last char is string is 'o'

* certain methods emulate regex functionality like .split()

```
s = 'hello'
s.split('e') # it seperates at every occurence
['h','llo']
```

* .partition() is like split() splits at first occurence and includes thje split char in the string array

```
s = 'weereeeeetrtt'
s.partition('e')
>> ['w','e','ereeeeetrtt']
```

### Lecture 99 - Advanced Sets

```
s = set()
s.add(1)
s.add(2)
s
>> {1,2}
s.add(2)
s
{1,2} # sets do not accept duplicates
```

* .clear() clears all elemetns from the set
* .copy() makes a copy of the set `sc = s.copy()`. changes done to the original do not affect the copy
* .difference() returns a set containign the elements that are different between 2 sets `set1.difference(set2)`
* .difference_update() removes the elemetns found to be same between 2 sets from the 1st set. `set1.difference_update(set2)`
set1
* .discard() removes an element from a set `s.discard(2)`
* .intersection() returns the intersection of 2 sets as a new set (common elements between 2 sets) `set1.intersection(set2)`
* .intersection_update() updates the first set to contain only common eleemtns with second set `set1.intersection_update(set2)`
* .isdisjoint() return true if 2 sets have no eleemtns in common, otherwise returns false `set1.isdisjoint(set2)`
* `s1.issubset(s2)` returns true if s1 is subset of s2
* `s1.issuperset(s2)` returns true if s1 is superset of s2
* `s1.symmetric_difference(s2)` returns the elements that exist in only one of the sets
* `s1.symmetric_difference_update(s2)` method updates s1 to contain the elemetns that exist in only one of the sets
* `s1.union(s2)` returs the union of the two sets (all elements that are in either set)
* `s1.update(s2` updates s1 to contain the union of the 2 sets

### Lecture 100 - Advanced Dictionaries

```
d = {'k1':1,'k2':2}
```

* dictionaries have their own comprehensions like lists

```
{x:x**2 for x in range (10)}
>> {0: 0, 1: 1, 2: 4, 3: 9, 4:16  ... 9: 81}
```

* if we want to set string keys we can do it with zio

```
{k:v**2 for k,v in zip(['a','b'], range (2))} # use tuple unpacking
>> {'a': 0, 'b': 1}
```

```
for k in d.itervalues(): # or iteritems() or interkeys()
	print k
>> 1
>> 2
```

### Lecture 101 - Advanced Lists

* `list.append(value)` appends a value to a list
* `list.count(value)` counts value occurences in list
* `list1.apend(list2)` apeends nested list 2 in list1
* `list1.extend(list2)` appends list2 elemetns to list1
* `list.index(eleemnt)` returns index of element (eeror if eleemtn not found)
* `list.insert(index,value)` inseerts value at specified index position int he list
* `list.pop(index)` pops out the value at index position. if index not sepcs returns last one
* `list.remove(value)` removes the first occurenc of the value in the list
* `list.reverse()` reverses thelist
* `list.sort()` sorts the list

## Section 17 - Bonus Material - Introduction to GUIs

### Lecture 104 - Introduction  to GUIs

* [common GUI frameworks](https://wiki.python.org/moin/GUI%20Programming%20in%20Python)
* [full GUI programming list](https://wiki.python.org/moin/GuiProgramming)
* we will use Widgets in Jupyter Notebook. this is good for dashboareds for business/data analysis
* jpywidgets switched to bootstrap [jpywidgets](https://ipywidgets.readthedocs.io/en/latest/examples/Widget%20Styling.html#Predefined-styles)

### Lecture 106 - Interact Functionality with GUIs

* we can build simple graphical user interfaces (GUI) with jupyter
* to use widgets in jypyter we need to import libraries
```
from  ipywidgets import interact,interactive, fixed
import ipywidgets as widgets
```
* we implement a basic function for our first widget
```
def func(x):
	return x
```
* we create a slider witn interact passing in the function and a default value
```
interact(func,x=10)
```
* the function determines the output value of the slider
* if i pass a boolean as default i get a checkbox `interact(func,x=True)` that is checked by default and returns true, by interacting i toggle the output between true/false
* if I pass a string as a second argument int eh interact function ai get a text field. whatever i type is outputed
* we will now use a decorator to wrap a function in the interact method. what I get is 2 UI elements a checkbox and a slider
```
@interact(x=True,y=1.0)
def g(x,y):
	return (x,y)
```
* if i want to fix a parameter to a certain value and disable it interact element i can use fixed method in the inetract arguments
```
@interact(x=True,y=fixed(1.0))
def g(x,y):
	return (x,y)
```
* if we look closer to the integer slider we see that its range is determined by the value we pass as second param. with min = -x and max = 3x
* we can parametrize that with widgets.Intslider() for ints bassing a kward (key value pairs) for the predefined params. `interact(func,x=widgets.IntSlider(min=-100,max=100,step=1,value=0))`
* there is a shorthand version for this `interact(func,x=(-100,100,1))`
* we can add this parametrization to the decorator
```
@interact(x=(0.0,20.0,0.5))
def h(x=5.0):
	return x**0.5
```
* if we pass in interact a list of strings as default val it will createa drop down list
* we can pass also a dictionary . it creates a dropdown list. we select the key and the output is the val
* jypyter widgets provide the interactive method. this method allows us to reuse widgets that are already produces or access the data bound to the UI controls
* in contrast with interact the output value is not dispalyed automatically. we can display it in a function using IPython.display
* we need to import display form IPython.display
```
from IPython.display import display

def f(a,b):
	display(a+b)
	return a+b
w = interactive(f,a=10,b=20)
```

* w is reusable. it has a type of `ipywidgets.widgets.interaction.interactive` and contains the widgets as its children. we can display it calling `display(w)` . we can get the current values of its input with `w.kwargs` as a dictionary and the output with `w.result`

```
type(w)
>> ipywidgets.widgets.interaction.interactive
w.children
>> (IntSlider(value=10, description='a', max=30, min=-10),
 IntSlider(value=20, description='b', max=60, min=-20),
 Output())
display(w)
>> widget on screen
```

### Lecture 107 - GUI Widget Basics

* we will build upon prior knowledge
* we import widgets
```
import ipywidgets as widgets
```
* widgets have lots of methods and attributes
* if i call `widgets.IntSlider()` i get a slider onscreen with predefined default vals 
* if i dont want to  display the widget directly but later on when i want to i store it to a var an later use display(var)

```
import ipywidgets as widgets
w = widgets.IntSlider()
from IPython.display import display
display(w)
```

* if i rediplay the same widget variable any interaction to one affects the other as they are the same thing (python is pass by reference language)
* to close the widget we write `w.close()`
* the var w (widget) has a number of attrigutes and methods. `w.value` gives the current val of the slider (not updatable)
* widgets have *keys* or stateful properties. properties connected tot he state of the display change the display programmaticaly
* we can connect multiple widgets using jslink (javascript link). the connection is doen between keys which we represent as strings in tuples (first element is the widget). the link is done after display

```
a = widgets.FloatText()
b = widgets.FloatSlider()
display(a,b)
mylink = widgets.jslink((a,'value'),(b,'value'))
```

* i can break the link with .unlink() `mylink.unlink()`

### Lecture 108 - List of Possible Widgets

* notebook contains the complete list. to view it run the script in jupyter

```
import ipywidgets as widgets

# Show all available widgets!
for item in widgets.Widget.widget_types.items():
    print(item[0][2][:-5])
```

* IntSlider (we've seen) properties list

```
widgets.IntSlider(
    value=7,
    min=0,
    max=10,
    step=1,
    description='Test:',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True,
    readout_format='d'
)
```

* FloatSlider has same properties (vals have decimals, format is '.1f')
* sliders can be displayed verticaly
* IntRangeSlider and FLoatRangeSlider support range (same params just value is passed as array of 2)
* IntProgress is like a progress bar (is from bootstrap)
* BoundedFloatText BoundedFloatText +. numerical text boxes with limits
* ToggleButton, Chackbox
* Selection Widgets => Dropdown, RadioButtons Select etc
* toggle buttons, select multiple
* HTML => enter HTMl
* Image (show image)

### Lecture 109 - Widget Styling and Layouts

* how to style widgets (we use html,css terms)
* .layout. gives a big list of css properties

```
import ipywidgets as widgets
from IPython.display import display
w = widgets.IntSlider()
w.layout.margin = 'auto'
w.layout.height = '75px'
```

* layout can be copied between widgets
* `widgets.Button(description=`Ordinary Button',button_style='danger')
* layout exposes layout CSS properties for top level elements
* style exposes non layout related attributes (custom colors)
```
b1 = widgets.Button(description='Custom Color')
b1.style.button_color = 'lightgreen'
```

* b1.style.keys returns all stuyles to be edited (varies per widget). styles can be copied

### Lecture 110 - Example of what a Widget can do

* we will create acustom widget (we will need external libraries)
* we will explore the LOrenz sustem of diff equations
* `%matplotlib inline`  allows us to view the visualizations in  the jupyter notebook
* we import methods from IPython.display and widgets

```
from ipywidgets import interact, interactive
from IPYthon.display import creal_output, display, HTML
```

* we import tools from external librarties, matplotlib is for plotting

```
import numpy as np
from scipy import integrate

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import cnames
from matplotlib import animation
```

* we implement the lorenz equation passing the required params
	* it creates a figure
	* sets the limits of the figure
	* computes the time derivative
	* select random starting point
	* solve the equation
	* choose colors for lines
	* plots everything
* we call interactive on the func tweaking the imput params 
* we make histograms