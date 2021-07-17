# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 14:35:09 2021

@author: CESAR AUGUSTO PAJARO
"""
#clave importar + Nombre de la Libreria + as + como la vas a llamar
import numpy as np #Manejo de Arrays Calculo Numérico
import pandas as pd #Manejo de DataFrames

#Si el archivo esta en la misma carpeta
df_sismos_hist = pd.read_csv('Sismos Historicos_UPd.csv') 
df_sismos_hist_np = np.loadtxt('Sismos Historicos_UPd_SN.csv', skiprows=1,
                               delimiter=',')

#Si el archivo no esta en la misma carpeta se le coloca a la ruta doble '\\'
df_sismos_hist = pd.read_csv('C:\\Users\\CESAR AUGUSTO PAJARO\\Desktop\\t\\Sismos Historicos_UPd.csv') 



#%%
A = 90
#indexación en pandas.
print('-'*50)
print(df_sismos_hist.iloc[:,5])
print('-'*50)
print(df_sismos_hist['Magnitud [Mw]'])
print('-'*50)

print(df_sismos_hist.iloc[15,5]) #En vez de esto
print(df_sismos_hist['Magnitud [Mw]'].iloc[15]) #ESTO
print('-'*50)

#indexación en numpy.
print(df_sismos_hist_np[0:21,3])

#%%
print('-'*50)
a = [10,20,30,40,5,60,7,80,90]
for el in range(len(a)):
    print(el)
    print(a[el])

print('-'*50)
#%%

for el in a:
    print(el
          
          
#%%
sw = 1;
sd = 1;
if sw and sd : 
    print('Si')
else:
    print('No')
    
#%%

   