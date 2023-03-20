'''
Filename: d:\70_PyCode\EX_PythonCode\01_Landsat8_to_XXX.py
Path: d:\70_PyCode\EX_PythonCode
Created Date: Monday, March 20th 2023, 11:16:53 am
Author: Mingyun(Main), henjinic(base), Istel90

Copyright (c) 2023 Your Company
'''
#%%
# ArcGIS 모듈 불러오기
import arcpy
from arcpy.sa import *
arcpy.CheckOutExtension("spatial")

import glob
import os
import re
import math as m
import datetime
from dateutil.parser import parse
from datetime import timedelta
from datetime import date, time, datetime

arcpy.env.overwriteOutput = True


#%% define class





#%%

workspace = u"D:/Landsat8_tier1_lv1_202004_202103/"	#작업 폴더 지정하기
	# 작업폴더 생성 가이드
	# 1.workspace는 Landsat8 이미지 압축파일을 푼 폴더
	# 2.압축파일, 폴더, 파일 이름은 변경 X

############################
# Check saving option (MUST)
# want = 1
# not  = 0
want_NDVI = 1
want_LST = 1
want_Albedo = 1
############################

# Check save option and make directory
if want_NDVI == 1 and os.path.isdir(workspace + '/NDVI')== False:
	os.makedirs(workspace + '/NDVI')
	
if want_LST == 1 and os.path.isdir(workspace + '/LST') == False:
	os.makedirs(workspace + '/LST')
	
if want_Albedo == 1 and os.path.isdir(workspace + '/ALBEDO')== False:
	os.makedirs(workspace + '/ALBEDO')


# landsat_folder를 불러옴
landsat_folders = filter(os.path.isdir, glob.glob(workspace+"LC08*"))

print("Number of LC08: " + str(len(landsat_folders)))

