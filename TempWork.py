#%%
from pathlib import Path
import pandas as pd
import numpy as np
import arcpy

import datetime

from PyEMD import EMD
#%%

Rawdf = pd.read_csv(Path(r"C:\Users\univSEOULGIS\Documents\카카오톡 받은 파일", '10471_Missing_test.csv'))

#%%
from datetime import datetime, timedelta

t = np.arange(datetime(1985,7,1), datetime(2015,7,1), timedelta(hours=1)).astype(datetime)
t = np.arange(datetime(1985,7,1), datetime(2015,7,1), timedelta(hours=1))


#%% CEEMDAN
from PyEMD import CEEMDAN
from PyEMD import EMD, Visualisation

ceemdan = CEEMDAN(range_thr=0.001, total_power_thr=0.01)

data = pd.read_csv(Path(r"C:\Users\univSEOULGIS\Documents\카카오톡 받은 파일", "test.csv"))

# Part of main run 
datalist = data["tem"].values.tolist()
Timelist = data["date"].values.tolist()
T = np.arange(0, 239, 1)

# module init: 그냥 한번 돌아가서 정의하는 느낌, 결과에 포함되거나 영향 미치지 않음
if __name__ == "__main__":
    s = np.random.random(100)
    ceemdan = CEEMDAN()
    cIMFs = ceemdan(s)

# Part of main run 
ceemdan = CEEMDAN()
c_imfs = ceemdan(datalist)
imfs, res = ceemdan.get_imfs_and_residue()

# Part of visualization
vis = Visualisation()
vis.plot_imfs(imfs=imfs, residue=res, t=Timelist, include_residue=True)
vis.plot_instant_freq(T, imfs=imfs)
vis.show()
#%%
ceemdan = CEEMDAN()
c_imfs = ceemdan(datalist)
imfs, res = ceemdan.get_imfs_and_residue()

# In general:
#components = EEMD()(S)
#imfs, res = components[:-1], components[-1]
vis = Visualisation()
vis.plot_imfs(imfs=imfs, residue=res, t=Timelist, include_residue=True)
vis.plot_instant_freq(t, imfs=imfs)
vis.show()

#%%
import numpy as np

t = np.arange(0, 3, 0.01)
S = np.sin(13*t + 0.2*t**1.4) - np.cos(3*t)

# Extract imfs and residue
# In case of EMD
emd = EMD()
emd.emd(S)
imfs, res = emd.get_imfs_and_residue()

# Extract imfs and residue
# In case of EMD
ceemdan = CEEMDAN()
ceemdan.ceemdan(S)
imfs, res = ceemdan.get_imfs_and_residue()

# In general:
#components = EEMD()(S)
#imfs, res = components[:-1], components[-1]
vis = Visualisation()
vis.plot_imfs(imfs=imfs, residue=res, t=t, include_residue=True)
vis.plot_instant_freq(t, imfs=imfs)
vis.show()

#%%
Indarr = np.identity(n=3, dtype=np.int8)
Stacknp = np.zeros( (10,3,3) )
for i in range(RawNp.shape[0]):
    RawNp[i] = Indarr
    print(i)

Test2 = Stacknp.reshape((10,9))
Test3 = Test2.transpose()
print(Test2)

# raster indexing 
test = []
for i in range(RawNp.shape[0]):
    getValue = RawNp[i][]
    test.append()

