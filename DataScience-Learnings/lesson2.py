import matplotlib.pyplot as plot
import numpy as np

data = np.loadtxt('./data/inflammation-01.csv', delimiter = ',')
#image = plot.imshow(data) #show heatmap
#plot.show()

avg = plot.plot(np.mean(data, axis = 0)) #show average per day
plot.show()