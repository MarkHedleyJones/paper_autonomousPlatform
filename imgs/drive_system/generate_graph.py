#! /env/python
import numpy as np
import matplotlib.pyplot as plt
import sys

from matplotlib.ticker import ScalarFormatter,AutoMinorLocator

plt.rc('font', family='serif', serif='STIXGeneral')

climb_ys = []
climb_xs = []
with open("climb.csv", 'r') as f:
  for line in f.readlines():
    climb_ys.append(float(line))

climb_ys = climb_ys[255:255+295]
climb_xs = [x * 0.01 for x in range(len(climb_ys))]
# climb_xs = [x for x in range(len(climb_ys))]

flat_ys = []
flat_xs = []
with open("flat.csv", 'r') as f:
  for line in f.readlines():
    flat_ys.append(float(line))
flat_ys = flat_ys[80:220+85]
flat_xs = [x * 0.01 for x in range(len(flat_ys))]
# flat_xs = [x for x in range(len(flat_ys))]


dimensions = [390*0.01384*0.75,195*0.01384]
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
cbc = 10
cbf = 5
ax.plot(climb_xs[:-cbc], climb_ys[:-cbc], linestyle="-", color="blue")
ax.plot(flat_xs[:-cbf], flat_ys[:-cbf], color="red")


vel_climb = 0.0
vel_flat = 0.0
climb_ys_vel = []
flat_ys_vel = []
for vel in flat_ys:
  vel_flat += vel * 0.01
  flat_ys_vel.append(vel_flat)

for vel in climb_ys:
  vel_climb += vel * 0.01
  climb_ys_vel.append(vel_climb)

ax2 = ax.twinx()

ax2.plot(climb_xs, climb_ys_vel, linestyle="-.", color="blue")
ax2.plot(flat_xs, flat_ys_vel, linestyle="-.", color="red")

power_climb_xs = []
power_flat_xs = []
power_climb_ys = []
power_flat_ys = []

torque_climb_xs = []
torque_flat_xs = []
torque_climb_ys = []
torque_flat_ys = []

wheel_radius = 0.365
mass = 900
angle = 3.5

for i in range(len(flat_xs[:-cbc])):
  force = mass * flat_ys[i]
  speed = flat_ys_vel[i]
  power_flat_ys.append((force * speed)/1000.0)
  power_flat_xs.append(flat_xs[i])
  torque_flat_ys.append(force / 0.365)
  torque_flat_xs.append(flat_xs[i])

print(mass)
print(3.5/90)
print(mass * 3.5/90)
for i in range(len(climb_xs[:-cbc])):
  force = mass * (climb_ys[i] + (angle/90.0))

  speed = climb_ys_vel[i]
  power_climb_ys.append((force * speed)/1000.0)
  torque_climb_ys.append(force / 0.365)
  power_climb_xs.append(climb_xs[i])
  torque_climb_xs.append(climb_xs[i])


print("Max power flat = " + str(max(power_flat_ys)/4))
print("Max power climb = " + str(max(power_climb_ys)/4))
print("Max torque flat = " + str(max(torque_flat_ys)/4))
print("Max torque climb = " + str(max(torque_climb_ys)/4))
# ax2.
#Multiply by 10
ax.set_xlabel("Time (s)")
ax.set_ylabel("Forward acceleration (m/s^2)")
ax2.set_ylabel("Speed (m/s)")
# ax.set_xlim(0, 500)
ax.set_ylim(0, 4.0)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')
ax.grid()
# ax2.grid()
plt.tight_layout()
plt.savefig("graph_acceleration.pdf")

plt.clf()

plt.plot(power_climb_xs, power_climb_ys, color="blue")
plt.plot(power_flat_xs, power_flat_ys, color="red")

plt.tight_layout()
plt.savefig("graph_power.pdf")