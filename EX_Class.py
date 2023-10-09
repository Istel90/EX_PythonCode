'''
Filename: c:\Users\istel\GitCode\EX_PythonCode\EX_Class.py
Path: c:\Users\istel\GitCode\EX_PythonCode
Created Date: Friday, January 13th 2023, 9:24:10 pm
Author: Istel90

Copyright (c) 2023 Your Company
'''

#%% necessary imports
import numpy as np
from numpy import linalg as LA
#%%
a = np.arange(9) - 4
b = a.reshape((3, 3))

one = 2 * np.ones((3, 3))
online = one.reshape((9, 1))
LA.norm(one)
dirVec = one / LA.norm(one)
dirVec
LA.norm(dirVec)
LA.norm(online)


#%% one line 으로 데이터 관리하기
a = np.arange(12)
# reshape 3 x 4, n X m 행렬로 만들기
n = a // 4 # n에는 m의 크기에 대한 몫이 저장됨
m = a % 4 # m에는 m의 크기에 대한 나머지가 저장됨
print(n)
print(m)
matrix = a.reshape((3, 4))
matrix
matrix.shape

# 반대의 경우
c = n * 4 + m
print(n)
print(m)
print(c)

#%%
oneline = np.arange(12)
a = oneline.reshape((4, 3))

x = oneline // a.shape[1]
y = oneline % a.shape[1]
ToMatrix = x * a.shape[1] + y

print(x)
print(y)
print(ToMatrix)



