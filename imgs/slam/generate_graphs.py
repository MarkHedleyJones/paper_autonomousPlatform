#! /env/python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter,AutoMinorLocator

plt.rc('font', family='serif', serif='STIXGeneral')

runs =  [
("green",  -0.1200164732, 0.1578583179),
("red",    -0.0413509056, -0.1391762753),
("blue",   0.0175453046, -0.2266556812),
("black",  0.1023887962, 0.3248270146),
("orange",  0.041433278, -0.116853376),
]







# 3.2200164393  54.4423387795
# 2.9229818462  54.521004347
# 2.8355024402  54.5799005572
# 3.386985136 54.6647440489
# 2.9453047454  54.6037885306

dimensions = [390*0.01384*0.7,195*0.01384]
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

ys = [x[1] for x in runs]
xs = [x[2] for x in runs]
ax.scatter(xs[3], ys[3], color=['black'], marker='v', label="Test 1")
ax.scatter(xs[1], ys[1], color=['r'], marker='x', label="Test 2")
ax.scatter(xs[2], ys[2], color=['b'], marker='o', label="Test 3")
ax.scatter(xs[0], ys[0], color=['g'], marker='>', label="Test 4")
ax.scatter(xs[4], ys[4], color=['orange'], marker='^', label="Test 5")

# ax.bar(range(1, len(datasource)+1), datasource, color='b', edgecolor="none", align="center", width=0.7)
# ax.set_xlim(4.0, 4.5)
# ax.set_ylim(107,108)

# plt.yticks(range(11))
# plt.xticks(range(len(datasource)+1))
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')
leg = ax.legend(scatterpoints=1, fancybox=True, loc=4)
leg.get_frame().set_linewidth(0.0)

ax = plt.gca()
plt.grid()
plt.xlabel('X-axis end positions (m)')
plt.ylabel('Y-axis end positions (m)')
plt.tight_layout()
plt.savefig("end_positions.pdf")

