# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 15:35:28 2021

@author: Kevin Duran
"""

import pandas as pd #Manejo de DataFrames 
import numpy as np #Manejo de Arrays para cálculo númerico
import matplotlib.pyplot as plt #Gráficos
import seaborn as sns #Gráficos y analisis de datos

Concrete_Data=pd.read_csv('Concrete_Data.csv',delimiter=';')
text1='Relación lineal y directamente proporcional (si una variable aumenta, entonces la otra ariable también)'
text2='cantidad de cemento por m3, la resistencia del concreto y la edad'
sns.scatterplot(x='Cement (component 1)(kg in a m^3 mixture)', y='Concrete compressive strength(MPa, megapascals) ', data=Concrete_Data,hue='Age (day)')
print('Se puede notar una %s entre la %s. '%(text1, text2))
#%%
fig=sns.boxplot(x='Age (day)', y='Concrete compressive strength(MPa, megapascals) ', data=Concrete_Data)
Description1=Concrete_Data.groupby(["Age (day)"])["Concrete compressive strength(MPa, megapascals) "].describe()
print('Se puede notar los concretos que alcanzaron una mayor resistencia fueron ensayados a los 90 días')
#%%'
Data=pd.read_csv('PRSA_data_2010.1.1-2014.12.31.csv')
sns.barplot(x='month', y='pm2.5', data=Data, hue='year')
Description2=Data.groupby(["year"])["pm2.5"].describe()
print('Del grafico podemos concluir que el pm2.5 más alto que se registró fue el del mes 1 del año 2013')
#%%
sns.boxplot(x='year', y='pm2.5', data=Data)
Description3=Data.groupby(["year"])["pm2.5"].describe()
print('Desde el 2010 hasta el 2014 los datos medidos se mantuvieron con una media cercana a las 100 unidades de pm2.5, con valores muy altos en muchos días considerados atípicos')