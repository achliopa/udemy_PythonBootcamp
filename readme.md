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