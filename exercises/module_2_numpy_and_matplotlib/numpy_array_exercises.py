#%%
# This script contains exercises on 
# manipulating arrays with numpy
import numpy as np

x = np.arange(0, 3**3)

#%%
# 1. What is the length of x?

#%%
# 2. How do you get the first value out of x?

#%%
# 3. How do you get the last value out of x?

#%%
# 4. How do you get the first 5 values out of x?

#%%
# 5. What about the last 5 values?

#%%
# 6. How do you get every other value out of x?

#%%
# 7. Get the first 9 values of x, and reshape them to a
#    3x3 matrix. Assign this matrix to the variable `y`
y = None
print(y)

#%%
# 8. How do you get the middle value out of y?
y = np.array([
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
])

#%%
# 9. How do you get the first row out of y?

#%%
# 10. How do you get the first column out of y?

#%%
# 11. Reshape x into a 3x3x3 cube. Assign this
#     to the variable `z`
z = None
print(z.shape)

#%%
# 12. How do you get the "center" value from z?
z = np.array([
    [[ 0, 1, 2],
     [ 3, 4, 5],
     [ 6, 7, 8]],
    [[ 9,10,11],
     [12,13,14],
     [15,16,17]],
    [[18,19,20],
     [21,22,23],
     [24,25,26]]
])


#%%
# 13. How do you take the total sum of z?

#%%
# 14. How do you take the sum along the first 
#     dimension of z?

#%%
# 15. How do you take the sum along the last
#     dimension of z?
