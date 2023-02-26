'''
Filename: d:\70_PyCode\EX_PythonCode\Conditional_Sampling.py
Path: d:\70_PyCode\EX_PythonCode
Created Date: Tuesday, January 31st 2023, 11:00:32 am
Author: Istel90, henjinic

Copyright (c) 2023 Lab.Spatial data Science & Planning in University of Seoul
'''
#%% Necessary Packages
import os
# import sys
import numpy as np
import pandas as pd
from pathlib import Path

import sys
sys.path.append(r"E:\30_github\TempPythonCode")

from SubPartForSHP import *

#%% Conditional Sampling class

class ConditionalSampling:
    def __init__(self, InputDATA, TARGET_FIELDS, CountTotalSample):
        GetInputsuffix = Path(InputDATA).suffix
        if GetInputsuffix == '.shp':
            self.readClassSHP = Shp(InputDATA)
            print("Input Data is Shapefile")
        else:
            self.readInputCSV = pd.read_csv(InputDATA)
            print("Input Data is CSV")
        self.TargetField = TARGET_FIELDS
        self.TotalSample = CountTotalSample
          
    # 내가 원하는 필드를 Quantile로 나누는 함수, Optional한 기능
    def QuantileField(self, field):
        self.data = self.data.groupby(self.TargetField).size().reset_index(name='counts')
        self.data['quantile'] = pd.qcut(self.data['counts'], 4, labels=False)
        return self.data

    # 원래 데이터에서 해당하는 샘플의 인덱스를 뽑아내는 함수
    def ConditionalSample(self):
        self._result = {}
        for key, group in self.readInputCSV.groupby(self.TargetField):
            size = int((group.index.size / self.readInputCSV.shape[0]) * self.TotalSample)
            size = max(size, 1)
            self._result[key] = sorted(np.random.choice(group.index, size, replace=False))
        return self._result
    
    def saveSampleToCsv(self, RESULT_DIR="./result_csv/"):
        Path(RESULT_DIR).mkdir(parents=True, exist_ok=True)
        for key, indices in self._result.items():
            target_df = self.readInputCSV.loc[indices]
            filename = f"{RESULT_DIR}/{'_'.join(map(str, key))}.csv"
            target_df.to_csv(filename, index=False, encoding="utf-8-sig")
        return print('Save done')
    
    def ConditionalSample_SHP(self, RESULT_DIR="./result_SHP/"):
        SHP_RESULT_DIR = Path(RESULT_DIR)
        df = self.readClassSHP.to_df(self.TargetField)
        conditions_to_indices = conditional_sample(df, self.TargetField, self.TotalSample)
        for conditions, indeces in conditions_to_indices.items():
            self.readClassSHP.filter_by_indeces(indeces)
            self.readClassSHP.save_as(SHP_RESULT_DIR / f"{'_'.join(map(str, conditions))}.shp")  
        print('Save done')      


#%% Example
# Set Working Directory
# dirpath = r'D:\70_PyCode\EX_PythonCode'
# os.chdir(dirpath)

#### CSV ConditionalSampling
# InputCSV = 'SampleforConditional.csv'
# SelectField = ["BBSNCD", "HSI_QUANTILE", "LV2_CODE"]
# CountTotalSample = 1100
# readClassTest = ConditionalSampling(InputCSV, SelectField, CountTotalSample)
# readClassTest.ConditionalSample()
# readClassTest.saveSampleToCsv("./result_csv/")

#### SHP ConditionalSampling
# InputSHP = 'Conditional_TestSHP.shp'
# SelectField_SHP = ["BBSNCD", "QUANTILE", "L2_CODE"]
# CountTotalSample = 1100
# readClassTest_SHP = ConditionalSampling(InputSHP, SelectField_SHP, CountTotalSample)
# readClassTest_SHP.ConditionalSample_SHP()

def main():
    InputCSV = 'SampleforConditional.csv'
    InputSHP = 'Conditional_TestSHP.shp'
    SelectField = ["BBSNCD", "HSI_QUANTILE", "LV2_CODE"]
    SelectField_SHP = ["BBSNCD", "QUANTILE", "L2_CODE"]
    CountTotalSample = 1100
    # CSV
    readClassTest = ConditionalSampling(InputCSV, SelectField, CountTotalSample)
    readClassTest.ConditionalSample()
    readClassTest.saveSampleToCsv("./result_csv/")
    # SHP
    readClassTest_SHP = ConditionalSampling(InputSHP, SelectField_SHP, CountTotalSample)
    readClassTest_SHP.ConditionalSample_SHP()

if __name__ == "__main__":
    main()
