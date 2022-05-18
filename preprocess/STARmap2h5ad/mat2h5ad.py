
from asyncore import write
from importlib.metadata import PathDistribution
from pickle import NONE
from turtle import pd

from requests import head
import scipy.io as scio
import scanpy
import h5py
import pandas as pd
dataFile="/home1/zhaolianhe/SPDB/sequentially_encoded/20180123_BS10_light.mat"
data= scio.loadmat(dataFile)
print(data['expr'].shape)
dfdata=pd.DataFrame(data['expr'])
dfdata.to_csv("test.csv",index=False)
adata=scanpy.read_csv("test.csv", delimiter=',', first_column_names=None)
adata.write("sequentially.h5ad")
