'''
Filename: d:\70_PyCode\EX_PythonCode\Conditional_Sampling.py
Path: d:\70_PyCode\EX_PythonCode
Created Date: Tuesday, January 31st 2023, 11:00:32 am
Author: Istel90

Copyright (c) 2023 Lab.Spatial data Science & Planning in University of Seoul
'''
#%% Necessary Packages
import os
import sys
import numpy as np
import pandas as pd

#%% Main Parameters
# Set Working Directory
dirpath = r'D:\70_PyCode\EX_PythonCode'
os.chdir(dirpath)

# read.csv
InputCSV = 'SampleforConditional.csv'
SelectField = ["BBSNCD", "HSI_QUANTILE", "LV2_CODE"]
CountTotalSample = 1100

readInputCSV = pd.read_csv(InputCSV)

#%% Conditional Sampling
GetConField = readInputCSV[SelectField]
# getProportion = GetConField.groupby(SelectField[0]).size().reset_index(name='counts')
#


ConditionalSampling = readInputCSV.groupby(SelectField).apply(lambda x: np.random.choice(x.index, int((x.index.size/readInputCSV.shape[0])*CountTotalSample) , replace=False))   

ConditionalSampling.size
for i in ConditionalSampling:
    print(i)
    
ConditionalSampling = readInputCSV.groupby(SelectField).apply(lambda x: np.random.choice(x.index, int((x.index.size/readInputCSV.shape[0])*CountTotalSample) if int((x.index.size/readInputCSV.shape[0])*CountTotalSample) > 0  else 1, replace=False))

#%% Conditional Sampling class

class ConditionalSampling:
    def __init__(self, InputCSV, fields, CountTotalSample):
        self.readInputCSV = pd.read_csv(InputCSV)
        self.field = fields
        self.TotalSample = CountTotalSample  
          
    # 내가 원하는 필드를 Quantile로 나누는 함수, Optional한 기능
    def QuantileField(self, field):
        self.data = self.data.groupby(self.field).size().reset_index(name='counts')
        self.data['quantile'] = pd.qcut(self.data['counts'], 4, labels=False)
        return self.data

    # 원래 데이터에서 해당하는 샘플의 인덱스를 뽑아내는 함수
    def ConditionalSample(self, *addfields):
        ConditionalSampling = self.readInputCSV.groupby(self.field).apply(lambda x: np.random.choice(x.index, int((x.index.size/self.readInputCSV.shape[0])*self.TotalSample) if int((x.index.size/self.readInputCSV.shape[0])*self.TotalSample) > 1  else 1, replace=False))
        return ConditionalSampling          

    # 해야하는 기능: 결과를 원하는 형태로 저장할 수 있는 함수 만들기
    def saveSample(self):
        return print("Not yet")

# ConditionalSampling = readInputCSV.groupby(SelectField).apply(lambda x: np.random.choice(x.index, ((x.index.size/readInputCSV.shape[0])*CountTotalSample) if ((x.index.size/readInputCSV.shape[0])*CountTotalSample) > 0  else int((x.index.size/readInputCSV.shape[0])*CountTotalSample), replace=False))

#%% Example 
# Set Working Directory
# dirpath = r'D:\70_PyCode\EX_PythonCode'
# os.chdir(dirpath)

# # read.csv
# InputCSV = 'SampleforConditional.csv'
# SelectField = ["BBSNCD", "HSI_QUANTILE", "LV2_CODE"]
# CountTotalSample = 1100

# ConditionalSampling


#%% Test
# read.csv
InputCSV = 'SampleforConditional.csv'

SelectField = ["BBSNCD", "HSI_QUANTILE", "LV2_CODE"]
CountTotalSample = 1100



#%% Back-Up

getCountPerType = GetConField.groupby(SelectField).size()
getProportionPerType = getCountPerType.groupby(level=0).apply(lambda x: (x / readInputCSV.shape[0]))
#
getNeedCountPerType = getProportionPerType * CountTotalSample
#
GetSample = readInputCSV.loc[readInputCSV[SelectField[0]]]


getProportionPerType = getCountPerType.groupby(level=0).apply(lambda x: np.random.choice(x.index, int((x / readInputCSV.shape[0]) * CountTotalSample), replace=False))

    

    
Test = readInputCSV.groupby(SelectField).indices
Test
Test2 = Test[(10, 2, 320)]
Test2
Test3 = np.random.choice(Test2, 2, replace=False)

Test4 = readInputCSV.groupby(SelectField).apply(lambda x: np.random.choice(x.index, int((x.index.size/readInputCSV.shape[0])*CountTotalSample) , replace=False))
Test5 = Test4.apply(lambda x: int((x.index.size/readInputCSV.shape[0])*CountTotalSample) )
Test6 = Test4.apply(lambda x: np.random.choice(x.index, int((x.index.size/readInputCSV.shape[0])*CountTotalSample) , replace=False))

Test7 = Test4.apply(lambda x: x.index.size )

Test4 = readInputCSV.groupby(SelectField).apply(lambda x: np.random.choice(x.index, 1, replace=False))
#
    

