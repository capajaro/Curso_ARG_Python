import pandas as pd
import matplotlib.pyplot as plt

Data1 = pd.read_csv('winequality-red.csv', delimiter= ';')
Data2 = pd.read_csv('winequality-white.csv', delimiter= ';')

redmean = []
whitemean = []


redmean= Data1.mean()
whitemean= Data2.mean() 
if Data2.columns.all() == Data1.columns.all():
    for i in range (len(Data1.columns)):
        print(Data1.columns[i])
        print ('   Red data', '       White data')
        print (redmean[i], whitemean[i])
        print ('-'*50) 
else:
    print('Review row names to compare')


plt.figure(facecolor= 'snow') #facecolor cambia color del fondo
plt.title('Comparison Red Wine')
plt.scatter(Data1['fixed acidity'], Data1['citric acid'], marker='.', c='rosybrown')
plt.ylabel('Citric acid')
plt.xlabel('Fixed acidity')
plt.show()

plt.figure(facecolor= 'snow')
plt.title('Comparison White Wine')
plt.scatter(Data2['fixed acidity'], Data2['citric acid'], marker='.', c='springgreen')
plt.ylabel('Citric acid')
plt.xlabel('Fixed acidity')
plt.show()

plt.figure()
plt.title('Means Comparison')
plt.rcParams['axes.facecolor'] = 'snow' #cambia todo el entorno
plt.scatter(redmean[:], Data1.columns, marker='p', c='darkred', label='Red wine')
plt.scatter(whitemean[:], Data1.columns,marker = '*', c='antiquewhite', label='White wine')
plt.ylabel('Comparison variables')
plt.xlabel('Means')
plt.legend()
plt.show()

## Variables error
E = []
for j in range (len(redmean)):
    E  = abs(redmean-whitemean)
        
print ('Comparing RED and WHITE wines, errors are:\n', E )
