import numpy as np

# a = np.arange(6)
# print(f'arrange:\n {a}')
# a = a.reshape(2,3)
# print(f'reshaped:\n {a}')
# b = np.arange(6,12)
# print(f'arrange:\n {b}')
# np.random.shuffle(b)
# print(f'shuffle:\n {b}')
# b = b.reshape(2,3)
# print(f'reshape:\n {b}')

# result = a * b
# print(f'multiple:\n{result}')

# result = a + b
# print(f'add:\n{result}')

# result = a - b
# print(f'substraction:\n{result}')

# result = a/b
# print(f'devided:\n{result}')

a = np.arange(3)
b = np.array([11, 7, 10])
print(a)
print(type(a))

dot = np.dot(a, b)
print(dot) # 内積
print(a @ b) # @ 行列積
cross = np.cross(a, b)
print(cross) # 外積
outer = np.outer(a, b)
print(outer) # 直積

print("-----------")

a = np.array([[1, 2], 
              [3, 4]])
b = np.array([[-2,1], 
              [1.5, -0.5]])
print(a @ b)
inva = np.linalg.inv(a)
print(a @ inva)
