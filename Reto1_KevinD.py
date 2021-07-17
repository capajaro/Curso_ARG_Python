# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd #Manejo de DataFrames 
import numpy as mp #Manejo de Arrays para cálculo númerico
import matplotlib.pyplot as plt #Gráficos
import seaborn as sbn #Gráficos y analisis de datos

Wine_Quality_red=pd.read_csv('C:\\Users\\Kevin Duran\\Documents\\GitHub\\Curso_ARG_Python\\winequality-red.csv')

Wine_Quality_white=pd.read_csv('C:\\Users\\Kevin Duran\\Documents\\GitHub\\Curso_ARG_Python\\winequality-white.csv')
dfw=pd.DataFrame(Wine_Quality_white)
dfr=pd.DataFrame(Wine_Quality_red)
Columns=["fixed acidity","volatile acidity","citric acid","residual sugar","chlorides","free sulfur dioxide","total sulfur dioxide","density","pH","sulphates","alcohol","quality"]
mean_dfr=dfr[Columns].mean() 
print('-'*50)
print("El promedio para cada una de las de los parametros medidos en el vino rojo es: ")
print(mean_dfr)
print('-'*50)
mean_dfw=dfw[Columns].mean() 
print("El promedio para cada una de las de los parametros medidos en el vino blanco es: ")
print(mean_dfw)
print('-'*50)
Deltamu=abs(mean_dfw-mean_dfr)
print("El delta de las variables entre entre el vino blanco y el rojo es: ")
print (Deltamu)
dfr.groupby('citric acid').mean()["residual sugar"].plot(kind="bar")
