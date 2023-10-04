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


#%%










