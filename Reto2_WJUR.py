# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 07:34:16 2021

@author: HP User
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#%%
#Concrete compressive strength
df = pd.read_csv('Concrete_Data.csv', delimiter=';')

#%%
#Correlación entre la adición de Fly Ash y la resistencia a la compresión del concreto
fig, axs = plt.subplots(1,3, figsize=(20,6))
sns.scatterplot(x = 'Fly Ash (component 3)(kg in a m^3 mixture)', 
                y = 'Concrete compressive strength(MPa, megapascals) ', 
                data = df, hue = 'Age (day)', ax=axs[0])
axs[0].set_title('Efecto de la adición de FA en la resistencia a la compresión', size=12)

#%%
#Correlación entre la adición de Slag y la resistencia a la compresión del concreto
sns.scatterplot(x = 'Blast Furnace Slag (component 2)(kg in a m^3 mixture)', 
                          y = 'Concrete compressive strength(MPa, megapascals) ', 
                          data = df, hue = 'Age (day)', ax=axs[1])
axs[1].set_title('Efecto de la adición de slag en la resistencia a la compresión', size=12)

#%%
#Concrete compressive strength
slump_data = pd.read_csv('slumpdata.csv', delimiter = ';')
#%%
#Correlación entre la cantidad de agua de la mezcla y el slump
sns.scatterplot(x = 'Water', y = 'SLUMP(cm)', data = slump_data, ax=axs[2])
axs[2].set_title('Correlación entre la cantidad de agua de la mezcla y el slump', size=12)
