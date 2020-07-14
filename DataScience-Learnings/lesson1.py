import numpy as np

data = np.loadtxt('./data/inflammation-01.csv', delimiter = ',')
print (data.shape) # outputs the dimensions of the n-dimensional array
print (np.mean(data)) # outputs the mean of the whole data

print(data[1:3, 0:10]) #outputs the 2nd and 3rd row and upto 10th columns
patient_0 = data[0, : ] # 1st row 
print (np.mean(patient_0))
print('maximum inflammation for patient 0:', np.max(patient_0))

print(np.mean(data, axis = 1)) #outputs the mean of axis 1 (rows)