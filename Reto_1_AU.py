import pandas as pd
import matplotlib.pyplot as plt

Data1 = pd.read_csv('winequality-red.csv', delimiter= ';')
Data2 = pd.read_csv('winequality-white.csv', delimiter= ';')

redmean = []
whitemean = []
print ('   Red data', '       White data')
for i in range(len(Data1.columns)):
    redmean= Data1.mean()
    if Data2.columns.all() == Data1.columns.all():
       whitemean= Data2.mean() 
    else:
        print('Review row names to compare')
    print(Data1.columns[i])
    print (redmean[i], whitemean[i])
    print ('-'*50) 

plt.figure()
plt.title('Comparison Red Wine')
plt.rcParams['axes.facecolor'] = 'snow'
plt.scatter(Data1['fixed acidity'], Data1['citric acid'], marker='.', c='rosybrown')
plt.ylabel('Citric acid')
plt.xlabel('Fixed acidity')
plt.show()

plt.figure()
plt.title('Comparison White Wine')
plt.rcParams['axes.facecolor'] = 'snow'
plt.scatter(Data2['fixed acidity'], Data2['citric acid'], marker='.', c='springgreen')
plt.ylabel('Citric acid')
plt.xlabel('Fixed acidity')
plt.show()


plt.figure()
plt.title('Means Comparison')
plt.rcParams['axes.facecolor'] = 'lightcyan'
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
    