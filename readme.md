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

* 