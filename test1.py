'''
A universal rule that I'd like to work with is that runs are not important.
I am sick and tired of having situations where I run a program for 10 minutes and then I need to change something that is irrelevant for those 10 mintues and RE RUN for another 10 just to get back to where I was before.

Programs crashing or stopping really shouldn't be that bad.

Including this graph situation.

That means data needs to be saved to disk, either continuously or on a program crash/stop.
I would also like to be able to run back in time through a training process, so I think frequenly saving information to a disk is a great thing to do.

what options are out there for doing this stuff? should I build my own visualization tools?
- I think I'll want to create ad hoc visualization tools. the ability to do this quickly and easily is very important.
You do well what you do often, and you do often what you do quickly.

A core principle of this setup is that the training process should be decoupled from visualizations. Changing visualizations should not impact training.
changing training should require minimal rewrites of visualization, but this is less important and will get better over time.

Basically what I'm after is a good system for saving data to the disk.
An important aspect of this is the ability to stop the training program and change what gets written to the disk.


files are a really great way of saving data.
How else do I save a tensor?
I'm not sure.
'''


import matplotlib.pyplot as plt
import matplotlib
import numpy as np

matplotlib.use('QtAgg')


x_values = np.arange(0, 100)
y_values = x_values ** 2

plt.plot(x_values, y_values)
plt.show()
