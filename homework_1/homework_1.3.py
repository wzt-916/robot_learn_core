import numpy as np
#产生随机数
myarray = np.random.random((10,10))
#获取行数和列数
rows,cols = myarray.shape

print(f"原来的矩阵:\n{myarray}")
#循环修改
for i in range(0,rows,1):
    for j in range(0,cols,1):
        if myarray[i][j] >= 0.5:
            myarray[i][j] = 1
        if myarray[i][j] < 0.5:
            myarray[i][j] = 0

print("修改后的矩阵:\n")
h = myarray.astype(int)
print(h)