# **HOWTO Setup a Jupyter Notebook**
###### Last update: 23/8/21 dbe - final v1

### Summary

The purpose of this [Jupyter Notebook](http://jupyter.org/) is to get
you started using Python and Jupyter Notebooks for routine chemical
engineering calculations. This introduction assumes this is your first
exposure to Python or Jupyter notebooks.

## Step 1: Gain Executable Access to Jupyter Notebooks

Jupyter notebooks are documents that can be viewed and executed inside
any modern web browser. Since you're reading this notebook, you already
know how to view a Jupyter notebook. The next step is to learn how to
execute computations that may be embedded in a Jupyter notebook.

To execute Python code in a notebook you will need access to a Python
kernal. A kernal is simply a program that runs in the background,
maintains workspace memory for variables and functions, and executes
Python code. The kernal can be located on the same laptop as your web
browser or located in an on-line cloud service.

**Important Note Regarding Versions** There are two versions of Python
in widespread use. Version 2.7 released in 2010, which was the last
release of the 2.x series. Version 3.5 is the most recent release of the
3.x series which represents the future direction of language. It has
taken years for the major scientific libraries to complete the
transition from 2.x to 3.x, but it is now safe to recommend Python 3.x
for widespread use. So for this course be sure to use latest verstion,
currently 3.6, of the Python language.


### 1.1 Using Jupyter/Python in the Cloud

The easiest way to use Jupyter notebooks is to sign up for a free account on a cloud-based service such as
**[Google Colab](https://colab.research.google.com/)** or
[Kaggle](https://www.kaggle.com/code). You will need continuous
internet connectivity to access your work, but the advantages are there
is no software to install or maintain. All you need is a modern web
browser on your laptop, Chromebook, tablet or other device. Note that
the free services are generally heavily oversubscribed, so you should
consider a paid account to assure access during prime hours.

There are also demonstration sites in the cloud, such as
[tmpnb.org](https://tmpnb.org/). These start an interactive session
where you can upload an existing notebook or create a new one from
scratch. Though convenient, these sites are intended mainly for
demonstration and generally quite overloaded. More significantly, there
is no way to retain your work between sessions, and some python
functionality is removed for security reasons.


### 1.2 Installing Jupyter/Python on your Laptop

For regular off-line use you should consider installing a Jupyter
Notebook/Python environment directly on your laptop. This will provide
you with reliable off-line access to a computational environment. This
will also allow you to install additional code libraries to meet
particular needs.

Choosing this option will require an initial software installation and
routine updates. For this course the recommended package is
[Anaconda](https://store.continuum.io/cshop/anaconda/) available from
[Continuum Analytics](http://continuum.io/). Downloading and installing
the software is well documented and easy to follow. Allow about 10-30
minutes for the installation depending on your connection speed.

After installing be sure to check for updates before proceeding further.
With the Anaconda package this is done by executing the following two
commands in a terminal window:

    > conda update conda
    > conda update anaconda

Anaconda includes an 'Anaconda Navigator' application that simplifies
startup of the notebook environment and manage the update process.


## Step 2: Start a Jupyter Notebook Session

### 2.1 Using a cloud-based Service  
If you are using a cloud-based service a Jupyter session will be started
when you log on.

When you are accessing yor **Collaboratory Account** with opening a notebook file (e.g."Willkommen bei Collaboratory") you should see a browser
window like this:

![Screen Shot Jupyter Session](figures/Screen-Shot-Colab-Google-Session.jpg)
   
### 2.2 Using a local Installation    
If you have installed a Jupyter/Python distribution on your laptop then
you can open a Jupyter session in one of two different ways:

  - Use the Anaconda Navigator App, or

  - open a terminal window on your laptop and execute the following
    statement at the command line:
    
    ``` 
      > jupyter notebook
    ```

And when you have opened a session you should see a browser
window like this:

![Screen Shot Jupyter Session](figures/Screen-Shot-Jupyter-Session.png)

At this point the browser displays a list of directories and files. You
can navigate amoung the directories in the usual way by clicking on
directory names or on the 'breadcrumbs' located just about the listing.

Jupyter notebooks are simply files in a directory with a `.ipynb`
suffix. They can be stored in any directory including Dropbox or Google
Drive. Upload and create new Jupyter notebooks in the displayed
directory using the appropriate buttons. Use the checkboxes to select
items for other actions, such as to duplicate, to rename, or to delete
notebooks and directories.

  - select one of your existing notebooks to work on,
  - start a new notebook by clicking on the `New Notebook` button, or
  - import a notebook from another directory by dragging it onto the
    list of notebooks.

An IPython notebook consists of cells that hold headings, text, or
python code. The user interface is relatively self-explanatory. Take a
few minutes now to open, rename, and save a new notebook.

Here's a quick [video overview](https://youtu.be/HW29067qVWk) of Jupyter notebooks.


## Step 3: Simple Calculations with Python  

Python is an elegant and modern language for programming and problem
solving that has found increasing use by engineers and scientists. In
the next few cells we'll demonstrate some basic Python functionality.


### 3.1 Example: Basic Arithmetic Operations

Basic arithmetic operations are built into the Python langauge. Here are
some examples. In particular, note that exponentiation is done with the
\*\* operator.

``` python
a = 12
b = 2

print(a + b)
print(a**b)
print(a/b)
```

<div class="output stream stdout">

    14
    144
    6.0

</div>


### 3.2 Example: Python Libraries

The Python language has only very basic operations. Most math functions
are in various math libraries. The `numpy` library is convenient
library. This next cell shows how to import `numpy` with the prefix
`np`, then use it to call a common mathematical functions.

</div>

<div class="cell code" data-execution_count="3" data-nbpages="{&quot;link&quot;:&quot;[1.1.4.2 Python Libraries](https://jckantor.github.io/CBE30338/01.01-Getting-Started-with-Python-and-Jupyter-Notebooks.html#1.1.4.2-Python-Libraries)&quot;,&quot;level&quot;:3,&quot;section&quot;:&quot;1.1.4.2 Python Libraries&quot;}">

``` python
import numpy as np

# mathematical constants
print(np.pi)
print(np.e)

# trignometric functions
angle = np.pi/4
print(np.sin(angle))
print(np.cos(angle))
print(np.tan(angle))
```

<div class="output stream stdout">

    3.141592653589793
    2.718281828459045
    0.707106781187
    0.707106781187
    1.0

</div>

</div>

<div class="cell markdown" data-nbpages="{&quot;link&quot;:&quot;[1.1.4.3 Working with Lists](https://jckantor.github.io/CBE30338/01.01-Getting-Started-with-Python-and-Jupyter-Notebooks.html#1.1.4.3-Working-with-Lists)&quot;,&quot;level&quot;:3,&quot;section&quot;:&quot;1.1.4.3 Working with Lists&quot;}">
    
### 3.3 Example: Working with Lists

Lists are a versatile way of organizing your data in Python. Here are
some examples, more can be found on [this Khan Academy
video](http://youtu.be/zEyEC34MY1A).

</div>

<div class="cell code" data-execution_count="4" data-nbpages="{&quot;link&quot;:&quot;[1.1.4.3 Working with Lists](https://jckantor.github.io/CBE30338/01.01-Getting-Started-with-Python-and-Jupyter-Notebooks.html#1.1.4.3-Working-with-Lists)&quot;,&quot;level&quot;:3,&quot;section&quot;:&quot;1.1.4.3 Working with Lists&quot;}">

``` python
xList = [1, 2, 3, 4]
xList
```

<div class="output execute_result" data-execution_count="4">

    [1, 2, 3, 4]

</div>

</div>

<div class="cell markdown" data-nbpages="{&quot;link&quot;:&quot;[1.1.4.3 Working with Lists](https://jckantor.github.io/CBE30338/01.01-Getting-Started-with-Python-and-Jupyter-Notebooks.html#1.1.4.3-Working-with-Lists)&quot;,&quot;level&quot;:3,&quot;section&quot;:&quot;1.1.4.3 Working with Lists&quot;}">

Concatentation is the operation of joining one list to another.

</div>

<div class="cell code" data-execution_count="5" data-nbpages="{&quot;link&quot;:&quot;[1.1.4.3 Working with Lists](https://jckantor.github.io/CBE30338/01.01-Getting-Started-with-Python-and-Jupyter-Notebooks.html#1.1.4.3-Working-with-Lists)&quot;,&quot;level&quot;:3,&quot;section&quot;:&quot;1.1.4.3 Working with Lists&quot;}">

``` python
# Concatenation
x = [1, 2, 3, 4];
y = [5, 6, 7, 8];

x + y
```

<div class="output execute_result" data-execution_count="5">

    [1, 2, 3, 4, 5, 6, 7, 8]

</div>

</div>

<div class="cell markdown" data-nbpages="{&quot;link&quot;:&quot;[1.1.4.3 Working with Lists](https://jckantor.github.io/CBE30338/01.01-Getting-Started-with-Python-and-Jupyter-Notebooks.html#1.1.4.3-Working-with-Lists)&quot;,&quot;level&quot;:3,&quot;section&quot;:&quot;1.1.4.3 Working with Lists&quot;}">

Sum a list of numbers

</div>

<div class="cell code" data-execution_count="6" data-nbpages="{&quot;link&quot;:&quot;[1.1.4.3 Working with Lists](https://jckantor.github.io/CBE30338/01.01-Getting-Started-with-Python-and-Jupyter-Notebooks.html#1.1.4.3-Working-with-Lists)&quot;,&quot;level&quot;:3,&quot;section&quot;:&quot;1.1.4.3 Working with Lists&quot;}">

``` python
np.sum(x)
```

<div class="output execute_result" data-execution_count="6">

``` 
10
```

</div>

</div>

<div class="cell markdown" data-nbpages="{&quot;link&quot;:&quot;[1.1.4.3 Working with Lists](https://jckantor.github.io/CBE30338/01.01-Getting-Started-with-Python-and-Jupyter-Notebooks.html#1.1.4.3-Working-with-Lists)&quot;,&quot;level&quot;:3,&quot;section&quot;:&quot;1.1.4.3 Working with Lists&quot;}">

An element-by-element operation between two lists may be performed with

</div>

<div class="cell code" data-execution_count="7" data-nbpages="{&quot;link&quot;:&quot;[1.1.4.3 Working with Lists](https://jckantor.github.io/CBE30338/01.01-Getting-Started-with-Python-and-Jupyter-Notebooks.html#1.1.4.3-Working-with-Lists)&quot;,&quot;level&quot;:3,&quot;section&quot;:&quot;1.1.4.3 Working with Lists&quot;}">

``` python
print(np.add(x,y))
print(np.dot(x,y))
```

<div class="output stream stdout">

    [ 6  8 10 12]
    70

</div>

</div>

<div class="cell markdown" data-nbpages="{&quot;link&quot;:&quot;[1.1.4.3 Working with Lists](https://jckantor.github.io/CBE30338/01.01-Getting-Started-with-Python-and-Jupyter-Notebooks.html#1.1.4.3-Working-with-Lists)&quot;,&quot;level&quot;:3,&quot;section&quot;:&quot;1.1.4.3 Working with Lists&quot;}">

A for loop is a means for iterating over the elements of a list. The
colon marks the start of code that will be executed for each element of
a list. Indenting has meaning in Python. In this case, everything in the
indented block will be executed on each iteration of the for loop. This
example also demonstrates string formatting.

</div>

<div class="cell code" data-execution_count="8" data-nbpages="{&quot;link&quot;:&quot;[1.1.4.3 Working with Lists](https://jckantor.github.io/CBE30338/01.01-Getting-Started-with-Python-and-Jupyter-Notebooks.html#1.1.4.3-Working-with-Lists)&quot;,&quot;level&quot;:3,&quot;section&quot;:&quot;1.1.4.3 Working with Lists&quot;}">

``` python
for x in xList:
    print("sin({0}) = {1:8.5f}".format(x,np.sin(x)))
```

<div class="output stream stdout">

    sin(1) =  0.84147
    sin(2) =  0.90930
    sin(3) =  0.14112
    sin(4) = -0.75680

</div>

</div>

<div class="cell markdown" data-nbpages="{&quot;link&quot;:&quot;[1.1.4.4 Working with Dictionaries](https://jckantor.github.io/CBE30338/01.01-Getting-Started-with-Python-and-Jupyter-Notebooks.html#1.1.4.4-Working-with-Dictionaries)&quot;,&quot;level&quot;:3,&quot;section&quot;:&quot;1.1.4.4 Working with Dictionaries&quot;}">
    
### 3.4 Example: Plotting with Matplotlib

Importing the `matplotlib.pyplot` library gives IPython notebooks
plotting functionality very similar to Matlab's. Here are some examples
using functions from the

</div>

<div class="cell code" data-execution_count="15" data-nbpages="{&quot;link&quot;:&quot;[1.1.4.5 Plotting with Matplotlib](https://jckantor.github.io/CBE30338/01.01-Getting-Started-with-Python-and-Jupyter-Notebooks.html#1.1.4.5-Plotting-with-Matplotlib)&quot;,&quot;level&quot;:3,&quot;section&quot;:&quot;1.1.4.5 Plotting with Matplotlib&quot;}">

``` python
%matplotlib inline

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10)
y = np.sin(x)
z = np.cos(x)

plt.plot(x,y,'b',x,z,'r')
plt.xlabel('Radians');
plt.ylabel('Value');
plt.title('Plotting Demonstration')
plt.legend(['Sin','Cos'])
plt.grid()
```

<div class="output display_data">

![](figures/Screen-Shot-MATLIB-Plot.png)

</div>

</div>

