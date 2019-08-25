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
animals = {'cat','dog','fish'}
for idx, animal in enumerate(animals):
    print('#%d: %s' %(idx+1,animal))
#%%
d = { (x,x+1): x for x in range(10)}
t = (5,6)
print(type(t))
print('key: {}, value: {}'.format(t,d[t]))
#%%
print(d)
#%%
def sign(x):
    if x>0:
        return 'positive'
    elif x<0:
        return 'negative'
    else:
        return 'zero'

for x in [-1,0,1]:
    print('{}: {}'.format(x, sign(x)))

#%%
def hello(name, loud=False):
    if loud:
        print('HELLO, %s' % name.upper())
    else:
        print('Hello, %s' % name)

hello('Bob')
hello('Fred',loud=True)


#%%
class Greeter(object):
    def __init__(self, name):
        self.name = name
    def greet(self, loud=False):
        if loud:
            print('HELLO, %s' % self.name.upper())
        else:
            print('Hello, %s' % self.name)

g = Greeter('Fred')
g.greet()
g.greet(loud=True)

#%%
import numpy as np
#%%
a = np.array([1,2,3])
print("Type :",type(a))
print("Shape :", a.shape)
print("Values :", a[0],a[1],a[2])
a[0] = 5
print("Values :", a)
#%%
b = np.array([[1,2,3],[4,5,6]])
print(b)
print("Values :",b)

#%%
print(b.shape)
print(b[0,0], b[0,1], b[1,0])

#%%
a = np.zeros((3,3))
print(a)
#%%
b = np.ones((1,2))
print(b)
#%%
c = np.full((2,2),7)
print(c)
#%%
d = np.eye(2)
print(d)
#%%
e = np.random.random((3,3))
print(e)
#%%
import numpy as np

a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(a)
print(a.shape)
#%%
b = a[:, 1:]
print(b)
#%%
print(a[0,1])
b[0,0] = 77
print(b)

#%%
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a)
#%%
row_r1 = a[1,:]
row_r2 = a[1:2, :]
row_r3 = a[[1],:]
print(row_r1 , row_r1.shape)
print(row_r2 , row_r2.shape)
print(row_r3 , row_r3.shape)

#%%
col_r1= a[:,1]
col_r2= a[:,1:2]
print(col_r1, col_r1.shape)
print(col_r2, col_r2.shape)

#%%
a = np.array([[1,2],[3,4],[5,6]])
print(a[[0,1,2],[0,1,0]])
print(np.array([a[0,0],a[1,1],a[2,0]]))
#%%
print(a[[0,0],[0,1]])
print(np.array([a[0,0],a[0,1]]))
#%%
a = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(a)
#%%
b = np.array([0,2,0,1])
print(b)
c = a[np.arange(4),b]
print(c)
#%%
print(np.arange(4))
#%%
a[np.arange(4),b] += 10
print(a)
#%%
a = np.array([[1,2],[3,4],[5,6]])
bool_idx = (a>2)
print(bool_idx)
#%%
print(a[bool_idx])
print(a[a>2])

#%%
print(a>2)
#%%
x = np.array([1,2])
y = np.array([1.0,2.0])
z = np.array([1,2], dtype=np.uint8)

print(x.dtype, y.dtype, z.dtype)

#%%
x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]],dtype=np.float64)

z1 = x+y
z2 = np.add(x,y)
print(z1)
print(z2)

print(np.testing.assert_array_equal(z1,z2) )# Test it
#%%
z1 = x-y
z2 = np.subtract(x,y)
print(z1)
print(z2)
print(np.testing.assert_array_equal(z1,z2))

#%%
z1 = x * y
z2 = np.multiply(x, y)
print(z1)
print(z2)
#%%
z1 = x / y
z2 = np.divide(x, y)
print(z1)
print(z2)
np.testing.assert_array_equal(z1, z2)
#%%
z1 = x // y
z2 = np.floor(np.divide(x, y))
z3 = np.floor_divide(x, y)
print(z1)
print(z2)
print(z3)
np.testing.assert_array_equal(z1, z2, z3)
#%%
print(x)
print(np.sqrt(x))
#%%
x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])

v = np.array([9,10])
w = np.array([11,12])

z1 = v.dot(w)
z2 = np.dot(v,w)
z3 = np.matmul(v,w)
z4 = v @ w
print(z1,z2,z3,z4)
np.testing.assert_array_equal(z1,z2,z3,z4)
#%%
z1 = x.dot(v)
z2 = np.dot(x,v)
z3 = np.matmul(x,v)
z4 = x@ v
print(z1,z2,z3,z4)
#%%
z1 = x.dot(y)
z2 = np.dot(x,y)
z3 = np.matmul(x,y)
z4 = x @ y
print(z1, end='\n\n')
print(z2, end='\n\n')
print(z3, end='\n\n')
print(z4, end='\n\n')
#%%
x =np.array([[1,2]
            ,[3,4]])

print(np.sum(x, axis=None))
print(np.sum(x, axis=0))
print(np.sum(x, axis=1))

#%%
print(x)
print(x.T)
#%%
v = np.array([1,2,3])
print(v, v.shape)
print(v.T, v.T.shape)
#%%
x = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print('shape of x:', x.shape)
print(x)
#%%
y = np.reshape(x, (3,4))
print('shape of y:',y.shape)
print(y)
#%%
z = np.reshape(x,(12,1))
print('shape of z:', z.shape)
print(z)
#%%
w = np.reshape(x, (1,12))
print('shape of w:',w.shape)
print(w)
#%%
v = np.reshape(x, (-1,12))
print('shape of v:',v.shape)
print(v)
#%%
x = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
v= np.array([1,0,1])
y =np.zeros_like(x)
print(y)
#%%
for i in range(4):
    y[i,:] = x[i,:] + v
print(y)
#%%
vv = np.tile(v,(4,1))
print(vv)
#%%
y= x+vv
print(y)
#%%
print(y)
#%%
