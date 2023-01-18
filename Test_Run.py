'''
Filename: d:\70_PyCode\EX_PythonCode\Test_Run.py
Path: d:\70_PyCode\EX_PythonCode
Created Date: Wednesday, November 2nd 2022, 3:44:43 pm
Author: Istel90

Copyright (c) 2022 Lab.Spatial data Science & Planning in University of Seoul
'''


#%%
import sys
sys.path.append(r"D:\70_PyCode")

from Wildboar import runCore, RasterGDAL
from RasterGDAL import RasterGDAL

#%% Test Define
import os
import numpy as np
dirpath = r"D:\wildboarDATA\Temp"
os.chdir(dirpath)
# #
InDEM = r"Match_KoreaChina_1arcDEM2.tif"
InputCon = r"Jinju_KOFTR31_PA1_Full_MAXENT.tif"

InputCon2 = RasterGDAL(InputCon).RasterToArray()[0]
InputCon3 = np.where( InputCon2 > 0 , InputCon2, 0 )
InputConRaster = RasterGDAL(InputCon).write_geotiff(InputCon3, "maxEnt_Jinju.tif")

InputConProp = r"maxEnt_Jinju.tif"

runCore(dirpath, InDEM, InputConProp, 42000)


#%% Test Define jinju
# dirpath = r"E:\Dropbox\60_Python_Study\99_UtilityCode\WildBoar\Temp"
# os.chdir(dirpath)
# #
# InDEM = r"ModelINPUT\Match_KoreaChina_1arcDEM2.tif"
# InputConProp = r"Jinju_KOFTR31_PA1_Full_MAXENT.tif"

# runCore(dirpath, InDEM, InputConProp, 42000)
