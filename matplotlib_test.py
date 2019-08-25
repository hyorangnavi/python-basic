#%%
import matplotlib.pyplot as plt
import numpy as np
#%%
x = np.arange(0, 3*np.pi,0.1)
print(x)
y = np.sin(x)
print(y)
#%%
plt.plot(x,y)
#%%
y_sin = np.sin(x)
y_cos = np.cos(x)
plt.plot(x, y_sin)
plt.plot(x, y_cos)
plt.xlabel('x axis label')
plt.ylabel('y axis label')
plt.title('Sine and Cosine')
plt.legend(['sine','cosine'])
#%%
x = np.arange(0, 3*np.pi,0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)

plt.subplot(2,1,1)

plt.plot(x,y_sin)
plt.title('Sine')

plt.subplot(2,1,2)
plt.plot(x,y_cos)
plt.title('Cosine')
plt.show()

#%%
fig, axes =plt.subplots(nrows=2,ncols=1)
axes[0].plot(x,y_sin)
axes[1].plot(x,y_cos)
axes[0].set_title('Sine')
axes[1].set_title('Cosine')
plt.show(fig)
#%%

#%%

#%%

#%%

#%%

#%%

#%%

#%%
