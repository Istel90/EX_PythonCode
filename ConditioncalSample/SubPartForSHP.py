'''
Filename: e:\30_github\EX_PythonCode\ConditioncalSample\SubPartForSHP.py
Path: e:\30_github\EX_PythonCode\ConditioncalSample
Created Date: Sunday, February 26th 2023, 5:39:16 pm
Author: henjinic(main), Istel90

Copyright (c) 2023 Lab.Spatial data Science & Planning in University of Seoul
'''
#%% necessary packages
from pathlib import Path
import numpy as np
from osgeo import ogr
import pandas as pd

#%% Sub Functions Define Class & Functions
class Shp:
    def __init__(self, path):
        self._driver = ogr.GetDriverByName("ESRI Shapefile")
        self._data_source = self._driver.Open(str(path), 0) # Data source must be holded
        self._layer = self._data_source.GetLayer()
    def to_df(self, fields=None):
        data = [self._get_feature_data(feature, fields) for feature in self._layer]
        return pd.DataFrame(data)
    def _get_feature_data(self, feature, fields=None):
        if fields is None:
            return feature.items()
        else:
            return {field: feature.GetField(field) for field in fields}
    def filter_by_indeces(self, indeces):
        query = f"FID in ({','.join(map(str, indeces))})"
        self._layer.SetAttributeFilter(query)
        return self
    def clear_filter(self):
        self._layer.SetAttributeFilter(None)
        return self
    def save_as(self, path):
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        data_source = self._driver.CreateDataSource(str(path))
        data_source.CopyLayer(self._layer, path.stem, options=["ENCODING=UTF-8"])
       
def conditional_sample(df, fields, count):
    result = {}
    for key, group in df.groupby(fields):
        size = int(count * len(group) / len(df))
        size = max(size, 1)
        result[key] = sorted(np.random.choice(group.index, size, replace=False))
    return result

SHP_PATH = "./Conditional_TestSHP.shp"
TARGET_FIELDS = ["BBSNCD", "QUANTILE", "L2_CODE"]
SAMPLE_COUNT = 1100
RESULT_DIR = Path("./result/")

def main():
    shp = Shp(SHP_PATH)
    df = shp.to_df(TARGET_FIELDS)
    conditions_to_indices = conditional_sample(df, TARGET_FIELDS, SAMPLE_COUNT)
    for conditions, indeces in conditions_to_indices.items():
        shp.filter_by_indeces(indeces)
        shp.save_as(RESULT_DIR / f"{'_'.join(map(str, conditions))}.shp")        

if __name__ == "__main__":
    main()
