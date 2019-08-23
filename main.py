#%%
x =3
print(x,type(x))
#%%
print('x+1 - %d' %(x+1))
print('x-1 = %d' %(x-1))
print('x*2 = %d' %(x*2))
#%%
y = 4.5
print(y,type(y))
#%%
t, f = True, False
print(type(t),type(f))
#%%
hello = 'hello'
world = 'world'
print(hello,world)
#%%
print('%s %s %d' %(hello,world,12))
#%%
print('{} {} {}'.format(hello,world,12))
#%%
s = 'hello'
print(s.capitalize())
print(s.upper())
print(s.replace('l','(ell)'))
print('          world'.strip())


#%%
ss = ['hello', 'world', 'python']
concat = ' '.join(ss)
print(concat)
#%%
xs = [2,0,1,8,0,9]
print('Length of list: {}'.format(len(xs)))
print('First Element: {}'.format(xs[0]))
print('Last Element: {}'.format(xs[-1]))


#%%
xs[2] = 'foo'
print(xs)
xs.append('bar')
print(xs)
#%%
x = xs.pop()
print(x, xs)
#%%
nums = range(5)
print(type(nums))
nums = list(nums)
print(type(nums))
#%%
print(nums)
print(nums[2:4])
print(nums[2:])
print(nums[:2])
print(nums[:])
print(nums[-1])
print(nums[:-1])
nums[2:4] = [8,9]
print(nums)
print(nums[::-1])
