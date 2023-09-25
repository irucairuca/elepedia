import numpy as np
#微分方程式を解く用
from scipy.integrate import odeint
import matplotlib.pyplot as plt

#グラフの日本語化
import japanize_matplotlib 


R=100
L=1.0*10**-3
C=1.0*10**-6



#d2i/d2t + (R/L)di/dt +(1/CL)i=0

def func(I,t):
    dIdt=[I[1],-(R/L)*I[1]-(1/(C*L))*I[0]]
    return dIdt



if((R/(2*L))**2>1/(L*C)):
    title="振動せずに収束する"
else:
    title="振動しながら収束する"

I0 = [1,0]
#t = np.arange(0,1000*(L*C)**0.5,0.1)
t=np.linspace(0, 10*(L*C)**0.5, 1000)
I = odeint(func,I0,t) #微分方程式を解く
plt.xlabel('時間t[s]')
plt.ylabel('電流I[A]')
plt.title('RLC回路の電流特性:'+title)

plt.plot(t,I[:,0]) #グラフの作成

plt.show() #グラフの表示