#! /env/python
import numpy as np
import matplotlib.pyplot as plt
import sys

from matplotlib.ticker import ScalarFormatter,AutoMinorLocator

plt.rc('font', family='serif', serif='STIXGeneral')


data = {
  'distance_from_centre': {
    'run1': {
      'meas':[],
      'max': [],
      'min': [],
    },
    'run2': {
      'meas':[],
      'max': [],
      'min': [],
    },
    'run3': {
      'meas':[],
      'max': [],
      'min': [],
    },
    'run4': {
      'meas':[],
      'max': [],
      'min': [],
    },
    'run5': {
      'meas':[],
      'max': [],
      'min': [],
    }
  },
  'distance_from_average': {
    'run1': {
      'meas':[],
      'max': [],
      'min': [],
    },
    'run2': {
      'meas':[],
      'max': [],
      'min': [],
    },
    'run3': {
      'meas':[],
      'max': [],
      'min': [],
    },
    'run4': {
      'meas':[],
      'max': [],
      'min': [],
    },
    'run5': {
      'meas':[],
      'max': [],
      'min': [],
    }
  },
}
block = 0
with open('tracking.csv', 'r') as f:
  for row, line in enumerate(f.readlines()):
    val_count = 0
    g_type = 'distance_from_centre'
    for col, val in enumerate(line.split(',')):
      if val != "" and val != '\n':
        val_count += 1
        try:
          num = float(val)
        except ValueError:
          print("got", val)
          num
      else:
        num = np.nan

      run = col
      if col == 5 or col > 10:
        continue
      if col > 4:
        g_type = 'distance_from_average'
        run = col - 6
      # print(block, run, num)
      if block == 0:
        cat = 'meas'
      elif block == 1:
        cat = 'max'
      elif block == 2:
        cat = 'min'

      data[g_type]['run'+str(run+1)][cat].append(num)

    if val_count == 0:
      block += 1

# print(data)


# sys.exit()

dimensions = [390*0.01384*0.5,195*0.01384]
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
dat = []
for run in ['run1', 'run2', 'run3', 'run4', 'run5']:
  dat.append([x/1000.0 for x in data['distance_from_average'][run]['meas'] if x is not np.nan])
plt.boxplot(dat)
plt.gca().set_xlabel("Trial number")
plt.gca().set_ylabel("Deviation from average (m)")
ax.set_ylim(-0.1, 0.1)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')
plt.grid()
plt.tight_layout()
plt.savefig("row_tracking_repeatability.pdf")
