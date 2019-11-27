import numpy as np

data = np.loadtxt('./data/inflammation-01.csv', delimiter = ',')
print (data.shape) # outputs the dimensions of the n-dimensional array
print (np.mean(data)) # outputs the mean of the whole data

patient_0 = data[0, : ] # 1st row 
print (np.mean(patient_0))
print('maximum inflammation for patient 0:', np.max(patient_0))