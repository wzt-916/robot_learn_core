import numpy as np
a = np.random.randint(0,100,size = (10,10))
print(f"随机产生的矩阵是\n{a}")
my_max = np.amax(a,axis = 0)
print(f"每一列的最大数是{my_max}")