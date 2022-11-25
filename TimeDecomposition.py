'''
Filename: d:\70_PyCode\EX_PythonCode\TimeDecomposition.py
Path: d:\70_PyCode\EX_PythonCode
Created Date: Friday, November 25th 2022, 8:07:20 pm
Author: Istel90

Copyright (c) 2022 Your Company
'''

#%%
import numpy as np

from scipy.io.wavfile import write
from scipy.fft import fft, fftfreq, rfft, rfftfreq, ifft
from matplotlib import pyplot as plt

from PyEMD import CEEMDAN,  EMD, Visualisation, EEMD

from RasterArcpy import RasterArcpy


#%%
T = np.linspace(0, 1, 100)
S = np.sin(2*2*np.pi*T)
emd = EMD(extrema_detection='parabol')
IMFs = emd.emd(S)
IMFs.shape

t = np.arange(100)
#%%
plt.plot( t, S, 'g' )

# plt.figure(figsize = (8, 6))
plt.plot( t, S, 'g' )
plt.plot( t, IMFs[0], 'r' )
plt.plot( t, IMFs[1], 'b' )
plt.show()

plt.ylabel('x: Amplitude')



#%%
# sampling rate
sr = 2000
# sampling interval
ts = 1.0/sr
t = np.arange(0,1,ts)
#
freq = 1.
x = 3*np.sin(2*np.pi*freq*t)
#
freq = 4
x += np.sin(2*np.pi*freq*t)
#
freq = 7   
x += 0.5* np.sin(2*np.pi*freq*t)

#
plt.figure(figsize = (8, 6))
plt.plot(t, x, 'r')
plt.ylabel('x: Amplitude')
plt.show()

#%%
emd = EMD(extrema_detection='parabol')
EX_IMFs = emd.emd(x)
EX_IMFs, EX_resi = emd.get_imfs_and_residue()

EX_IMFs.shape

ts = np.arange(2000)
plt.plot( ts, EX_IMFs[0], 'r' )
plt.plot( ts, EX_resi, 'r' )

#%%
dirPath = r"F:\Gawongwon_FPAR"
os.chdir(dirPath)

#
CallClass = RasterArcpy(dirPath, "Con_VR_FPAR200101.tif")
ReadRasterStack = CallClass.StackRaster(dirPath, "Con_VR_*.tif" )

#%%
LinearCell = ReadRasterStack[0:240, 150, 150]

# 원본 데이터의 150,150 위치의파형 
ts = np.arange(240)
plt.plot( ts, LinearCell, 'b' )

# module init: 그냥 한번 돌아가서 정의하는 느낌, 결과에 포함되거나 영향 미치지 않음
if __name__ == "__main__":
    s = np.random.random(100)
    ceemdan = CEEMDAN()
    cIMFs = ceemdan(s)
EX_IMFs = ceemdan(LinearCell)
EX_IMFs, EX_resi = ceemdan.get_imfs_and_residue()
# Decomposition 
ts = np.arange(240)

#%%
compFreq = EX_IMFs[0] 
plt.plot( ts, compFreq, 'y' )
plt.plot( ts, LinearCell, 'black' )
#%%
compFreq += EX_IMFs[1] 
plt.plot( ts, compFreq, 'g' )
plt.plot( ts, LinearCell, 'black' )
#%%
compFreq += EX_IMFs[2]
plt.plot( ts, compFreq, 'b' )
plt.plot( ts, LinearCell, 'black' )
#%%
compFreq += EX_IMFs[3]
plt.plot( ts, compFreq, 'c' )
plt.plot( ts, LinearCell, 'black' )
#%%
compFreq += EX_IMFs[4] 
plt.plot( ts, compFreq, 'm' )
plt.plot( ts, LinearCell, 'black' )

#%%
compFreq += EX_resi + 0.2
plt.plot( ts, compFreq, 'r' )
plt.plot( ts, LinearCell, 'black' )


plt.plot( ts, EX_resi, 'r' )


#%% EEMD

