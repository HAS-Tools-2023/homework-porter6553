#%%
import numpy as np

#%%
a = np.array([5,7,9,8,6,4,5])
b = np.array([6,3,4,8,9,7,1])
c = np.zeros(len(a))

for i in range(len(c)):
    c[i] = max(a[i], b[i])
print(c)
# %%
