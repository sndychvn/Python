import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as mpp

x = np.linspace(0,10,1000000)
fig, ax = mpp.subplots(figsize=(4,5))
ax.plot(x, np.tan(x))
ax.plot(x, np.cos(x), '--')
ax.plot(x, x*3000)
ax.plot(x, -x*9000)
ax.plot(x, -10000*-x)

fig, ax = mpp.subplots(2,2,figsize=(4,5))
ax[0,0].plot(x, np.tan(x))
ax[0,0].plot(x, -x*9000)
ax[0,1].plot(x, np.cos(x), '--')
ax[0,1].plot(x, x*3000)
ax[1,0].plot(x, -x*9000)
ax[1,0].plot(x, -10000*-x)
ax[1,1].plot(x, -80*-x)
ax[1,1].plot(x, -x*4000)
ax[1,1].plot(x, -8000*-x)

x = np.random.randn(1000)
y = np.random.randn(1000)

fig_a, fig_b = mpp.subplots(figsize=(3,4),colour='blue')
fig_b.scatter(x,y)

data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

fig, ax = mpp.subplots()
ax.scatter('a', 'b', c='c', s='d', data=data)
ax.set(xlabel='entry a', ylabel='entry b')
mpp.show()
