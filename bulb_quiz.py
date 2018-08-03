from matplotlib import pyplot as plt
import numpy as np
from math import exp


def growth(t,k,r,t0):

    val = k/(1+exp(-r*(t+t0)))
    return val


x = np.arange(0,75,1)
y1 = []
y2 = []

for i in x:
    res = growth(i,15,0.1,-2)
    y1.append(res)

    res2 = growth(i, 15, 0.1, -10)
    y2.append(res2)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x,y1, label='-2')
ax.plot(x,y2, label='-10')
ax.legend()
fig.show()

h = np.array(y1)
R = [0]
for i in range(len(h)):
    if i>0:
        dr = h[i]-h[i-1]
        R.append(dr)
fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
ax2.plot(x,R)

arrR = np.array(R)
print('max growth rate',np.where(arrR==arrR.max())[0])
print('sub t0 growth rate',np.where(arrR<arrR[1])[0])

