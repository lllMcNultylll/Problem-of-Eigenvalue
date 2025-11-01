
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import math




def f(x,theta):
    O_RZ = 432.8
    if x<=0.95:
        O_CZ = 470.308 - 62.79*np.cos(theta)**2 - 67.87*np.cos(theta)**4
    else:
        O_CZ = 470.308 - 62.79*np.cos(theta)**2 - 67.87*np.cos(theta)**4 - 16.808*(x-0.95)*20
    O1 = 0.5*(1+math.erf((x-0.7)/0.04))

    ans = ( O_RZ + (O_CZ - O_RZ) * O1 )*2*math.pi
    

    return ans



x = np.linspace(0.6,1,100)
theta = np.linspace(0,np.pi,100)
xL, thetaL = np.meshgrid( x, theta )
a,b=xL.shape
O = np.zeros((a,b))
M = np.zeros((a,b))
N = np.zeros((a,b))
for i in range(a):
    for j in range(b):
        x=xL[i][j]
        theta=thetaL[i][j]
        O[i][j] = f(x,theta)
        M[i][j] = x*np.cos(theta)
        N[i][j] = x*np.sin(theta)







fig = plt.figure()
# ax = Axes3D(fig)
# fig.add_axes(ax)
ax = fig.add_subplot(111, projection='3d')

# plt.rcParams['font.sans-serif']=['FangSong'] # 用来正常显示中文标签
# plt.rcParams['axes.unicode_minus']=False # 用来正常显示负号

ax.plot_surface(M,N,O, rstride=1, cstride=1, cmap=plt.get_cmap('rainbow'))
ax.set_xlabel('X')
ax.set_ylabel('Y')  
plt.show()

