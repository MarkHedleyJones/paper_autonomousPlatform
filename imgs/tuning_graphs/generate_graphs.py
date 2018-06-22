#! /env/python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter,AutoMinorLocator

plt.rc('font', family='serif', serif='STIXGeneral')
# plt.rc('text', usetex=True)
# plt.rc('xtick', labelsize=8)
# plt.rc('ytick', labelsize=8)
# plt.rc('axes', labelsize=8)
# plt.rc('mathtext', fontset='stix')
# plt.rc('figure', autolayout=True)
# plt.rc('figure', figsize=(7.2, 4.5))

bateman = [7, 6, 6, 4, 3, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
newnham = [9, 6, 4, 4, 3, 2, 1, 0, 0, 0]


dimensions = [390*0.01384,195*0.01384]
params = {'backend': 'ps',
          'axes.labelsize': 10,
          'text.fontsize': 10,
          'legend.fontsize': 8,
          'axes.linewidth' : 0.5,
          'xtick.labelsize': 10,
          'ytick.labelsize': 10,
          'axes.formatter.limits' : '-3, 3',
          'figure.figsize': dimensions,
          'text.usetex'        : True,
          'text.latex.unicode' : True,
          'lines.markersize' : 4}
plt.rcParams.update(params)

fig, ax = plt.subplots(1)
datasource = bateman
ax.bar(range(1, len(datasource)+1), datasource, color='b', edgecolor="none", align="center", width=0.7)
ax.set_xlim(1,len(datasource))
ax.set_ylim(0,10)

plt.yticks(range(11))
plt.xticks(range(len(datasource)+1))
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')
ax = plt.gca()
plt.grid()
plt.xlabel('Traversal attempts through Block A')
plt.ylabel('Interventions per traversal')
plt.tight_layout()
plt.savefig("bateman.pdf")


plt.clf()


dimensions = [230*0.01384,195*0.01384]
params = {'figure.figsize': dimensions}
plt.rcParams.update(params)
fig, ax = plt.subplots(1)

datasource = newnham
ax.bar(range(1, len(datasource)+1), datasource, color='b', edgecolor="none", align="center", width=0.7)
ax.set_xlim(1,len(datasource))
ax.set_ylim(0,10)

plt.yticks(range(11))
plt.xticks(range(len(datasource)+1))
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')
ax = plt.gca()
plt.grid()
plt.xlabel('Traversal attempt through Block B')
plt.ylabel('Interventions per traversal')
plt.tight_layout()
plt.savefig("newnham.pdf")
