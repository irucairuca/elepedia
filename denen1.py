"""複数のグラフを重ねて描画するプログラム"""
import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib
import math #度数法を使用できるようにする
PI = np.pi  # 円周率をPIで使えるようにする



fig, ax = plt.subplots()

# delta の範囲
delta = np.linspace(0, 2*PI, 1000000)
alpha= math.radians(int(input("インピーダンス角を入力してください")))
Z= 1.0

E_s=1.0
E_r=1.0



# 関数を記述
P_s = E_s**2*np.cos(alpha)/Z-E_s*E_r*np.cos(delta+alpha)/Z
Q_s =  E_s**2*np.sin(alpha)/Z-E_s*E_r*np.sin(delta+alpha)/Z

P_r =  -E_r**2*np.cos(alpha)/Z-E_s*E_r*np.cos(-delta+alpha)/Z
Q_r = -E_r**2*np.sin(alpha)/Z+E_s*E_r*np.sin(-delta+alpha)/Z

c1,c2 ,c3= "blue","green","red"    # 各プロットの色
l1,l2 ,l3= "送電円","受電円","直線軸"  # 各ラベル

ax.set_xlabel('有効電力')  # x軸ラベル
ax.set_ylabel('無効電力')  # y軸ラベル
ax.set_title("電力円線図:一般角の送電インピーダンスの場合") # グラフタイトル
ax.set_aspect('equal') # スケールを揃える
ax.grid()            # 罫線
#ax.set_xlim([-10, 10]) # x方向の描画範囲を指定
#ax.set_ylim([0, 1])    # y方向の描画範囲を指定
ax.plot(P_r, Q_r, color=c1, label=l1)
ax.plot(P_s, Q_s, color=c2, label=l2)

#軸となる直線の描写

x = np.arange(-2.0, 2.0, 0.02)
plt.plot(x,np.tan(alpha)*x, color=c3, label=l3)



ax.legend(loc=0)    # 凡例
fig.tight_layout()  # レイアウトの設定
# plt.savefig('hoge.png') # 画像の保存
plt.show()