eemd = EEMD()
# Say we want detect extrema using parabolic method
emd = eemd.EMD
emd.extrema_detection="parabol"

# Execute EEMD on S
eIMFs = eemd.eemd(LinearCell, ts)
eIMFs, resi= eemd.get_imfs_and_residue()
nIMFs = eIMFs.shape[0]

# Plot results
plt.figure(figsize=(12,9))
plt.subplot(nIMFs+1, 1, 1)
plt.plot(ts, LinearCell, 'r')

for n in range(nIMFs):
    plt.subplot(nIMFs+1, 1, n+2)
    plt.plot(ts, eIMFs[n], 'g')
    plt.ylabel("eIMF %i" %(n+1))
    plt.locator_params(axis='y', nbins=5)

plt.xlabel("Time [s]")
plt.tight_layout()
plt.savefig('eemd_example', dpi=120)
plt.show()

#%%
compFreq = eIMFs[0] 
plt.plot( ts, compFreq, 'y' )
plt.plot( ts, LinearCell, 'black' )
#%%
compFreq += eIMFs[1] 
plt.plot( ts, compFreq, 'g' )
plt.plot( ts, LinearCell, 'black' )
#%%
compFreq += eIMFs[2]
plt.plot( ts, compFreq, 'b' )
plt.plot( ts, LinearCell, 'black' )
#%%
compFreq += eIMFs[3]
plt.plot( ts, compFreq, 'c' )
plt.plot( ts, LinearCell, 'black' )
#%%
compFreq += eIMFs[4] 
plt.plot( ts, compFreq, 'm' )
plt.plot( ts, LinearCell, 'black' )

#%%
compFreq += eIMFs[5] 
plt.plot( ts, compFreq, 'm' )
plt.plot( ts, LinearCell, 'black' )

#%%
compFreq += eIMFs[6] 
plt.plot( ts, compFreq, 'm' )
plt.plot( ts, LinearCell, 'black' )


#%%
compFreq += resi
plt.plot( ts, compFreq, 'r' )
plt.plot( ts, LinearCell, 'black' )

















#%%
emd = EMD(extrema_detection='parabol')
EX_IMFs = emd.emd(LinearCell)
EX_IMFs, EX_resi = emd.get_imfs_and_residue()
# EX_IMFs.shape

#%%
for i in range(6):
    plt.plot( ts, EX_IMFs[i], 'r' )
    # plt.plot( ts, EX_resi, 'r' )

compFreq = EX_IMFs[1] + EX_IMFs[2] + EX_resi
plt.plot( ts, compFreq, 'g' )
plt.plot( ts, LinearCell, 'black' )


compFreq = 0
for i in range(6):
    print( f"Freq{i}")
    compFreq += EX_IMFs[i]
    plt.plot( ts, compFreq, 'r' )
    plt.plot( ts, LinearCell, 'black' )
    print( "Freq_Done")

#%%
compFreq = EX_IMFs[0]
plt.plot( ts, compFreq, 'y' )
plt.plot( ts, LinearCell, 'black' )
#%%
compFreq += EX_IMFs[1]
plt.plot( ts, compFreq, 'g' )
plt.plot( ts, LinearCell, 'black' )
#%%
compFreq += EX_IMFs[2]
plt.plot( ts, compFreq, 'b' )
plt.plot( ts, LinearCell, 'black' )
#%%
compFreq += EX_IMFs[3]
plt.plot( ts, compFreq, 'c' )
plt.plot( ts, LinearCell, 'black' )
#%%
compFreq += EX_IMFs[4]
plt.plot( ts, compFreq, 'm' )
plt.plot( ts, LinearCell, 'black' )
#%%
compFreq += EX_IMFs[5]
plt.plot( ts, compFreq, 'r' )
plt.plot( ts, LinearCell, 'black' )

#%%
compFreq += EX_IMFs[5] + EX_resi
plt.plot( ts, compFreq, 'r' )
plt.plot( ts, LinearCell, 'black' )



#%%
plt.plot( ts, LinearCell, 'r' )


