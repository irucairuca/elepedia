import numpy as np
import matplotlib.pyplot as plt
import math

R=int((input("抵抗値を入力してください")))
X_L=int((input("インダクタンスを入力してください")))
X_C=int((input("キャパシタンスを入力してください")))
V=100

a=float((X_L-X_C)/R)

x = np.arange(-5, 5, 0.1)
y1 = V*np.sin(x)
y2 = V*np.sin(x+math.atan(a))/(R**2+(X_L-X_C)**2)**0.5
 
plt.title("交流：直列RCL回路における電流特性", fontname="MS Gothic")#日本語化
plt.xlabel("time")
plt.ylabel("size")
 
plt.plot(x, y1, label="V",)   # labelに凡例に表示する文字を指定
plt.plot(x, y2, label="I")
plt.legend()                     # 凡例を表示
 
plt.xlim(-np.pi, np.pi)
plt.ylim(-1.2*V,   1.2*V)
 
plt.show()