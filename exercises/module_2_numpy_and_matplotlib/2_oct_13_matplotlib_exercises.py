#%% 
# This one is a set of exercises to learn how to 
# customize plots with matplotlib, but also some
# further practice with using numpy and basic
# python functionality

import numpy as np
import matplotlib.pyplot as plt

# %% 1.)
# Plot a sine wave over the domain defined by `x`
x = np.linspace(-5 * np.pi, 5 * np.pi, 1000)
# TODO: Your code here
y = None


plt.plot(x, y)


# %% 2.)
# Now plot a sine wave from y1
# and a cosine wave vrom y2 using
# the same values for x. Label things
# appropriately.
y1 = None
y2 = None
plt.plot(x, y1, label=None)
plt.plot(x, y2, label=None)

# %% 3.)
# From the previous example, plot the sine wave 
# agaist the cosine wave. Before proceeeding with
# the code, think about what you expect to come out
# of this plot. You should not be surprised here...
#
# TODO: Your code here
plt.plot(None, None)

# %% 4.)
# Let's get a bit funky! Now try plotting
# sin(x) against x * cos(x)
# PS: messing with trig functions is dope, go wild here
# TODO: Your code here
None

# %% 5.)
# Moving to a different plot type, let's return to scatter
# plots. Here we just want to make a "scatter" for x and y
# which are described by a multivariate normal distribution
# NOTE: Don't worry if you don't know what the multivariate
#       normal distribution means, the code should still work

x, y = np.random.multivariate_normal(
    mean=[0,1], 
    cov=[[10, 2],
         [ 1, 0]],
    size=1000
).T
# TODO: Your code here
plt.scatter(None, None)

# %% 6.)
# Now add a horizontal line and a vertical line
# for the mean values of x and y.
# NOTE: These can be done with `plt.axhline` and `plt.axvline`

#%% 7.)
# Let's get more advanced and give a taste of 
# subplots - there's nothing to do here, but if 
# we get here let's chat!
fig, axes = plt.subplots(2,2)
axes[0,1].scatter(x, np.log1p(y))
axes[0,0].hist(np.log1p(y), bins=100)
axes[1,1].hist(x, bins=100)
axes[1,0].axis('off')

# %%
