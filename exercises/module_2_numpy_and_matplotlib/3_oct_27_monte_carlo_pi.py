#%%
import numpy as np
import matplotlib.pyplot as plt

#%%
# Want points (x, y) where x in [-1, +1]
# and y in [-1, +1]
x = np.random.uniform(-1, 1)
y = np.random.uniform(-1, 1)

#%% 
# Want to know radius of a line from the
# origin (0,0) to the point (x,y)

xs = x ** 2
ys = y ** 2
r = np.sqrt(xs + ys)

print(x, y, r)

# %%
def random_point_and_radius():
    x = np.random.uniform(-1, 1)
    y = np.random.uniform(-1, 1)
    xs = x ** 2
    ys = y ** 2
    r = np.sqrt(xs + ys)
    return x, y, r

# %%
all_samples_sizes = np.arange(100, 50000, 1000)

#%%
all_x = []
all_y = []
all_r = []
sample_size = 1000
for i in range(sample_size):
    # What you want to do many times
    # how do we assign values from this function
    x, y, r = random_point_and_radius()
    all_x.append(x)
    all_y.append(y)
    all_r.append(r)

all_x = np.array(all_x)
all_y = np.array(all_y)
all_r = np.array(all_r)

# %%
# boolean array all trues/falses
in_circle = all_r <= 1
out_circle = all_r > 1

# %%
x_points_in_circle = all_x[in_circle]
y_points_in_circle = all_y[in_circle]

x_points_out_circle = all_x[out_circle]
y_points_out_circle = all_y[out_circle]

#%%
plt.scatter(
    x_points_in_circle,
    y_points_in_circle
)
plt.scatter(
    x_points_out_circle,
    y_points_out_circle,
)
# %%
ratio = 4 * np.sum(in_circle) / len(all_x)
ratio


# %%
# ******************************************
# Now let's do this for many different sample
# sizes to see how convergence happens!
# For this we will use a double loop, with
# the outer part calculating the estimate
# and the inner part sampling the number of
# points
# ******************************************
all_samples_sizes = np.arange(10, 5000, 100)

# pi_estimates will store our calculated ratio
pi_estimates = []
# OUTER LOOP
# Just want to run pi estimation code 
# for many sample sizes
for sample_size in all_samples_sizes:
    # We initialize a new list
    # for each sample size test
    all_x = []
    all_y = []
    all_r = []

    # INNER LOOP
    # Actually sample the points and 
    # calculate the radius
    for i in range(sample_size):
        x, y, r = random_point_and_radius()
        all_x.append(x)
        all_y.append(y)
        all_r.append(r)

    # Do the array conversion
    all_x = np.array(all_x)
    all_y = np.array(all_y)
    all_r = np.array(all_r)

    # Calculate the pi estimate
    # and add it to `pi_estimates`
    in_circle = all_r <= 1
    ratio = 4 * np.sum(in_circle) / len(all_x)
    pi_estimates.append(ratio)


# %%

plt.plot(all_samples_sizes, pi_estimates, marker='o')
plt.axhline(np.pi, color='black')
plt.xlabel('Sample size')
plt.ylabel('Pi estimate')

# %%
