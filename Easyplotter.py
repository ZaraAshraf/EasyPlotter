#!/usr/bin/python3
import sys,os,argparse
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook

parser = argparse.ArgumentParser(prog='EasyPlotter.py')
parser.add_argument("-l", help="Label of the graph.",required = True)
parser.add_argument("-f",nargs='+', help="Plot files(csv) after this command(use a space to separate multiple files).")
parser.add_argument("-x", help="The label of the X-axis.")
parser.add_argument("-y", help="The label of the Y-axis.")
args = parser.parse_args()

dir = os.path.dirname(os.path.abspath(__file__))

colors = ['r','g','b','p','c']
data = []
counter = 0

if args.f:
    for file in args.f:
        fl = dir + '/' + file
        data.append(np.genfromtxt(fl,delimiter=',',names=['x','y']))
        print(fl)
        #counter+=1

if args.l:
    label = args.l
else:
    label = "Unnamed Graph"

fig = plt.figure()

ax1 = fig.add_subplot(111)
ax2 = fig.add_subplot(111)
plt.title(label)
plt.xlabel(args.x)
plt.ylabel(args.y)
plt.grid(True)

counter=0
plots=[]
for plot in data:
    plots.append(fig.add_subplot(111))
    plots[counter].plot(data[counter]['x'],data[counter]['y'], color = colors[counter], label = args.f[counter][:-4])

#ax1.plot(data1['x'],data1['y'], color = 'r', label=sys.argv[2][:-4])
#ax2.plot(data2['x'],data2['y'], color = 'b', label=sys.argv[3][:-4])

    leg = plots[counter].legend(shadow=True)
    counter+=1

plt.show()
