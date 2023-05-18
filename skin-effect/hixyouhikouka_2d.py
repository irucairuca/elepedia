import matplotlib.pyplot as plt
import math 
import numpy as np
#ベッセル関数の読み込み
from scipy.special import jv

#円筒銅線の材料パラメーター

#電気伝導率σ
sigma = 1.0
#透磁率μ
mu = 1.0

#角周波数
omega = 10
#電流値
I=1.0
#銅線の半径
r_0=100
k= (-1j*omega*mu*sigma)**0.5
r = np.linspace(-1*r_0,r_0,100)
#電流密度（rの関数）
y = (k*I/(2*math.pi))*jv(0,k*r)/jv(1,k*r_0)

plt.plot(r,y)
plt.show()