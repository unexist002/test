'''最小二乘法OLS车辆2003 202004061314 郝丁亮'''
import numpy as np
import matplotlib.pyplot as plt
X = np.arange(0, 15, 0.01)        #生成随机点
Z = [4 + 3 * x for x in X]      #原函数
Y = [np.random.normal(z, 0.5) for z in Z]
plt.plot(X, Y, 'ro')
plt.show()

def line(x, y):
    N = len(x)
    sumx = sum(x)
    sumy = sum(y)
    sumx2 = sum(x**2)
    sumxy = sum(x*y)
    A = np.mat([[N, sumx], [sumx, sumx2]])
    b = np.array([sumy, sumxy])
    return np.linalg.solve(A, b)

b, k = line(X, Y)

_Y = [b+ k * x for x in X]

# 生成拟合直线
plt.plot(X, Y, 'ro', X, _Y, 'b', linewidth=2)
plt.title("y = {} + {}x".format(b, k))
plt.show()