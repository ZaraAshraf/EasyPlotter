# EasyPlotter
An Easy plotter that can plot multiple CSV files.
***
A simple graph plotter that uses numpy and matplotlib to plot a simple 2D graph.
>I built this because I had an objective in a university course to compare betweeen different Algorithms' runtimes given different number of inputs through plotting graphs in Microsoft Excel, and since I'm lazy and broke I decided to take the easy way and plot through this python script I wrote , But I cleaned it a bit and made it usable so here it is.

>It also has multiple colors and stuff
***
![alt text](https://github.com/InEdited/EasyPlotter/blob/master/Plots.png)
## Installing requirements 

```shell
$ sudo pip install numpy
$ sudp pip install matplotlib
```

# Usage
```shell
usage: EasyPlotter.py [-h] -l L [-f F [F ...]] [-x X] [-y Y]

optional arguments:
  -h, --help    show this help message and exit
  -l L          Label of the graph.
  -f F [F ...]  Plot files(csv) after this command(use a space to separate
                multiple files).
  -x X          The label of the X-axis.
  -y Y          The label of the Y-axis.
```

For help : 
```shell
$ python3 EasyPlotter.py -h
```

### Example:

```shell
$ python3 EasyPlotter.py -l LabelOfTheGraph -f file1.csv file2.csv -x XaxisName -y YaxisName
```
