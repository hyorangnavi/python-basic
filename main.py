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
#%%
animals = ['cat','dog','monkey']
for animal in animals:
    print(animal)
#%%
nums = list(range(5))
print(nums)
squares = []
for x in nums:
    squares.append(x**2)
print(squares)
#%%
even_squares = [x**2 for x in nums if x%2 ==0]
print(even_squares)
#%%
# Dictionary
d = {'cat': 'cute', 'dog':'furry'}
print(d['cat'])
print(d.get('cat'))
print('cat' in d)
print('cute' in d)
#%%
d['fish'] = 'wet'
print(d)
#%%
print(d['tuttle'])
#%%
print(d.get('tuttle'))
#%%
print(d.get('monkey', 'N/A'))
print(d.get('fish', 'N/A'))
#%%
d = {'person':2, 'cat':4,'spider':8}
for animal in d:
    legs = d.get(animal)
    print('A {} has {} legs'.format(animal,legs))
#%%
d.update({'ant':6})
for animal in d:
    legs = d.get(animal)
    print('A {} has {} legs'.format(animal,legs))
#%%
nums = list(range(5))
even_num_to_square = {x: x**2 for x in nums if x%2 ==0}
print(even_num_to_square)
#%%
animals = {'cat','dog'}
print('cat' in animals)
print('fish' in animals)
#%%

#%%
animals.add('fish')
print(animals)
print('fish' in animals)
print(len(animals))
#%%
animals.add('cat')
print(len(animals))
animals.remove('cat')
print(len(animals))
#%%

#%%

#%%
