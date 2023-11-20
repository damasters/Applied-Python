# Name: Daniel Masters
# Spring 2022
# Section: 31883
# ITP 216 Lab 12

import numpy as np
from matplotlib import pyplot as plt
# Your goal is to duplicate the figure in the Example Output section. It does not have to be identical, but should
# contain the following:
# 1. Your code should produce a figure containing 6 plots.
x = np.arange(0, 2*np.pi, 0.1)
# 2. Each plot should contain a trigonometric function as shown below.
y = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
y4 = np.sinh(x)
y5 = np.cosh(x)
y6 = np.tanh(x)
fig, ax = plt.subplots(2, 3)

# 2. Each plot should contain a trigonometric function as shown below.
# 3. Each plot's axes should be labelled appropriately.
# 4. The figure should have a title.
ax[0, 0].plot(x,y)
ax[0, 0].set(title='sin(x)', xlabel='x', ylabel='y')

ax[0, 1].plot(x, y2)
ax[0, 1].set(title='cos(x)', xlabel='x', ylabel='y')

ax[0, 2].plot(x, y3)
ax[0, 2].set(title='tan(x)', xlabel='x', ylabel='y')

ax[1, 0].plot(x,y4)
ax[1, 0].set(title='sinh(x)', xlabel='x', ylabel='y')

ax[1, 1].plot(x,y5)
ax[1, 1].set(title='cosh(x)', xlabel='x', ylabel='y')

ax[1, 2].plot(x, y6)
ax[1, 2].set(title='tanh(x)', xlabel='x', ylabel='y')


fig.tight_layout()
plt.show()



