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