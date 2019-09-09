# -*- coding: utf-8 -*-
"""
read combine files from same experiment but from different fast regimes

"""
import pandas as pd
import os
import glob
import natsort



Experiment='SM_1_03042019_FR'
os.chdir('/Volumes/mpistaff/Diaz_Pichugina_Pseudomona/Data/Mosaik_tracking_1_TIMELAPSES_2019_1-1/'+'SM_1_03042019_FR/')

path=os.getcwd()
all_files=glob.glob(path+"/*Trajectories.txt")
all_files=natsort.humansorted(all_files)



#=============================================#
# read files from one experiment in one data frame
df = pd.DataFrame()

for filename in all_files:
    fast_regime=(filename.split('_')[-1])[0:2]
    fast_regime=int(fast_regime)
    print(fast_regime)
    
    df_temp = pd.read_table(filename)
    df_temp["Experiment"]=Experiment
    df_temp["Fast_regime"]=fast_regime
    df=df.append(df_temp)

# drop empty column
df=df.drop(columns=df.columns[7])

#rearrange column order
col_names=list(df.columns)
new_col_order=col_names[7:9]+col_names[0:7]
df = df[new_col_order]

#=============================================#
