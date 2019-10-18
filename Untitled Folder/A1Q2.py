import os
import PIL
from PIL import Image
import glob
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import imshow

def main():
  g=os.getcwd()+"\\"+"*.jpg"
  print(g)
  new_width  = 200
  new_height = 200
  size=(new_width, new_height)
  X_data = np.empty([20,200,200,3], dtype = int)
  files = glob.glob (g)
  m=0
  for myFile in files:
    image = Image.open(myFile)
    
    image=image.resize(size)
    X_data[m]=image
    m=m+1
    for img in X_data:
      plt.figure()
      plt.imshow(img)


if __name__ == "__main__":
    main()
   

    

    
    
    

    
    
    
    
    
    
    
#print('X_data shape:', np.array(X_data).shape)