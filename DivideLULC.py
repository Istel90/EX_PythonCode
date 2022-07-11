# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 19:23:14 2020

@author: univSEOULGIS
"""


#%% import.관리
import arcpy


#%% DevideLULC
def DevideLULC (InputShp, FieldName, OutputName) :
    ### Auto variables 수정최소
    Pre_where = '"'+ FieldName + '"' + '='
    
    ### Main 수정최소
    allValues = set()
    with arcpy.da.SearchCursor(InputShp, [FieldName]) as searchCursor:
        for row in searchCursor:
            allValues.add(row[0])
            UniqueValues = sorted(allValues)
    for i in UniqueValues :
        out_feature_class = OutputName + str(i) + ".shp"
        where_clause = Pre_where + str(i)
        arcpy.Select_analysis(InputShp, out_feature_class, where_clause)


### 함수 변수 설명 
# InputShp 은 나눠야하는 토지피복 지도 데이터로 '이름.shp' 나 '이름' 형식으로 작성해야함 
# FieldName 은 토지피복코드가 있는 필드의 이름을 설정합니다. '필드명'형식으로 작성해야함.
# OutputName 는 결과로 나오는 shp파일의 이름입니다. 설정한 이름뒤_토지피복코드가 자동으로 붙습니다. 예) 'Landcover'입력시 Landcover120, Landcover130 등 붙음.


DevideLULC(r'D:\90_ArcGISProjects\Projects\MountLine\Inseoul_ST', 'cur_step', r'D:\90_ArcGISProjects\Projects\MountLine\InSeoul_ST_' )
#
