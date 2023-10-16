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

#%%
import matplotlib.pyplot as plt

controled = np.arange(12)
Treat_1 = controled + 1
Treat_2 = controled*2
Fullelements = np.concatenate((controled, Treat_1, Treat_2))

# 총 평균, 집단평균
TotalMean = np.mean(Fullelements)
MeanControl = np.mean(controled)
MeanTreat_1 = np.mean(Treat_1)
MeanTreat_2 = np.mean(Treat_2)
print(f"총 평균: {TotalMean}, 집단평균: {MeanControl}, {MeanTreat_1}, {MeanTreat_2}")
# 총 변동량
TotalVar = np.var(Fullelements)
## 군간 변동량
VarControl = controled.size*((TotalMean - MeanControl)**2)
VarTreat_1 = controled.size*((TotalMean - MeanTreat_1)**2)
VarTreat_2 = controled.size*((TotalMean - MeanTreat_2)**2)
RefVar = VarControl + VarTreat_1 + VarTreat_2
# 불편분산
UnbiasedVar = RefVar / (controled.size - 1)

## 군내 변동량
InnerVarControl = np.var(controled)
InnerVarTreat_1 = np.var(Treat_1)
InnerVarTreat_2 = np.var(Treat_2)
InnerVar = InnerVarControl + InnerVarTreat_1 + InnerVarTreat_2
InnerUnbiasedVar = InnerVar / (controled.size - 1)

print('총 변동량: ', TotalVar)
print('군내 변동량: ', InnerVar)
print('군간 변동량: ', RefVar)

#%% 두 집단에서
controled = np.arange(12)
Treat_1 = controled + 1
Treat_2 = controled * 3
Fullelements = np.concatenate((controled, Treat_1, Treat_2))

# 총 평균, 집단평균
TotalMean = np.mean(Fullelements)
MeanControl = np.mean(controled)
MeanTreat_1 = np.mean(Treat_1)

# 총 변동량
TotalVar = np.var(Fullelements)
## 군간 변동량
VarControl = controled.size*((TotalMean - MeanControl)**2)
VarTreat_1 = controled.size*((TotalMean - MeanTreat_1)**2)
VarTreat_2 = controled.size*((TotalMean - MeanTreat_2)**2)
RefVar = VarControl + VarTreat_1 + VarTreat_2
# 불편분산
UnbiasedVar = RefVar / (controled.size - 1)

## 군내 변동량
InnerVarControl = np.var(controled)
InnerVarTreat_1 = np.var(Treat_1)
InnerVar = InnerVarControl + InnerVarTreat_1
InnerUnbiasedVar = InnerVar / (controled.size - 1)

## F-value
F = UnbiasedVar / InnerUnbiasedVar

print('총 변동량: ', TotalVar)
print('군내 변동량: ', InnerVar)
print('군간 변동량: ', RefVar)
print('F-value: ', F)

# 선형계수로 
fitControl = np.polyfit(controled, controled, 1)
fitTreat_1 = np.polyfit(controled, Treat_1, 1)
fitTreat_2 = np.polyfit(controled, Treat_2, 1)
# 선형계수 차이
fitDiff_1 = abs(fitControl[0] - fitTreat_1[0])
fitDiff_2 = abs(fitControl[0] - fitTreat_2[0])
print(f"fitDiff_1: {fitDiff_1}, fitDiff_2: {fitDiff_2}")

#%% X축을 Binary로
Controled = np.arange(24).reshape((2,12))
Controled[1] = Controled[1]*2
# 절편만 올린거, 동질성 확보
Treat_1 = Controled + 1
# 기울기 변화시킨거, 군간 변동량 확보  
Treat_2 = Controled * 3

## 0, 1 인덱스의 각 평균 구하기
MeanControl_0 = np.mean(Controled[0])
MeanControl_1 = np.mean(Controled[1])
MeanTreat_1_0 = np.mean(Treat_1[0])
MeanTreat_1_1 = np.mean(Treat_1[1])
MeanTreat_2_0 = np.mean(Treat_2[0])
MeanTreat_2_1 = np.mean(Treat_2[1])

## DID Control vs Treat_1
DiffPast = abs(MeanControl_0 - MeanTreat_1_0)
DiffNow = abs(MeanControl_1 - MeanTreat_1_1)
DID_1 = DiffNow - DiffPast
print(f"DID_CvsT1: {DID_1}")

## DID Control vs Treat_2
DiffPast = abs(MeanControl_0 - MeanTreat_2_0)
DiffNow = abs(MeanControl_1 - MeanTreat_2_1)
DID_2 = DiffNow - DiffPast
print(f"DID_CvsT2: {DID_2},\n MeanControl: {MeanControl_0}, {MeanControl_1},\n MeanTreat_2: {MeanTreat_2_0}, {MeanTreat_2_1}")

DiffFitControl = abs(MeanControl_0 - MeanControl_1)
DiffFitTreat2 = abs(MeanTreat_2_0 - MeanTreat_2_1)
DiffFit = DiffFitTreat2 - DiffFitControl
print(f"DiffFit: {DiffFit}")

#%% X축을 Continuous로
import matplotlib.pyplot as plt

Num_N = 512
X = np.linspace(0, 23, Num_N)
Controled = np.cos(X*2)  + np.random.normal(0, 1, Num_N) + 30 # 3X + 3 + e(오차항)
Treat_1 = np.cos(X*2) + np.random.normal(0, 1, Num_N) + 60 # 일부러 오차항도 다르게 계산되도록 함
Treat_2 = np.cos(X+365) + np.cos(X*2) + np.random.normal(0, 1, Num_N) + 45 # 일부러 오차항도 다르게 계산되도록 함


FitControl = np.polyfit(X, Controled, 1)
FitTreat_1 = np.polyfit(X, Treat_1, 1)
FitTreat_2 = np.polyfit(X, Treat_2, 1)
print(f"FitControl: {FitControl}, FitTreat_1: {FitTreat_1}, FitTreat_2: {FitTreat_2}")

# plot X 축 늘리기
plt.figure(figsize=(30, 15))
plt.rcParams['axes.grid'] = True
plt.rcParams['font.size'] = 50
plt.scatter(X, Controled, c = 'black', marker = 'o')
plt.scatter(X, Treat_1, c = 'skyblue', marker = 'o')
plt.scatter(X, Treat_2, c = 'Tomato', marker = 'o')
plt.plot(X, FitControl[0]*X + FitControl[1], c = 'black', linewidth = 5)
plt.plot(X, FitTreat_1[0]*X + FitTreat_1[1], c = 'blue', linewidth = 5)
plt.plot(X, FitTreat_2[0]*X + FitTreat_2[1], c = 'red', linewidth = 5)

diffFitTreat_1 = abs(FitControl[0] - FitTreat_1[0])
diffFitTreat_2 = abs(FitControl[0] - FitTreat_2[0])
print(f"diffFitTreat_1: {diffFitTreat_1}, diffFitTreat_2: {diffFitTreat_2}")



# sacatter plot 색상 변경




 
