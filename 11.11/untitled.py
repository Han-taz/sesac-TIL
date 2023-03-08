import pandas as pd
import numpy as np
import pickle

obj_col=[]
for i,j in zip(df2.dtypes.index,df2.dtypes.values):
    print(i,j)
    if j=='object':
        obj_col.append(i)
        
for col in obj_col[1:]:
    label1=LabelEncoder()
    df2[col]=label1.fit_transform([col])
    
    
    
def prefunc():
    