"""
2本の電線の周辺に生じる磁場
"""

import numpy as np
import matplotlib.pyplot as plt
import math
plt.figure()


LX, LY=3,3

gridwidth=0.3 
X, Y= np.meshgrid(np.arange(-LX, LX, gridwidth), np.arange(-LY, LY,gridwidth)) 

n=10
x=np.linspace(-2,+2,n)
d=1.5
zp=np.zeros(n)
zp2=np.zeros(n)
for i in range(n):
    zp[i]=x[i]    
    plt.plot(x[i],0,'o',color='blue')

    plt.plot(x[i],d,'o',color='blue')



I=1
print()
x=[]
y=[]
u=[]
v=[]

z=0

for i in range(len(X)):
    for k in range(len(X)):
        x=X[i][k]
        y=Y[i][k]
        z=x+1j*y
        
     
        #H=I1/(2*math.pi*abs(z_1))*((-1j)*z_1/abs(z_1)) +I2/(2*math.pi*abs(z_2))*((-1j)*z_2/abs(z_2))
        H=0
        for p in range(len(zp)):
            z_1=z-zp[p]
            z_2=z-(zp[p]+d*1j)
            H=H+I/(2*math.pi*abs(z_1))*((-1j)*z_1/abs(z_1)) -I/(2*math.pi*abs(z_2))*((-1j)*z_2/abs(z_2)) 
        u=H.real
        v=H.imag
        
        plt.quiver(x,y,u,v,color='red',angles='xy',scale_units='xy', scale=4.5)


plt.xlim([-LX,LX])
plt.ylim([-LY,LY])

# グラフ描画
plt.grid()
plt.draw()
plt.savefig("solenoid.png")
plt.show()