import numpy as np
import matplotlib.pyplot as plt
#円周率の読み込み
import math 
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
r_0=10


x = np.arange(-1*r_0,r_0 , 0.2) #x軸の描画範囲の生成。0から10まで0.05刻み。
y = np.arange(-1*r_0,r_0 , 0.2) #y軸の描画範囲の生成。0から10まで0.05刻み。



k= complex((-1j*omega*mu*sigma)**0.5)


#print(k)
X, Y = np.meshgrid(x, y)
r=np.sqrt(X**2+Y**2) #半径の定義

Z =k*I/(2*math.pi)* jv(0,k*r)/jv(1,k*r_0) # 表示する計算式の指定。等高線はZに対して作られる。
print(Z)
plt.pcolormesh(X, Y, Z, cmap='hsv') # 等高線図の生成。cmapで色付けの規則を指定する。
#plt.pcolor(X, Y, Z, cmap='hsv') # 等高線図の生成。cmapで色付けの規則を指定する。

pp=plt.colorbar (orientation="vertical") # カラーバーの表示 
pp.set_label("Label", fontname="Arial", fontsize=24) #カラーバーのラベル

plt.xlabel('X', fontsize=24)
plt.ylabel('Y', fontsize=24)

plt.show()