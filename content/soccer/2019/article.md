---
title: "test article"
author: "Atom Scott"
date: 2019-02-20T11:53:49-07:00
description: "A test of article theme"
type: article
draft: false
---
# matplotlib - 2D and 3D plotting in Python

J.R. Johansson (jrjohansson at gmail.com)

The latest version of this [IPython notebook](http://ipython.org/notebook.html) lecture is available at [http://github.com/jrjohansson/scientific-python-lectures](http://github.com/jrjohansson/scientific-python-lectures).

The other notebooks in this lecture series are indexed at [http://jrjohansson.github.io](http://jrjohansson.github.io).


```python
# This line configures matplotlib to show figures embedded in the notebook, 
# instead of opening a new window for each figure. More about that later. 
# If you are using an old version of IPython, try using '%pylab inline' instead.
%matplotlib inline
```

## Introduction

Matplotlib is an excellent 2D and 3D graphics library for generating scientific figures. Some of the many advantages of this library include:

* Easy to get started
* Support for $\LaTeX$ formatted labels and texts
* Great control of every element in a figure, including figure size and DPI. 
* High-quality output in many formats, including PNG, PDF, SVG, EPS, and PGF.
* GUI for interactively exploring figures *and* support for headless generation of figure files (useful for batch jobs).

One of the key features of matplotlib that I would like to emphasize, and that I think makes matplotlib highly suitable for generating figures for scientific publications is that all aspects of the figure can be controlled *programmatically*. This is important for reproducibility and convenient when one needs to regenerate the figure with updated data or change its appearance. 

More information at the Matplotlib web page: http://matplotlib.org/

To get started using Matplotlib in a Python program, either include the symbols from the `pylab` module (the easy way):


```python
from pylab import *
```

or import the `matplotlib.pyplot` module under the name `plt` (the tidy way):


```python
import matplotlib
import matplotlib.pyplot as plt
```


```python
import numpy as np
```

## MATLAB-like API

The easiest way to get started with plotting using matplotlib is often to use the MATLAB-like API provided by matplotlib. 

It is designed to be compatible with MATLAB's plotting functions, so it is easy to get started with if you are familiar with MATLAB.

To use this API from matplotlib, we need to include the symbols in the `pylab` module: 


```python
from pylab import *
```

### Example

A simple figure with MATLAB-like plotting API:


```python
x = np.linspace(0, 5, 10)
y = x ** 2
```


```python
figure()
plot(x, y, 'r')
xlabel('x')
ylabel('y')
title('title')
show()
```


![png](article_17_0.png)


Most of the plotting related functions in MATLAB are covered by the `pylab` module. For example, subplot and color/symbol selection:


```python
subplot(1,2,1)
plot(x, y, 'r--')
subplot(1,2,2)
plot(y, x, 'g*-');
```


![png](article_19_0.png)


The good thing about the pylab MATLAB-style API is that it is easy to get started with if you are familiar with MATLAB, and it has a minumum of coding overhead for simple plots. 

However, I'd encourrage not using the MATLAB compatible API for anything but the simplest figures.

Instead, I recommend learning and using matplotlib's object-oriented plotting API. It is remarkably powerful. For advanced figures with subplots, insets and other components it is very nice to work with. 

## The matplotlib object-oriented API

The main idea with object-oriented programming is to have objects that one can apply functions and actions on, and no object or program states should be global (such as the MATLAB-like API). The real advantage of this approach becomes apparent when more than one figure is created, or when a figure contains more than one subplot. 

To use the object-oriented API we start out very much like in the previous example, but instead of creating a new global figure instance we store a reference to the newly created figure instance in the `fig` variable, and from it we create a new axis instance `axes` using the `add_axes` method in the `Figure` class instance `fig`:


```python
fig = plt.figure()

axes = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # left, bottom, width, height (range 0 to 1)

axes.plot(x, y, 'r')

axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('title');
```


![png](article_23_0.png)


Although a little bit more code is involved, the advantage is that we now have full control of where the plot axes are placed, and we can easily add more than one axis to the figure:


```python
fig = plt.figure()

axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8]) # main axes
axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3]) # inset axes

# main figure
axes1.plot(x, y, 'r')
axes1.set_xlabel('x')
axes1.set_ylabel('y')
axes1.set_title('title')

# insert
axes2.plot(y, x, 'g')
axes2.set_xlabel('y')
axes2.set_ylabel('x')
axes2.set_title('insert title');
```


![png](article_25_0.png)


If we don't care about being explicit about where our plot axes are placed in the figure canvas, then we can use one of the many axis layout managers in matplotlib. My favorite is `subplots`, which can be used like this:


```python
fig, axes = plt.subplots()

axes.plot(x, y, 'r')
axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('title');
```


![png](article_27_0.png)



```python
fig, axes = plt.subplots(nrows=1, ncols=2)

for ax in axes:
    ax.plot(x, y, 'r')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('title')
```


![png](article_28_0.png)


That was easy, but it isn't so pretty with overlapping figure axes and labels, right?

We can deal with that by using the `fig.tight_layout` method, which automatically adjusts the positions of the axes on the figure canvas so that there is no overlapping content:


```python
fig, axes = plt.subplots(nrows=1, ncols=2)

for ax in axes:
    ax.plot(x, y, 'r')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('title')
    
fig.tight_layout()
```


![png](article_30_0.png)


### Figure size, aspect ratio and DPI

Matplotlib allows the aspect ratio, DPI and figure size to be specified when the `Figure` object is created, using the `figsize` and `dpi` keyword arguments. `figsize` is a tuple of the width and height of the figure in inches, and `dpi` is the dots-per-inch (pixel per inch). To create an 800x400 pixel, 100 dots-per-inch figure, we can do: 


```python
fig = plt.figure(figsize=(8,4), dpi=100)
```


    <matplotlib.figure.Figure at 0x8065320>


The same arguments can also be passed to layout managers, such as the `subplots` function:


```python
fig, axes = plt.subplots(figsize=(12,3))

axes.plot(x, y, 'r')
axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('title');
```


![png](article_35_0.png)


### Saving figures

To save a figure to a file we can use the `savefig` method in the `Figure` class:


```python
fig.savefig("filename.png")
```

Here we can also optionally specify the DPI and choose between different output formats:


```python
fig.savefig("filename.png", dpi=200)
```

#### What formats are available and which ones should be used for best quality?

Matplotlib can generate high-quality output in a number formats, including PNG, JPG, EPS, SVG, PGF and PDF. For scientific papers, I recommend using PDF whenever possible. (LaTeX documents compiled with `pdflatex` can include PDFs using the `includegraphics` command). In some cases, PGF can also be good alternative.

### Legends, labels and titles

Now that we have covered the basics of how to create a figure canvas and add axes instances to the canvas, let's look at how decorate a figure with titles, axis labels, and legends.

**Figure titles**

A title can be added to each axis instance in a figure. To set the title, use the `set_title` method in the axes instance:


```python
ax.set_title("title");
```

**Axis labels**

Similarly, with the methods `set_xlabel` and `set_ylabel`, we can set the labels of the X and Y axes:


```python
ax.set_xlabel("x")
ax.set_ylabel("y");
```

**Legends**

Legends for curves in a figure can be added in two ways. One method is to use the `legend` method of the axis object and pass a list/tuple of legend texts for the previously defined curves:


```python
ax.legend(["curve1", "curve2", "curve3"]);
```

The method described above follows the MATLAB API. It is somewhat prone to errors and unflexible if curves are added to or removed from the figure (resulting in a wrongly labelled curve).

A better method is to use the `label="label text"` keyword argument when plots or other objects are added to the figure, and then using the `legend` method without arguments to add the legend to the figure: 


```python
ax.plot(x, x**2, label="curve1")
ax.plot(x, x**3, label="curve2")
ax.legend();
```

The advantage with this method is that if curves are added or removed from the figure, the legend is automatically updated accordingly.

The `legend` function takes an optional keyword argument `loc` that can be used to specify where in the figure the legend is to be drawn. The allowed values of `loc` are numerical codes for the various places the legend can be drawn. See http://matplotlib.org/users/legend_guide.html#legend-location for details. Some of the most common `loc` values are:


```python
ax.legend(loc=0) # let matplotlib decide the optimal location
ax.legend(loc=1) # upper right corner
ax.legend(loc=2) # upper left corner
ax.legend(loc=3) # lower left corner
ax.legend(loc=4) # lower right corner
# .. many more options are available
```




    <matplotlib.legend.Legend at 0x3dfc1d0>



The following figure shows how to use the figure title, axis labels and legends described above:


```python
fig, ax = plt.subplots()

ax.plot(x, x**2, label="y = x**2")
ax.plot(x, x**3, label="y = x**3")
ax.legend(loc=2); # upper left corner
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('title');
```


![png](article_56_0.png)


### Formatting text: LaTeX, fontsize, font family

The figure above is functional, but it does not (yet) satisfy the criteria for a figure used in a publication. First and foremost, we need to have LaTeX formatted text, and second, we need to be able to adjust the font size to appear right in a publication.

Matplotlib has great support for LaTeX. All we need to do is to use dollar signs encapsulate LaTeX in any text (legend, title, label, etc.). For example, `"$y=x^3$"`.

But here we can run into a slightly subtle problem with LaTeX code and Python text strings. In LaTeX, we frequently use the backslash in commands, for example `\alpha` to produce the symbol $\alpha$. But the backslash already has a meaning in Python strings (the escape code character). To avoid Python messing up our latex code, we need to use "raw" text strings. Raw text strings are prepended with an '`r`', like `r"\alpha"` or `r'\alpha'` instead of `"\alpha"` or `'\alpha'`:


```python
fig, ax = plt.subplots()

ax.plot(x, x**2, label=r"$y = \alpha^2$")
ax.plot(x, x**3, label=r"$y = \alpha^3$")
ax.legend(loc=2) # upper left corner
ax.set_xlabel(r'$\alpha$', fontsize=18)
ax.set_ylabel(r'$y$', fontsize=18)
ax.set_title('title');
```


![png](article_59_0.png)


We can also change the global font size and font family, which applies to all text elements in a figure (tick labels, axis labels and titles, legends, etc.):


```python
# Update the matplotlib configuration parameters:
matplotlib.rcParams.update({'font.size': 18, 'font.family': 'serif'})
```


```python
fig, ax = plt.subplots()

ax.plot(x, x**2, label=r"$y = \alpha^2$")
ax.plot(x, x**3, label=r"$y = \alpha^3$")
ax.legend(loc=2) # upper left corner
ax.set_xlabel(r'$\alpha$')
ax.set_ylabel(r'$y$')
ax.set_title('title');
```


![png](article_62_0.png)


A good choice of global fonts are the STIX fonts: 


```python
# Update the matplotlib configuration parameters:
matplotlib.rcParams.update({'font.size': 18, 'font.family': 'STIXGeneral', 'mathtext.fontset': 'stix'})
```


```python
fig, ax = plt.subplots()

ax.plot(x, x**2, label=r"$y = \alpha^2$")
ax.plot(x, x**3, label=r"$y = \alpha^3$")
ax.legend(loc=2) # upper left corner
ax.set_xlabel(r'$\alpha$')
ax.set_ylabel(r'$y$')
ax.set_title('title');
```


![png](article_65_0.png)


Or, alternatively, we can request that matplotlib uses LaTeX to render the text elements in the figure:


```python
matplotlib.rcParams.update({'font.size': 18, 'text.usetex': True})
```


```python
fig, ax = plt.subplots()

ax.plot(x, x**2, label=r"$y = \alpha^2$")
ax.plot(x, x**3, label=r"$y = \alpha^3$")
ax.legend(loc=2) # upper left corner
ax.set_xlabel(r'$\alpha$')
ax.set_ylabel(r'$y$')
ax.set_title('title');
```


![png](article_68_0.png)



```python
# restore
matplotlib.rcParams.update({'font.size': 12, 'font.family': 'sans', 'text.usetex': False})
```

### Setting colors, linewidths, linetypes

#### Colors

With matplotlib, we can define the colors of lines and other graphical elements in a number of ways. First of all, we can use the MATLAB-like syntax where `'b'` means blue, `'g'` means green, etc. The MATLAB API for selecting line styles are also supported: where, for example, 'b.-' means a blue line with dots:


```python
# MATLAB style line color and style 
ax.plot(x, x**2, 'b.-') # blue line with dots
ax.plot(x, x**3, 'g--') # green dashed line
```




    [<matplotlib.lines.Line2D at 0x96df0b8>]



We can also define colors by their names or RGB hex codes and optionally provide an alpha value using the `color` and `alpha` keyword arguments:


```python
fig, ax = plt.subplots()

ax.plot(x, x+1, color="red", alpha=0.5) # half-transparant red
ax.plot(x, x+2, color="#1155dd")        # RGB hex code for a bluish color
ax.plot(x, x+3, color="#15cc55")        # RGB hex code for a greenish color
```




    [<matplotlib.lines.Line2D at 0x6fbc048>]




![png](article_75_1.png)


#### Line and marker styles

To change the line width, we can use the `linewidth` or `lw` keyword argument. The line style can be selected using the `linestyle` or `ls` keyword arguments:


```python
fig, ax = plt.subplots(figsize=(12,6))

ax.plot(x, x+1, color="blue", linewidth=0.25)
ax.plot(x, x+2, color="blue", linewidth=0.50)
ax.plot(x, x+3, color="blue", linewidth=1.00)
ax.plot(x, x+4, color="blue", linewidth=2.00)

# possible linestype options ‘-‘, ‘--’, ‘-.’, ‘:’, ‘steps’
ax.plot(x, x+5, color="red", lw=2, linestyle='-')
ax.plot(x, x+6, color="red", lw=2, ls='-.')
ax.plot(x, x+7, color="red", lw=2, ls=':')

# custom dash
line, = ax.plot(x, x+8, color="black", lw=1.50)
line.set_dashes([5, 10, 15, 10]) # format: line length, space length, ...

# possible marker symbols: marker = '+', 'o', '*', 's', ',', '.', '1', '2', '3', '4', ...
ax.plot(x, x+ 9, color="green", lw=2, ls='--', marker='+')
ax.plot(x, x+10, color="green", lw=2, ls='--', marker='o')
ax.plot(x, x+11, color="green", lw=2, ls='--', marker='s')
ax.plot(x, x+12, color="green", lw=2, ls='--', marker='1')

# marker size and color
ax.plot(x, x+13, color="purple", lw=1, ls='-', marker='o', markersize=2)
ax.plot(x, x+14, color="purple", lw=1, ls='-', marker='o', markersize=4)
ax.plot(x, x+15, color="purple", lw=1, ls='-', marker='o', markersize=8, markerfacecolor="red")
ax.plot(x, x+16, color="purple", lw=1, ls='-', marker='s', markersize=8, 
        markerfacecolor="yellow", markeredgewidth=2, markeredgecolor="blue");
```


![png](article_78_0.png)


### Control over axis appearance

The appearance of the axes is an important aspect of a figure that we often need to modify to make a publication quality graphics. We need to be able to control where the ticks and labels are placed, modify the font size and possibly the labels used on the axes. In this section we will look at controling those properties in a matplotlib figure.

#### Plot range

The first thing we might want to configure is the ranges of the axes. We can do this using the `set_ylim` and `set_xlim` methods in the axis object, or `axis('tight')` for automatrically getting "tightly fitted" axes ranges:


```python
fig, axes = plt.subplots(1, 3, figsize=(12, 4))

axes[0].plot(x, x**2, x, x**3)
axes[0].set_title("default axes ranges")

axes[1].plot(x, x**2, x, x**3)
axes[1].axis('tight')
axes[1].set_title("tight axes")

axes[2].plot(x, x**2, x, x**3)
axes[2].set_ylim([0, 60])
axes[2].set_xlim([2, 5])
axes[2].set_title("custom axes range");
```


![png](article_83_0.png)


#### Logarithmic scale

It is also possible to set a logarithmic scale for one or both axes. This functionality is in fact only one application of a more general transformation system in Matplotlib. Each of the axes' scales are set seperately using `set_xscale` and `set_yscale` methods which accept one parameter (with the value "log" in this case):


```python
fig, axes = plt.subplots(1, 2, figsize=(10,4))
      
axes[0].plot(x, x**2, x, np.exp(x))
axes[0].set_title("Normal scale")

axes[1].plot(x, x**2, x, np.exp(x))
axes[1].set_yscale("log")
axes[1].set_title("Logarithmic scale (y)");
```


![png](article_86_0.png)


### Placement of ticks and custom tick labels

We can explicitly determine where we want the axis ticks with `set_xticks` and `set_yticks`, which both take a list of values for where on the axis the ticks are to be placed. We can also use the `set_xticklabels` and `set_yticklabels` methods to provide a list of custom text labels for each tick location:


```python
fig, ax = plt.subplots(figsize=(10, 4))

ax.plot(x, x**2, x, x**3, lw=2)

ax.set_xticks([1, 2, 3, 4, 5])
ax.set_xticklabels([r'$\alpha$', r'$\beta$', r'$\gamma$', r'$\delta$', r'$\epsilon$'], fontsize=18)

yticks = [0, 50, 100, 150]
ax.set_yticks(yticks)
ax.set_yticklabels(["$%.1f$" % y for y in yticks], fontsize=18); # use LaTeX formatted labels
```




    [<matplotlib.text.Text at 0x10a3ae610>,
     <matplotlib.text.Text at 0x10a3aedd0>,
     <matplotlib.text.Text at 0x10a3fe110>,
     <matplotlib.text.Text at 0x10a3fe750>]




![png](article_89_1.png)


There are a number of more advanced methods for controlling major and minor tick placement in matplotlib figures, such as automatic placement according to different policies. See http://matplotlib.org/api/ticker_api.html for details.

#### Scientific notation

With large numbers on axes, it is often better use scientific notation:


```python
fig, ax = plt.subplots(1, 1)
      
ax.plot(x, x**2, x, np.exp(x))
ax.set_title("scientific notation")

ax.set_yticks([0, 50, 100, 150])

from matplotlib import ticker
formatter = ticker.ScalarFormatter(useMathText=True)
formatter.set_scientific(True) 
formatter.set_powerlimits((-1,1)) 
ax.yaxis.set_major_formatter(formatter) 
```


![png](article_93_0.png)


### Axis number and axis label spacing


```python
# distance between x and y axis and the numbers on the axes
matplotlib.rcParams['xtick.major.pad'] = 5
matplotlib.rcParams['ytick.major.pad'] = 5

fig, ax = plt.subplots(1, 1)
      
ax.plot(x, x**2, x, np.exp(x))
ax.set_yticks([0, 50, 100, 150])

ax.set_title("label and axis spacing")

# padding between axis label and axis numbers
ax.xaxis.labelpad = 5
ax.yaxis.labelpad = 5

ax.set_xlabel("x")
ax.set_ylabel("y");
```


![png](article_95_0.png)



```python
# restore defaults
matplotlib.rcParams['xtick.major.pad'] = 3
matplotlib.rcParams['ytick.major.pad'] = 3
```

#### Axis position adjustments

Unfortunately, when saving figures the labels are sometimes clipped, and it can be necessary to adjust the positions of axes a little bit. This can be done using `subplots_adjust`:


```python
fig, ax = plt.subplots(1, 1)
      
ax.plot(x, x**2, x, np.exp(x))
ax.set_yticks([0, 50, 100, 150])

ax.set_title("title")
ax.set_xlabel("x")
ax.set_ylabel("y")

fig.subplots_adjust(left=0.15, right=.9, bottom=0.1, top=0.9);
```


![png](article_99_0.png)


### Axis grid

With the `grid` method in the axis object, we can turn on and off grid lines. We can also customize the appearance of the grid lines using the same keyword arguments as the `plot` function:


```python
fig, axes = plt.subplots(1, 2, figsize=(10,3))

# default grid appearance
axes[0].plot(x, x**2, x, x**3, lw=2)
axes[0].grid(True)

# custom grid appearance
axes[1].plot(x, x**2, x, x**3, lw=2)
axes[1].grid(color='b', alpha=0.5, linestyle='dashed', linewidth=0.5)
```


![png](article_102_0.png)


### Axis spines

We can also change the properties of axis spines:


```python
fig, ax = plt.subplots(figsize=(6,2))

ax.spines['bottom'].set_color('blue')
ax.spines['top'].set_color('blue')

ax.spines['left'].set_color('red')
ax.spines['left'].set_linewidth(2)

# turn off axis spine to the right
ax.spines['right'].set_color("none")
ax.yaxis.tick_left() # only ticks on the left side
```


![png](article_105_0.png)


### Twin axes

Sometimes it is useful to have dual x or y axes in a figure; for example, when plotting curves with different units together. Matplotlib supports this with the `twinx` and `twiny` functions:


```python
fig, ax1 = plt.subplots()

ax1.plot(x, x**2, lw=2, color="blue")
ax1.set_ylabel(r"area $(m^2)$", fontsize=18, color="blue")
for label in ax1.get_yticklabels():
    label.set_color("blue")
    
ax2 = ax1.twinx()
ax2.plot(x, x**3, lw=2, color="red")
ax2.set_ylabel(r"volume $(m^3)$", fontsize=18, color="red")
for label in ax2.get_yticklabels():
    label.set_color("red")
```


![png](article_108_0.png)


### Axes where x and y is zero


```python
fig, ax = plt.subplots()

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0)) # set position of x spine to x=0

ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))   # set position of y spine to y=0

xx = np.linspace(-0.75, 1., 100)
ax.plot(xx, xx**3);
```


![png](article_110_0.png)


### Other 2D plot styles

In addition to the regular `plot` method, there are a number of other functions for generating different kind of plots. See the matplotlib plot gallery for a complete list of available plot types: http://matplotlib.org/gallery.html. Some of the more useful ones are show below:


```python
n = np.array([0,1,2,3,4,5])
```


```python
fig, axes = plt.subplots(1, 4, figsize=(12,3))

axes[0].scatter(xx, xx + 0.25*np.random.randn(len(xx)))
axes[0].set_title("scatter")

axes[1].step(n, n**2, lw=2)
axes[1].set_title("step")

axes[2].bar(n, n**2, align="center", width=0.5, alpha=0.5)
axes[2].set_title("bar")

axes[3].fill_between(x, x**2, x**3, color="green", alpha=0.5);
axes[3].set_title("fill_between");
```


![png](article_114_0.png)



```python
# polar plot using add_axes and polar projection
fig = plt.figure()
ax = fig.add_axes([0.0, 0.0, .6, .6], polar=True)
t = np.linspace(0, 2 * np.pi, 100)
ax.plot(t, t, color='blue', lw=3);
```


![png](article_115_0.png)



```python
# A histogram
n = np.random.randn(100000)
fig, axes = plt.subplots(1, 2, figsize=(12,4))

axes[0].hist(n)
axes[0].set_title("Default histogram")
axes[0].set_xlim((min(n), max(n)))

axes[1].hist(n, cumulative=True, bins=50)
axes[1].set_title("Cumulative detailed histogram")
axes[1].set_xlim((min(n), max(n)));
```


![png](article_116_0.png)


### Text annotation

Annotating text in matplotlib figures can be done using the `text` function. It supports LaTeX formatting just like axis label texts and titles:


```python
fig, ax = plt.subplots()

ax.plot(xx, xx**2, xx, xx**3)

ax.text(0.15, 0.2, r"$y=x^2$", fontsize=20, color="blue")
ax.text(0.65, 0.1, r"$y=x^3$", fontsize=20, color="green");
```


![png](article_119_0.png)


### Figures with multiple subplots and insets

Axes can be added to a matplotlib Figure canvas manually using `fig.add_axes` or using a sub-figure layout manager such as `subplots`, `subplot2grid`, or `gridspec`:

#### subplots


```python
fig, ax = plt.subplots(2, 3)
fig.tight_layout()
```


![png](article_123_0.png)


#### subplot2grid


```python
fig = plt.figure()
ax1 = plt.subplot2grid((3,3), (0,0), colspan=3)
ax2 = plt.subplot2grid((3,3), (1,0), colspan=2)
ax3 = plt.subplot2grid((3,3), (1,2), rowspan=2)
ax4 = plt.subplot2grid((3,3), (2,0))
ax5 = plt.subplot2grid((3,3), (2,1))
fig.tight_layout()
```


![png](article_125_0.png)


#### gridspec


```python
import matplotlib.gridspec as gridspec
```


```python
fig = plt.figure()

gs = gridspec.GridSpec(2, 3, height_ratios=[2,1], width_ratios=[1,2,1])
for g in gs:
    ax = fig.add_subplot(g)
    
fig.tight_layout()
```


![png](article_128_0.png)


#### add_axes

Manually adding axes with `add_axes` is useful for adding insets to figures:


```python
fig, ax = plt.subplots()

ax.plot(xx, xx**2, xx, xx**3)
fig.tight_layout()

# inset
inset_ax = fig.add_axes([0.2, 0.55, 0.35, 0.35]) # X, Y, width, height

inset_ax.plot(xx, xx**2, xx, xx**3)
inset_ax.set_title('zoom near origin')

# set axis range
inset_ax.set_xlim(-.2, .2)
inset_ax.set_ylim(-.005, .01)

# set axis tick locations
inset_ax.set_yticks([0, 0.005, 0.01])
inset_ax.set_xticks([-0.1,0,.1]);
```


![png](article_131_0.png)


### Colormap and contour figures

Colormaps and contour figures are useful for plotting functions of two variables. In most of these functions we will use a colormap to encode one dimension of the data. There are a number of predefined colormaps. It is relatively straightforward to define custom colormaps. For a list of pre-defined colormaps, see: http://www.scipy.org/Cookbook/Matplotlib/Show_colormaps


```python
alpha = 0.7
phi_ext = 2 * np.pi * 0.5

def flux_qubit_potential(phi_m, phi_p):
    return 2 + alpha - 2 * np.cos(phi_p) * np.cos(phi_m) - alpha * np.cos(phi_ext - 2*phi_p)
```


```python
phi_m = np.linspace(0, 2*np.pi, 100)
phi_p = np.linspace(0, 2*np.pi, 100)
X,Y = np.meshgrid(phi_p, phi_m)
Z = flux_qubit_potential(X, Y).T
```

#### pcolor


```python
fig, ax = plt.subplots()

p = ax.pcolor(X/(2*np.pi), Y/(2*np.pi), Z, cmap=matplotlib.cm.RdBu, vmin=abs(Z).min(), vmax=abs(Z).max())
cb = fig.colorbar(p, ax=ax)
```


![png](article_137_0.png)


#### imshow


```python
fig, ax = plt.subplots()

im = ax.imshow(Z, cmap=matplotlib.cm.RdBu, vmin=abs(Z).min(), vmax=abs(Z).max(), extent=[0, 1, 0, 1])
im.set_interpolation('bilinear')

cb = fig.colorbar(im, ax=ax)
```


![png](article_139_0.png)


#### contour


```python
fig, ax = plt.subplots()

cnt = ax.contour(Z, cmap=matplotlib.cm.RdBu, vmin=abs(Z).min(), vmax=abs(Z).max(), extent=[0, 1, 0, 1])
```


![png](article_141_0.png)


## 3D figures

To use 3D graphics in matplotlib, we first need to create an instance of the `Axes3D` class. 3D axes can be added to a matplotlib figure canvas in exactly the same way as 2D axes; or, more conveniently, by passing a `projection='3d'` keyword argument to the `add_axes` or `add_subplot` methods.


```python
from mpl_toolkits.mplot3d.axes3d import Axes3D
```

#### Surface plots


```python
fig = plt.figure(figsize=(14,6))

# `ax` is a 3D-aware axis instance because of the projection='3d' keyword argument to add_subplot
ax = fig.add_subplot(1, 2, 1, projection='3d')

p = ax.plot_surface(X, Y, Z, rstride=4, cstride=4, linewidth=0)

# surface_plot with color grading and color bar
ax = fig.add_subplot(1, 2, 2, projection='3d')
p = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=matplotlib.cm.coolwarm, linewidth=0, antialiased=False)
cb = fig.colorbar(p, shrink=0.5)
```


![png](article_146_0.png)


#### Wire-frame plot


```python
fig = plt.figure(figsize=(8,6))

ax = fig.add_subplot(1, 1, 1, projection='3d')

p = ax.plot_wireframe(X, Y, Z, rstride=4, cstride=4)
```


![png](article_148_0.png)


#### Coutour plots with projections


```python
fig = plt.figure(figsize=(8,6))

ax = fig.add_subplot(1,1,1, projection='3d')

ax.plot_surface(X, Y, Z, rstride=4, cstride=4, alpha=0.25)
cset = ax.contour(X, Y, Z, zdir='z', offset=-np.pi, cmap=matplotlib.cm.coolwarm)
cset = ax.contour(X, Y, Z, zdir='x', offset=-np.pi, cmap=matplotlib.cm.coolwarm)
cset = ax.contour(X, Y, Z, zdir='y', offset=3*np.pi, cmap=matplotlib.cm.coolwarm)

ax.set_xlim3d(-np.pi, 2*np.pi);
ax.set_ylim3d(0, 3*np.pi);
ax.set_zlim3d(-np.pi, 2*np.pi);
```


![png](article_150_0.png)


#### Change the view angle

We can change the perspective of a 3D plot using the `view_init` method, which takes two arguments: `elevation` and `azimuth` angle (in degrees):


```python
fig = plt.figure(figsize=(12,6))

ax = fig.add_subplot(1,2,1, projection='3d')
ax.plot_surface(X, Y, Z, rstride=4, cstride=4, alpha=0.25)
ax.view_init(30, 45)

ax = fig.add_subplot(1,2,2, projection='3d')
ax.plot_surface(X, Y, Z, rstride=4, cstride=4, alpha=0.25)
ax.view_init(70, 30)

fig.tight_layout()
```


![png](article_153_0.png)


### Animations

Matplotlib also includes a simple API for generating animations for sequences of figures. With the `FuncAnimation` function we can generate a movie file from sequences of figures. The function takes the following arguments: `fig`, a figure canvas, `func`, a function that we provide which updates the figure, `init_func`, a function we provide to setup the figure, `frame`, the number of frames to generate, and `blit`, which tells the animation function to only update parts of the frame which have changed (for smoother animations):

    def init():
        # setup figure

    def update(frame_counter):
        # update figure for new frame

    anim = animation.FuncAnimation(fig, update, init_func=init, frames=200, blit=True)

    anim.save('animation.mp4', fps=30) # fps = frames per second

To use the animation features in matplotlib we first need to import the module `matplotlib.animation`:


```python
from matplotlib import animation
```


```python
# solve the ode problem of the double compound pendulum again

from scipy.integrate import odeint
from numpy import cos, sin

g = 9.82; L = 0.5; m = 0.1

def dx(x, t):
    x1, x2, x3, x4 = x[0], x[1], x[2], x[3]
    
    dx1 = 6.0/(m*L**2) * (2 * x3 - 3 * cos(x1-x2) * x4)/(16 - 9 * cos(x1-x2)**2)
    dx2 = 6.0/(m*L**2) * (8 * x4 - 3 * cos(x1-x2) * x3)/(16 - 9 * cos(x1-x2)**2)
    dx3 = -0.5 * m * L**2 * ( dx1 * dx2 * sin(x1-x2) + 3 * (g/L) * sin(x1))
    dx4 = -0.5 * m * L**2 * (-dx1 * dx2 * sin(x1-x2) + (g/L) * sin(x2))
    return [dx1, dx2, dx3, dx4]

x0 = [np.pi/2, np.pi/2, 0, 0]  # initial state
t = np.linspace(0, 10, 250) # time coordinates
x = odeint(dx, x0, t)    # solve the ODE problem
```

Generate an animation that shows the positions of the pendulums as a function of time:


```python
fig, ax = plt.subplots(figsize=(5,5))

ax.set_ylim([-1.5, 0.5])
ax.set_xlim([1, -1])

pendulum1, = ax.plot([], [], color="red", lw=2)
pendulum2, = ax.plot([], [], color="blue", lw=2)

def init():
    pendulum1.set_data([], [])
    pendulum2.set_data([], [])

def update(n): 
    # n = frame counter
    # calculate the positions of the pendulums
    x1 = + L * sin(x[n, 0])
    y1 = - L * cos(x[n, 0])
    x2 = x1 + L * sin(x[n, 1])
    y2 = y1 - L * cos(x[n, 1])
    
    # update the line data
    pendulum1.set_data([0 ,x1], [0 ,y1])
    pendulum2.set_data([x1,x2], [y1,y2])

anim = animation.FuncAnimation(fig, update, init_func=init, frames=len(t), blit=True)

# anim.save can be called in a few different ways, some which might or might not work
# on different platforms and with different versions of matplotlib and video encoders
#anim.save('animation.mp4', fps=20, extra_args=['-vcodec', 'libx264'], writer=animation.FFMpegWriter())
#anim.save('animation.mp4', fps=20, extra_args=['-vcodec', 'libx264'])
#anim.save('animation.mp4', fps=20, writer="ffmpeg", codec="libx264")
anim.save('animation.mp4', fps=20, writer="avconv", codec="libx264")

plt.close(fig)
```

Note: To generate the movie file we need to have either `ffmpeg` or `avconv` installed. Install it on Ubuntu using:

    $ sudo apt-get install ffmpeg

or (newer versions)

    $ sudo apt-get install libav-tools

On MacOSX, try: 

    $ sudo port install ffmpeg


```python
from IPython.display import HTML
video = open("animation.mp4", "rb").read()
video_encoded = video.encode("base64")
video_tag = '<video controls alt="test" src="data:video/x-m4v;base64,{0}">'.format(video_encoded)
HTML(video_tag)
```




<video controls alt="test" src="data:video/x-m4v;base64,AAAAIGZ0eXBpc29tAAACAGlzb21pc28yYXZjMW1wNDEAAAAIZnJlZQABlYptZGF0AAACrwYF//+r
3EXpvebZSLeWLNgg2SPu73gyNjQgLSBjb3JlIDE0MiByMjQ1NSAwMjFjMGRjIC0gSC4yNjQvTVBF
Ry00IEFWQyBjb2RlYyAtIENvcHlsZWZ0IDIwMDMtMjAxNCAtIGh0dHA6Ly93d3cudmlkZW9sYW4u
b3JnL3gyNjQuaHRtbCAtIG9wdGlvbnM6IGNhYmFjPTEgcmVmPTMgZGVibG9jaz0xOjA6MCBhbmFs
eXNlPTB4MzoweDExMyBtZT1oZXggc3VibWU9NyBwc3k9MSBwc3lfcmQ9MS4wMDowLjAwIG1peGVk
X3JlZj0xIG1lX3JhbmdlPTE2IGNocm9tYV9tZT0xIHRyZWxsaXM9MSA4eDhkY3Q9MSBjcW09MCBk
ZWFkem9uZT0yMSwxMSBmYXN0X3Bza2lwPTEgY2hyb21hX3FwX29mZnNldD0tMiB0aHJlYWRzPTEy
IGxvb2thaGVhZF90aHJlYWRzPTIgc2xpY2VkX3RocmVhZHM9MCBucj0wIGRlY2ltYXRlPTEgaW50
ZXJsYWNlZD0wIGJsdXJheV9jb21wYXQ9MCBjb25zdHJhaW5lZF9pbnRyYT0wIGJmcmFtZXM9MyBi
X3B5cmFtaWQ9MiBiX2FkYXB0PTEgYl9iaWFzPTAgZGlyZWN0PTEgd2VpZ2h0Yj0xIG9wZW5fZ29w
PTAgd2VpZ2h0cD0yIGtleWludD0yNTAga2V5aW50X21pbj0yMCBzY2VuZWN1dD00MCBpbnRyYV9y
ZWZyZXNoPTAgcmNfbG9va2FoZWFkPTQwIHJjPWNyZiBtYnRyZWU9MSBjcmY9MjMuMCBxY29tcD0w
LjYwIHFwbWluPTAgcXBtYXg9NjkgcXBzdGVwPTQgaXBfcmF0aW89MS40MCBhcT0xOjEuMDAAgAAA
CDhliIQAO//+906/AptFl2oDklcK9sqkJlm5UmsB8qYAAAMAV9H+CyvrADACapK6ArKw5hT578uF
J69+Vayla3UdyN5CC5xj+zs07maJkq+X9ameCrcBxFJsPXR7Y/WWJKDMk7QpZAAAHAxwgRQr6faa
1eReGl2U3V5C/TjvCC6j0DhG0TN1kPjHhNIyxh54FeVrD6jYdH9ovZftXSTkSc8Z1RZi3xKnM9wQ
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
AAABAAAABQAAAAEAAAACAAAAAQAAAAAAAAABAAAAAQAAAAEAAAAFAAAAAQAAAAIAAAABAAAAAAAA
AAEAAAABAAAAAQAAAAUAAAABAAAAAgAAAAEAAAAAAAAAAQAAAAEAAAACAAAAAgAAAAEAAAAEAAAA
AQAAAAIAAAABAAAAAAAAAAQAAAACAAAAAQAAAAUAAAABAAAAAgAAAAEAAAAAAAAAAQAAAAEAAAAE
AAAAAgAAAAEAAAAFAAAAAQAAAAIAAAABAAAAAAAAAAEAAAABAAAAAQAAAAUAAAABAAAAAgAAAAEA
AAAAAAAAAQAAAAEAAAABAAAABQAAAAEAAAACAAAAAQAAAAAAAAABAAAAAQAAAAEAAAAFAAAAAQAA
AAIAAAABAAAAAAAAAAEAAAABAAAAAgAAAAIAAAABAAAABQAAAAEAAAACAAAAAQAAAAAAAAABAAAA
AQAAAAEAAAAFAAAAAQAAAAIAAAABAAAAAAAAAAEAAAABAAAAAQAAAAIAAAABAAAABQAAAAEAAAAC
AAAAAQAAAAAAAAABAAAAAQAAAAEAAAAFAAAAAQAAAAIAAAABAAAAAAAAAAEAAAABAAAAAQAAAAIA
AAABAAAABQAAAAEAAAACAAAAAQAAAAAAAAABAAAAAQAAAAIAAAACAAAAAQAAAAUAAAABAAAAAgAA
AAEAAAAAAAAAAQAAAAEAAAABAAAABQAAAAEAAAACAAAAAQAAAAAAAAABAAAAAQAAAAQAAAACAAAA
AQAAAAUAAAABAAAAAgAAAAEAAAAAAAAAAQAAAAEAAAACAAAAAgAAAAEAAAAFAAAAAQAAAAIAAAAB
AAAAAAAAAAEAAAABAAAAAgAAAAIAAAABAAAABQAAAAEAAAACAAAAAQAAAAAAAAABAAAAAQAAAAEA
AAAFAAAAAQAAAAIAAAABAAAAAAAAAAEAAAABAAAAAQAAAAUAAAABAAAAAgAAAAEAAAAAAAAAAQAA
AAEAAAADAAAAAgAAAAEAAAAFAAAAAQAAAAIAAAABAAAAAAAAAAEAAAABAAAAAwAAAAIAAAABAAAA
BQAAAAEAAAACAAAAAQAAAAAAAAABAAAAAQAAAAoAAAACAAAAAQAAAAUAAAABAAAAAgAAAAEAAAAA
AAAAAQAAAAEAAAABAAAABQAAAAEAAAACAAAAAQAAAAAAAAABAAAAAQAAAAEAAAAFAAAAAQAAAAIA
AAABAAAAAAAAAAEAAAABAAAAAQAAAAIAAAABAAAABQAAAAEAAAACAAAAAQAAAAAAAAABAAAAAQAA
AAEAAAAFAAAAAQAAAAIAAAABAAAAAAAAAAEAAAABAAAAAwAAAAIAAAABAAAABQAAAAEAAAACAAAA
AQAAAAAAAAABAAAAAQAAAAEAAAAFAAAAAQAAAAIAAAABAAAAAAAAAAEAAAABAAAAAQAAAAIAAAAB
AAAABQAAAAEAAAACAAAAAQAAAAAAAAABAAAAAQAAAAEAAAAFAAAAAQAAAAIAAAABAAAAAAAAAAEA
AAABAAAAAgAAAAIAAAABAAAABQAAAAEAAAACAAAAAQAAAAAAAAABAAAAAQAAAAIAAAACAAAAAQAA
AAUAAAABAAAAAgAAAAEAAAAAAAAAAQAAAAEAAAABAAAAAgAAABxzdHNjAAAAAAAAAAEAAAABAAAA
AQAAAAEAAAP8c3RzegAAAAAAAAAAAAAA+gAACu8AAAHyAAAA8QAAAGoAAACoAAABGQAAAYMAAAJc
AAACUQAAAYQAAAHuAAABMAAAAagAAAG3AAACCQAAAiQAAAH6AAAB7gAAAa4AAAFvAAABkQAAAScA
AADYAAAA1gAAAnYAAAHtAAABCwAAAPgAAAIqAAABlQAAARkAAAGGAAABwAAAAXkAAAEnAAABPAAA
AXoAAAGWAAABswAAAigAAAIsAAACIgAAAUIAAAFSAAAB+AAAAV0AAAFRAAABJAAAAgEAAAF2AAAA
5gAAARsAAAI8AAABagAAAiAAAAIdAAAB0AAAAhsAAAIIAAABoQAAAiIAAAFSAAABUgAAALYAAAIN
AAACkAAAAbsAAAEbAAAAnQAAAUcAAACdAAAAVwAAAEYAAAKCAAABsQAAAOAAAAFiAAACCwAAAdgA
AAFzAAABNwAAAXkAAAFfAAABvwAAAXoAAAHxAAACUAAAAeIAAAE0AAAB4wAAAW0AAAHKAAABcQAA
AUkAAAGIAAAAzgAAANIAAAEjAAACUgAAAkkAAAEqAAABYAAAAi0AAAInAAAB5gAAAZAAAAGvAAAC
AQAAAdUAAAFyAAABJQAAAasAAAI9AAAB8gAAAaEAAAG8AAABeQAAAgsAAAGjAAABMQAAAasAAAGa
AAAB4wAAAc4AAAGRAAABzwAAAVwAAAE2AAABDQAAATIAAAH6AAABtAAAAQYAAAF5AAACGwAAAlAA
AAInAAABuwAAAXsAAAF6AAACJAAAAZ8AAAITAAABIAAAAbYAAAF9AAACDAAAAeIAAAGLAAAA9gAA
AUUAAAFAAAABjQAAAQ4AAAJbAAAB5gAAAeUAAAHYAAABygAAAPAAAAIZAAAB0QAAAcoAAAEZAAAC
EgAAAW0AAAFWAAABswAAAO4AAAHDAAABRQAAAWgAAAIMAAABqQAAAZsAAAIKAAAB4AAAAbAAAAHb
AAABmwAAAVgAAAD/AAAByAAAAXUAAAEmAAABzwAAAa8AAAGnAAABRQAAAakAAAHUAAACSgAAAaYA
AAJBAAAB/gAAAakAAAFZAAABXwAAAQ4AAAD1AAACUAAAAj8AAAHCAAABiAAAAnIAAAD7AAABzQAA
AM0AAAHfAAABhQAAAW0AAAFwAAABswAAAYcAAAI9AAABPQAAAYoAAAHSAAACAAAAAXQAAAGbAAAB
dwAAARsAAADtAAACZgAAAh0AAAFxAAABkAAAAYsAAAJHAAAB5gAAAecAAAGrAAAB7gAAAg0AAAIA
AAABAQAAAV4AAAFyAAAAdAAAAPIAAABxAAAAdwAAAQwAAADyAAACHAAAAi8AAACwAAACGQAAAaAA
AAP4c3RjbwAAAAAAAAD6AAAAMAAACx8AAA0RAAAOAgAADmwAAA8UAAAQLQAAEbAAABQMAAAWXQAA
F+EAABnPAAAa/wAAHKcAAB5eAAAgZwAAIosAACSFAAAmcwAAKCEAACmQAAArIQAALEgAAC0gAAAt
9gAAMGwAADJZAAAzZAAANFwAADaGAAA4GwAAOTQAADq6AAA8egAAPfMAAD8aAABAVgAAQdAAAENm
AABFGQAAR0EAAEltAABLjwAATNEAAE4jAABQGwAAUXgAAFLJAABT7QAAVe4AAFdkAABYSgAAWWUA
AFuhAABdCwAAXysAAGFIAABjGAAAZTMAAGc7AABo3AAAav4AAGxQAABtogAAblgAAHBlAABy9QAA
dLAAAHXLAAB2aAAAd68AAHhMAAB4owAAeOkAAHtrAAB9HAAAffwAAH9eAACBaQAAg0EAAIS0AACF
6wAAh2QAAIjDAACKggAAi/wAAI3tAACQPQAAkh8AAJNTAACVNgAAlqMAAJhtAACZ3gAAmycAAJyv
AACdfQAAnk8AAJ9yAAChxAAApA0AAKU3AACmlwAAqMQAAKrrAACs0QAArmEAALAQAACyEQAAs+YA
ALVYAAC2fQAAuCgAALplAAC8VwAAvfgAAL+0AADBLQAAwzgAAMTbAADGDAAAx7cAAMlRAADLNAAA
zQIAAM6TAADQYgAA0b4AANL0AADUAQAA1TMAANctAADY4QAA2ecAANtgAADdewAA38sAAOHyAADj
rQAA5SgAAOaiAADoxgAA6mUAAOx4AADtmAAA704AAPDLAADy1wAA9LkAAPZEAAD3OgAA+H8AAPm/
AAD7TAAA/FoAAP61AAEAmwABAoAAAQRYAAEGIgABBxIAAQkrAAEK/AABDMYAAQ3fAAEP8QABEV4A
ARK0AAEUZwABFVUAARcYAAEYXQABGcUAARvRAAEdegABHxUAASEfAAEi/wABJK8AASaKAAEoJQAB
KX0AASp8AAEsRAABLbkAAS7fAAEwrgABMl0AATQEAAE1SQABNvIAATjGAAE7EAABPLYAAT73AAFA
9QABQp4AAUP3AAFFVgABRmQAAUdZAAFJqQABS+gAAU2qAAFPMgABUaQAAVKfAAFUbAABVTkAAVcY
AAFYnQABWgoAAVt6AAFdLQABXrQAAWDxAAFiLgABY7gAAWWKAAFnigABaP4AAWqZAAFsEAABbSsA
AW4YAAFwfgABcpsAAXQMAAF1nAABdycAAXluAAF7VAABfTsAAX7mAAGA1AABguEAAYThAAGF4gAB
h0AAAYiyAAGJJgABihgAAYqJAAGLAAABjAwAAYz+AAGPGgABkUkAAZH5AAGUEgAAAF91ZHRhAAAA
V21ldGEAAAAAAAAAIWhkbHIAAAAAAAAAAG1kaXJhcHBsAAAAAAAAAAAAAAAAKmlsc3QAAAAiqXRv
bwAAABpkYXRhAAAAAQAAAABMYXZmNTYuMS4w
">



### Backends

Matplotlib has a number of "backends" which are responsible for rendering graphs. The different backends are able to generate graphics with different formats and display/event loops. There is a distinction between noninteractive backends (such as 'agg', 'svg', 'pdf', etc.) that are only used to generate image files (e.g. with the `savefig` function), and interactive backends (such as Qt4Agg, GTK, MaxOSX) that can display a GUI window for interactively exploring figures. 

A list of available backends are:


```python
print(matplotlib.rcsetup.all_backends)
```

    [u'GTK', u'GTKAgg', u'GTKCairo', u'MacOSX', u'Qt4Agg', u'Qt5Agg', u'TkAgg', u'WX', u'WXAgg', u'CocoaAgg', u'GTK3Cairo', u'GTK3Agg', u'WebAgg', u'nbAgg', u'agg', u'cairo', u'emf', u'gdk', u'pdf', u'pgf', u'ps', u'svg', u'template']


The default backend, called `agg`, is based on a library for raster graphics which is great for generating raster formats like PNG.

Normally we don't need to bother with changing the default backend; but sometimes it can be useful to switch to, for example, PDF or GTKCairo (if you are using Linux) to produce high-quality vector graphics instead of raster based graphics. 

#### Generating SVG with the svg backend


```python
#
# RESTART THE NOTEBOOK: the matplotlib backend can only be selected before pylab is imported!
# (e.g. Kernel > Restart)
# 
import matplotlib
matplotlib.use('svg')
import matplotlib.pylab as plt
import numpy
from IPython.display import Image, SVG
```


```python
#
# Now we are using the svg backend to produce SVG vector graphics
#
fig, ax = plt.subplots()
t = numpy.linspace(0, 10, 100)
ax.plot(t, numpy.cos(t)*numpy.sin(t))
plt.savefig("test.svg")
```


```python
#
# Show the produced SVG file. 
#
SVG(filename="test.svg")
```




![svg](article_169_0.svg)



#### The IPython notebook inline backend

When we use IPython notebook it is convenient to use a matplotlib backend that outputs the graphics embedded in the notebook file. To activate this backend, somewhere in the beginning on the notebook, we add:

    %matplotlib inline

It is also possible to activate inline matplotlib plotting with:

    %pylab inline

The difference is that `%pylab inline` imports a number of packages into the global address space (scipy, numpy), while `%matplotlib inline` only sets up inline plotting. In new notebooks created for IPython 1.0+, I would recommend using `%matplotlib inline`, since it is tidier and you have more control over which packages are imported and how. Commonly, scipy and numpy are imported separately with:

    import numpy as np
    import scipy as sp
    import matplotlib.pyplot as plt

The inline backend has a number of configuration options that can be set by using the IPython magic command `%config` to update settings in `InlineBackend`. For example, we can switch to SVG figures or higher resolution figures with either:

    %config InlineBackend.figure_format='svg'
     
or:

    %config InlineBackend.figure_format='retina'
    
For more information, type:

    %config InlineBackend


```python
%matplotlib inline
%config InlineBackend.figure_format='svg'

import matplotlib.pylab as plt
import numpy
```


```python
#
# Now we are using the SVG vector graphics displaced inline in the notebook
#
fig, ax = plt.subplots()
t = numpy.linspace(0, 10, 100)
ax.plot(t, numpy.cos(t)*numpy.sin(t))
plt.savefig("test.svg")
```


![svg](article_174_0.svg)


#### Interactive backend (this makes more sense in a python script file)


```python
#
# RESTART THE NOTEBOOK: the matplotlib backend can only be selected before pylab is imported!
# (e.g. Kernel > Restart)
# 
import matplotlib
matplotlib.use('Qt4Agg') # or for example MacOSX
import matplotlib.pylab as plt
import numpy as np
```


```python
# Now, open an interactive plot window with the Qt4Agg backend
fig, ax = plt.subplots()
t = np.linspace(0, 10, 100)
ax.plot(t, np.cos(t) * np.sin(t))
plt.show()
```

Note that when we use an interactive backend, we must call `plt.show()` to make the figure appear on the screen.

## Further reading

* http://www.matplotlib.org - The project web page for matplotlib.
* https://github.com/matplotlib/matplotlib - The source code for matplotlib.
* http://matplotlib.org/gallery.html - A large gallery showcaseing various types of plots matplotlib can create. Highly recommended! 
* http://www.loria.fr/~rougier/teaching/matplotlib - A good matplotlib tutorial.
* http://scipy-lectures.github.io/matplotlib/matplotlib.html - Another good matplotlib reference.


## Versions


```python
%reload_ext version_information
%version_information numpy, scipy, matplotlib
```




<table><tr><th>Software</th><th>Version</th></tr><tr><td>Python</td><td>2.7.10 64bit [GCC 4.2.1 (Apple Inc. build 5577)]</td></tr><tr><td>IPython</td><td>3.2.1</td></tr><tr><td>OS</td><td>Darwin 14.1.0 x86_64 i386 64bit</td></tr><tr><td>numpy</td><td>1.9.2</td></tr><tr><td>scipy</td><td>0.16.0</td></tr><tr><td>matplotlib</td><td>1.4.3</td></tr><tr><td colspan='2'>Sat Aug 15 11:30:23 2015 JST</td></tr></table>

