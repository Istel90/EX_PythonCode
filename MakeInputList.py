# -*- coding: utf-8 -*-
"""
Created on Tue May 10 14:59:05 2022

@author: univSEOULGIS
"""
import glob
import os
import arcpy

#%% defind Function
#
def Folder_ToMultiInput(FloderPath, search_criteria ):
    dirpath = FloderPath
    search_Con = search_criteria
    queryExpression = os.path.join(dirpath, search_Con) 
    glob_list = glob.glob(queryExpression)
    #Make List
    ListEle = ("';'").join(list(map(str, glob_list)))
    ListInput = "'" + ListEle + "'"
    return ListInput


# arcgisInput으로 만들기
def GDB_ToMultiInput(FloderPath, search_criteria, FeatureType ):
    arcpy.env.overwriteOutput = True
    arcpy.env.workspace = FloderPath
    QueryKey = search_criteria
    glob_list = arcpy.ListFeatureClasses( QueryKey, FeatureType ,"")
    #Make List
    ListEle = ("';'").join(list(map(str, glob_list)))
    ListInput = "'" + ListEle + "'"
    return ListInput

#%%
def Folder_ToList(FloderPath, search_criteria ):
    dirpath = FloderPath
    search_Con = search_criteria
    queryExpression = os.path.join(dirpath, search_Con) 
    ListInput = glob.glob(queryExpression)
    return ListInput


#%%
def GDB_ToList(FloderPath, search_criteria, FeatureType ):
    arcpy.env.overwriteOutput = True
    arcpy.env.workspace = FloderPath
    QueryKey = search_criteria
    ListInput = arcpy.ListFeatureClasses( QueryKey, FeatureType ,"")
    return ListInput




#%% Example of def
## Floder_lsitEX = Folder_ToFileList( r"D:\SRTM_1arc_projected","n*.hgt" )
## print(Floder_lsitEX)

## GDB_lsitEX = GDB_ToFileList_arcgis( r"D:\90.ArcGISProjects\Projects\KoreaCells.gdb","Korea_*", "Polygon " )
## print(GDB_lsitEX)

## List of FeatureType
# Arc —Arc (or polyline) feature classes
# Annotation —Annotation feature classes
# Dimension —Dimension feature classes
# Edge —Edge feature classes
# Junction —Junction feature classes
# Label — Label feature classes
# Line —Polyline (or arc) feature classes
# Multipatch —Multipatch feature classes
# Multipoint —Multipoint feature class
# Node —Node feature classes
# Point —Point feature classes
# Polygon —Polygon feature classes
# Polyline —Polyline (or arc) feature classes
# Region —Region feature classes
# Route —Route feature classes
# Tic —Tic feature classes
# All — All feature classes in the workspace. This is the default.
