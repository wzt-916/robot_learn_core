import numpy as np
#产生随机数
myarray = np.random.randint(1,10,size=(10,10))
#求每列的均值
mymean = np.mean(myarray,axis = 0)
print(f'每列的均值:\n{mymean}')
mystd = np.std(myarray,axis = 0)
print(f"每列的标准差:\n{mystd}")