i = 0
for landsat_folder in landsat_folders:

	# 필요한 Landsat 밴드 불러오기
	## [ALBEDO] B2, B4, B5, B6, B7
	## [NDVI] B4, B5
	## [LST] B10
	f_B1 = glob.glob(landsat_folder + "/*_B1.TIF")[0]
	f_B2 = glob.glob(landsat_folder + "/*_B2.TIF")[0]
	f_B3 = glob.glob(landsat_folder + "/*_B3.TIF")[0]
	f_B4 = glob.glob(landsat_folder + "/*_B4.TIF")[0]
	f_B5 = glob.glob(landsat_folder + "/*_B5.TIF")[0]
	f_B6 = glob.glob(landsat_folder + "/*_B6.TIF")[0]
	f_B7 = glob.glob(landsat_folder + "/*_B7.TIF")[0]
	f_B8 = glob.glob(landsat_folder + "/*_B8.TIF")[0]
	f_B9 = glob.glob(landsat_folder + "/*_B9.TIF")[0]
	f_B10 = glob.glob(landsat_folder + "/*_B10.TIF")[0]
	f_B11 = glob.glob(landsat_folder + "/*_B11.TIF")[0]
	MTL = glob.glob(landsat_folder + "/*_MTL.txt")[0]
	
	# 정규표현식 컴파일
	pMult10 = re.compile("RADIANCE_MULT_BAND_10 = [-|0-9].*[0-9]", re.MULTILINE)
	pAdd10 = re.compile("RADIANCE_ADD_BAND_10 = [-|0-9].*[0-9]", re.MULTILINE)
	
	k1Const10 = re.compile("K1_CONSTANT_BAND_10 = [-|0-9].*[0-9]", re.MULTILINE)
	k2Const10 = re.compile("K2_CONSTANT_BAND_10 = [-|0-9].*[0-9]", re.MULTILINE)
	
	pSun = re.compile("SUN_ELEVATION = [-|0-9].*[0-9]", re.MULTILINE)
	pDate = re.compile("DATE_ACQUIRED = [-|0-9].*[0-9]", re.MULTILINE)
	pTime = re.compile("SCENE_CENTER_TIME = [\'\"][^\'\"]+[\'\"]", re.MULTILINE)
	
	pMult1 = re.compile("REFLECTANCE_MULT_BAND_1 = [-|0-9].*[0-9]", re.MULTILINE)
	pMult2 = re.compile("REFLECTANCE_MULT_BAND_2 = [-|0-9].*[0-9]", re.MULTILINE)
	pMult3 = re.compile("REFLECTANCE_MULT_BAND_3 = [-|0-9].*[0-9]", re.MULTILINE)
	pMult4 = re.compile("REFLECTANCE_MULT_BAND_4 = [-|0-9].*[0-9]", re.MULTILINE)
	pMult5 = re.compile("REFLECTANCE_MULT_BAND_5 = [-|0-9].*[0-9]", re.MULTILINE)
	pMult6 = re.compile("REFLECTANCE_MULT_BAND_6 = [-|0-9].*[0-9]", re.MULTILINE)
	pMult7 = re.compile("REFLECTANCE_MULT_BAND_7 = [-|0-9].*[0-9]", re.MULTILINE)
	pMult8 = re.compile("REFLECTANCE_MULT_BAND_8 = [-|0-9].*[0-9]", re.MULTILINE)
	pMult9 = re.compile("REFLECTANCE_MULT_BAND_9 = [-|0-9].*[0-9]", re.MULTILINE)
	
	pAdd1 = re.compile("REFLECTANCE_ADD_BAND_1 = [-|0-9].*[0-9]", re.MULTILINE)
	pAdd2 = re.compile("REFLECTANCE_ADD_BAND_2 = [-|0-9].*[0-9]", re.MULTILINE)
	pAdd3 = re.compile("REFLECTANCE_ADD_BAND_3 = [-|0-9].*[0-9]", re.MULTILINE)
	pAdd4 = re.compile("REFLECTANCE_ADD_BAND_4 = [-|0-9].*[0-9]", re.MULTILINE)
	pAdd5 = re.compile("REFLECTANCE_ADD_BAND_5 = [-|0-9].*[0-9]", re.MULTILINE)
	pAdd6 = re.compile("REFLECTANCE_ADD_BAND_6 = [-|0-9].*[0-9]", re.MULTILINE)
	pAdd7 = re.compile("REFLECTANCE_ADD_BAND_7 = [-|0-9].*[0-9]", re.MULTILINE)
	pAdd8 = re.compile("REFLECTANCE_ADD_BAND_8 = [-|0-9].*[0-9]", re.MULTILINE)
	pAdd9 = re.compile("REFLECTANCE_ADD_BAND_9 = [-|0-9].*[0-9]", re.MULTILINE)
	
	
	#Search complied pattern
	f = open(MTL, "r")
	r = f.read()
	
	mMult10 = pMult10.search(r)
	mAdd10 = pAdd10.search(r)
	
	m_k1Const10 = k1Const10.search(r)
	m_k2Const10 = k2Const10.search(r)
	
	mSun = pSun.search(r)
	mDate = pDate.search(r)
	mTime = pTime.search(r)
	
	mMult1 = pMult1.search(r)
	mMult2 = pMult2.search(r)
	mMult3 = pMult3.search(r)
	mMult4 = pMult4.search(r)
	mMult5 = pMult5.search(r)
	mMult6 = pMult6.search(r)
	mMult7 = pMult7.search(r)
	mMult8 = pMult8.search(r)
	mMult9 = pMult9.search(r)
	
	mAdd1 = pAdd1.search(r)
	mAdd2 = pAdd2.search(r)
	mAdd3 = pAdd3.search(r)
	mAdd4 = pAdd4.search(r)
	mAdd5 = pAdd5.search(r)
	mAdd6 = pAdd6.search(r)
	mAdd7 = pAdd7.search(r)
	mAdd8 = pAdd8.search(r)
	mAdd9 = pAdd9.search(r)
	
	#Convert pattern to string(value)
	
	rfMult10 = mMult10.group().split(" = ")[-1]
	rfAdd10 = mAdd10.group().split(" = ")[-1]
	
	rf_k1Const10 = m_k1Const10.group().split(" = ")[-1]
	rf_k2Const10 = m_k2Const10.group().split(" = ")[-1]
	
	rfSun = mSun.group().split(" = ")[-1]
	rfDate = mDate.group().split(" = ")[-1]
	Date = rfDate
	rfTime = mTime.group().split(" = ")[-1].split(".")[0].strip('"')
	rfDate = parse(rfDate+"T"+rfTime)
	rfDate = rfDate + timedelta(hours=9)
	
	rfMult1 = mMult1.group().split(" = ")[-1]
	rfMult2 = mMult2.group().split(" = ")[-1]
	rfMult3 = mMult3.group().split(" = ")[-1]
	rfMult4 = mMult4.group().split(" = ")[-1]
	rfMult5 = mMult5.group().split(" = ")[-1]
	rfMult6 = mMult6.group().split(" = ")[-1]
	rfMult7 = mMult7.group().split(" = ")[-1]
	rfMult8 = mMult8.group().split(" = ")[-1]
	rfMult9 = mMult9.group().split(" = ")[-1]
	
	rfAdd1 = mAdd1.group().split(" = ")[-1]
	rfAdd2 = mAdd2.group().split(" = ")[-1]
	rfAdd3 = mAdd3.group().split(" = ")[-1]
	rfAdd4 = mAdd4.group().split(" = ")[-1]
	rfAdd5 = mAdd5.group().split(" = ")[-1]
	rfAdd6 = mAdd6.group().split(" = ")[-1]
	rfAdd7 = mAdd7.group().split(" = ")[-1]
	rfAdd8 = mAdd8.group().split(" = ")[-1]
	rfAdd9 = mAdd9.group().split(" = ")[-1]
	
	print ("%d: %s processing" % (i, Date))	# CHECK LINE
	
	# Load landsat images
	B1 = ((Float(f_B1) * float(rfMult1)) + float(rfAdd1)) / m.sin(m.radians(float(rfSun)))
	B2 = ((Float(f_B2) * float(rfMult2)) + float(rfAdd2)) / m.sin(m.radians(float(rfSun)))
	B3 = ((Float(f_B3) * float(rfMult3)) + float(rfAdd3)) / m.sin(m.radians(float(rfSun)))
	B4 = ((Float(f_B4) * float(rfMult4)) + float(rfAdd4)) / m.sin(m.radians(float(rfSun)))
	B5 = ((Float(f_B5) * float(rfMult5)) + float(rfAdd5)) / m.sin(m.radians(float(rfSun)))
	B6 = ((Float(f_B6) * float(rfMult6)) + float(rfAdd6)) / m.sin(m.radians(float(rfSun)))
	B7 = ((Float(f_B7) * float(rfMult7)) + float(rfAdd7)) / m.sin(m.radians(float(rfSun)))
	B8 = ((Float(f_B8) * float(rfMult8)) + float(rfAdd8)) / m.sin(m.radians(float(rfSun)))
	B9 = ((Float(f_B9) * float(rfMult9)) + float(rfAdd9)) / m.sin(m.radians(float(rfSun)))
	
	#Conversion to TOA Radiance
	toa_band10 = (((Float(f_B10)*float(rfMult10)) + float(rfAdd10)))
	#toa_band10.save(workspace+ "t/LC08_"+ "1toa_band10.tif")
	
	# Conversion to TOA Reflectance
	toa_reflection_band10 = (Float(toa_band10)/m.sin(float(rfSun)))
	#toa_reflection_band10.save(workspace+ "t/LC08_"+ "2toa_reflection_band10.tif")
	
	#Calculate LST in Kelvin for Band 10 and Band 11
	tempKelvin10 = (float(rf_k2Const10)/Ln(float(rf_k1Const10) / Float(toa_band10) + 1.0))
	#tempKelvin10.save(workspace+ "t/LC08_"+ "3tempKelvin10.tif")
	
	#Convert Kelvin to Celsius for Band 10 and 11
	tempCelsius10 = (Float(tempKelvin10) - 273.15)
	#tempCelsius10.save(workspace+ "t/LC08_"+ "4tempCelsius10.tif")	
	
	#Calculate the NDVI
	print ("Calculating the NDVI....")
	
	
	NDVI = ((B5-B4) / (B5 + B4))
	NDVI = SetNull(NDVI, NDVI, "VALUE <= -1" )
	NDVI = SetNull(NDVI, NDVI, "VALUE >= 1" )
	
	# Save NDVI
	if want_NDVI == 1:
		NDVI.save(workspace+ "NDVI/LC08_"+ rfDate.strftime("%y%m%d_T%H'%M'%S") +  "_NDVI.tif")
	
	# Get NDVI max, min
	NDVImax = str(arcpy.GetRasterProperties_management(NDVI, "MAXIMUM"))
	NDVImin = str(arcpy.GetRasterProperties_management(NDVI, "MINIMUM"))
	print(NDVImin)
	print(NDVImax)
	
	#Calculate the proportion of vegetation Pv
	Pv = Square((Float(NDVI)- float(NDVImin)) / (float(NDVImax)-float(NDVImin)))
	#Pv.save(workspace+ "t/LC08_"+ "5Pv.tif")	
	
	#Calculate Emissivity ε
	e = 0.004 * Pv + 0.986
	
	#Calculate the Land Surface Temperature(LST)
	LST = (tempCelsius10 / (1 + (0.00115 * tempCelsius10 / 1.4388) * Ln(e)))
	
	# Save LST
	if want_LST == 1:
		LST.save(workspace +"LST/LC08_"+ rfDate.strftime("%y%m%d_T%H'%M'%S") +  "_LST.tif")
		
		
	# Calculate albedo ( https://www.mdpi.com/2072-4292/9/2/110/htm )
	ALBEDO = 0.356 * B2 + 0.130 * B4 + 0.373 * B5 + 0.085 * B6 + 0.072 * B7 - 0.0018
	
	if want_Albedo == 1:
		ALBEDO.save(workspace +"Albedo/LC08_"+ rfDate.strftime("%y%m%d_T%H'%M'%S") +  "_Albedo.tif")
	

	f.close()
	

	i += 1


	# for test
	# if i == 1:
		# break






