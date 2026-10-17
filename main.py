from scipy.io import loadmat
import matplotlib.pyplot as plt

data = loadmat("piv0_copy.mat")   
img = data["pivw"]              

plt.imshow(img)                  
plt.show()