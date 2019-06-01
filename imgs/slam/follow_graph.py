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
      'color': 'black' # good
    },
    'run2': {
      'meas':[],
      'max': [],
      'min': [],
      'color': 'green'
    },
    'run3': {
      'meas':[],
      'max': [],
      'min': [],
      'color': 'red'
    },
    'run4': {
      'meas':[],
      'max': [],
      'min': [],
      'color': '#FF9955'
    },
    'run5': {
      'meas':[],
      'max': [],
      'min': [],
      'color': 'blue'
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

dimensions = [390*0.01384*1.0,195*0.01384]
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

xs = range(1,len(data['distance_from_average']['run1']['meas'])+1)
ys = data['distance_from_average']['run1']['meas']

errs = []

for item_num in range(40):
  print(item_num)
  errs.append(data['distance_from_centre']['run1']['max'][item_num] - data['distance_from_centre']['run1']['min'][item_num])

print(errs)

for run in range(1,6):
  print(run)
  # ax.plot(xs,data['distance_from_average']['run'+str(run)]['meas'])
  ax.errorbar(xs,list(map(lambda x: x/1000, data['distance_from_centre']['run'+str(run)]['meas'])), xerr=None, yerr=0.546703/2, barsabove=True, fmt="-x", capsize=2, color=data['distance_from_centre']['run'+str(run)]['color'])
# ax.bar(range(1, len(datasource)+1), datasource, color='b', edgecolor="none", align="center", width=0.7)
ax.set_xlim(0, 41)
# ax.set_ylim(-4.370/2,4.370/2)
ax.set_ylim(-1.0, 1.0)

# plt.yticks(range(11))
# plt.xticks(range(len(datasource)+1))
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')
leg = ax.legend(scatterpoints=1, fancybox=True, loc=4)
# leg.get_frame().set_linewidth(0.0)

ax = plt.gca()
plt.grid()
plt.ylabel('Displacement from \npost/trunk mid-point (m)')
plt.xlabel('Post/trunk pair')
plt.tight_layout()
plt.savefig("row_tracking_averages.pdf")

fig.clf()

