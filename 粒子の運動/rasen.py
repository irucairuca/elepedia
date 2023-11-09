import numpy as np
import matplotlib.pyplot as plt

#パラメータ
B=np.array([0,0,1])
q=1.0
m=1.0
#初期条件 (x,v,a)=(位置,速度,加速度)
x=np.array([1,0,0])
#斜め上に発射
v=np.array([0,1,1])

#a=np.array([-1,0,0])

#3次元のグラフ（散布図）を描くための設定
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

#初期時間
t=0
#微小時間の時間間隔(小さくするほど精度は上がるが計算時間が比例して増大する)
delta_t=0.01
while(t<10):
    #ローレンツ力によって生じる加速度,cross(v,B)はvとBの外積である
    a=-(q/m)*np.cross(v, B)
    #速度の微小変化
    v=v+a*delta_t
    #位置の微小変化
    x=x+v*delta_t
    #時間の更新
    t=t+delta_t
    #print(x)
    #粒子の位置を記録
    ax.scatter(x[0], x[1], x[2], color='blue')
#グラフを保存する
plt.savefig("rasen.png")
#グラフの表示
plt.show()
