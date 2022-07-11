# -*- coding: utf-8 -*-
"""
Created on Tue May 10 19:38:23 2022

@author: univSEOULGIS
"""
import subprocess

#%%
MaxEntPath = r"E:\MaxEntSamples\maxent\maxent.jar"

#%% java Memory 설정
javaMemory = "java -mx1025m"

#%% define Function

def Py_Maxent(**kwargs):
    """### parameters
    * dem: path
    * output: path
    """
    command = javaMemory + " -jar " + MaxEntPath + " " + kwargs_to_command(kwargs)
    print(command)
    subprocess.run(command)

def kwargs_to_command(kwargs):
    result = " "
    for param, arg in kwargs.items():
        if not arg:
            continue
        
        if isinstance(arg, bool):
            arg = str(arg)
        else:
            arg = str(arg)
        result +=  param + "=" + arg + " "
    return(result)

#%% Example of def

#### 입력변수 설정
## EnvPath = r"E:\MaxEntSamples\Env"
## InputSamplePath = r"E:\MaxEntSamples\input\기존_수원_까마귀.csv"
## OuputPath = r"E:\MaxEntSamples\Output"
####

#### 함수실행
#Py_Maxent(environmentalLayers=EnvPath,
#        samplesFile = InputSamplePath,
#        outputDirectory = OuputPath,
#        #### Options of basicRun
#        autorun = True,
#        redoifexists = True,
#        autofeature = True,
#        responseCurves = True,
#        jackknife = True, 
#        #### Options of advancdRun
#        #writeplotdata = True,
#        #appendtoresultsfile = False, #결과파일(maxentResults.csv)초기화(f)/추가(T)
#        #writebackgroundpredictions = True
#        )

