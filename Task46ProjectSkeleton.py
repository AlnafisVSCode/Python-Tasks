import numpy as np



myDigits = np.load('myDigitsDataset.npy')
print("The type of 'myDigits' is", type(myDigits))
print("The array 'myDigits' consists of elements of type", myDigits.dtype)
print("The array 'myDigits' has", myDigits.ndim, "dimensions")
print("The shape of 'myDigits' is", myDigits.shape)