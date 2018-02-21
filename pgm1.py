# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 21:14:38 2018

@author: Dell
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

chronic_ill1= pd.read_csv('F:\machine learning\health analytics kaggle india\Key_Indicator_State_and_District_wise_data\KK_Chronic_Illness_District.csv')
#print(chronic_ill1.head(n=5))
#print(chronic_ill1.describe())
print(chronic_ill1.index)
print (type(chronic_ill1))
#print(chronic_ill1.columns)
print(chronic_ill1.shape)
chronic_ill1.columns=['state','Distt','PPT','PPR','PPU','PMT','PMR','PMU','PFT','PFR','PFU','MCPT','MCPR','MCPU','MCMT','MCMR','MCMU','MCFT','MCFR','MCFU','PDPT','PDPR','PDPU','PDMT','PDMR','PDMU','PDFT','PDFR','PDFU','PHPT','PHPR','PHPU','PHMT','PHMR','PHMU','PHFT','PHFR','PHFU','PTbPT','PTbPR','PTbPU','PTbMT','PTbMR','PTbMU','PTbFT','PTbFR','PTbFU','PRPT','PRPR','PRPU','PRMT','PRMR','PRMU','PRFT','PRFR','PRFU','PAPT','PAPR','PAPU','PAMT','PAMR','PAMU','PAFT','PAFR','PAFU','ACIPT','ACIPR','ACIPU','ACIMT','ACIMR','ACIMU','ACIFT','ACIFR','ACIFU','RTPT','RTPR','RTPU','RTMT','RTMR','RTMU','RTFT','RTFR','RTFU','RTGSPT','RTGSPR','RTGSPU','RTGSMT','RTGSMR','RTGSMU','RTGSFT','RTGSFR','RTGSFU']
print(chronic_ill1.head(n=5))
#plt.plot(chronic_ill1.state, chronic_ill1.PPT,marker='x')

##A scatter plot between feature of state and chronic illness seeking medical care female total in 100000
##kk_chronic_illness_state.cs is used
np.random.seed(19680801)
N=284
colors=np.random.rand(N)
area= np.pi*(15*np.random.rand(N))**2
plt.figure(figsize=(20,10))
plt.scatter(chronic_ill1.state, chronic_ill1.MCFT,s=area,c=colors,alpha=0.5)

