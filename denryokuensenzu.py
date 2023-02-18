import math
import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib
PI = np.pi  # 円周率をPIで使えるようにする

# delta の範囲
delta = np.linspace(0, 2*PI, 1000000)

X= 2.0

# 関数を記述
P_r = np.sin(delta)/X
Q_r = (1-np.cos(delta))/X

P_s = np.sin(delta)/X
Q_s = (1+np.cos(delta))/X


# 軸を自動で設定する場合
#plt.gca().set_aspect('equal', adjustable='box')
# 軸を手動で設定する場合
plt.axis([-10, 10, -10, 10])

#plt.grid(which='major', color='gray', linestyle='--')
#plt.grid(which='minor', color='gray', linestyle='--')

# plt.plot(P_r, Q_r,color="red")

# #plt.grid(which='major', color='gray', linestyle='--')
# #plt.grid(which='minor', color='gray', linestyle='--')

# plt.plot(P_s, Q_s,color="blue")

plt.subplot(1, 2, 1, title="data1", xlabel="x-1", ylabel="y-1")
plt.plot(P_r, Q_r)
plt.subplot(1, 2, 2, title="data2", xlabel="x-2", ylabel="y-2")
plt.plot(P_s, Q_s)
plt.tight_layout()
plt.show()




plt.show()