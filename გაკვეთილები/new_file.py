import matplotlib.pyplot as plt 
import numpy as np

list_of_x = np.array([0, 0, 0.4, 0.4, 0, 0, 0.20, 0.40  ])
list_of_y = np.array([0, 3.90, 3.90, 0, 0, 3.90, 5.5, 3.90])

plt.plot(list_of_x, list_of_y)

plt.show()
