import numpy as np
import sys 

x = [i for i in range(256)]
np.random.shuffle(x)
x = bytes(x)
# convert into bytes 

fileName = sys.argv[1]

with open(fileName, "wb") as binary_file:
   
    # Write bytes to file
    binary_file.write(x)