#%%
import numpy as np
x = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
v = np.array([1,0,1])
y = x+v
print(y)
#%%
v = np.array([1,2,3])
w = np.array([4,5])
print(np.reshape(v, (3,1))* w)
#%%
x = np.array([[1, 2, 3], [4, 5, 6]])
print(x+v)
#%%
print((x.T +w).T)
#%%w
w = np.array([4,5])
u = np.reshape(w, (2,1))
print(u)
print(x *2)
#%%

#%%
