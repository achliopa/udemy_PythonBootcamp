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

* 