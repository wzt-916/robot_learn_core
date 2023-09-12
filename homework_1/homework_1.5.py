import numpy as np

mytensor = np.random.randint(1,10,size=(3,5,5))
myarray = np.random.randint(1,10,size=(5,5))
print(mytensor)
myarray = myarray[np.newaxis,:,:]
mytensor = mytensor * myarray
print(mytensor)

#print(h)
    