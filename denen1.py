"""複数のグラフを重ねて描画するプログラム"""
import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib
PI = np.pi  # 円周率をPIで使えるようにする



fig, ax = plt.subplots()

# delta の範囲
delta = np.linspace(0, 2*PI, 1000000)
pusai = 0
Z= .0

# 関数を記述
P_r = np.sin(delta)/X
Q_r = (1-np.cos(delta))/X

P_s = np.sin(delta)/X
Q_s = (-1+np.cos(delta))/X

c1,c2 = "blue","green"    # 各プロットの色
l1,l2 = "送電円","受電円"  # 各ラベル

ax.set_xlabel('有効電力')  # x軸ラベル
ax.set_ylabel('無効電力')  # y軸ラベル
ax.set_title("電力円線図:インダクタンスのみ") # グラフタイトル
ax.set_aspect('equal') # スケールを揃える
ax.grid()            # 罫線
#ax.set_xlim([-10, 10]) # x方向の描画範囲を指定
#ax.set_ylim([0, 1])    # y方向の描画範囲を指定
ax.plot(P_r, Q_r, color=c1, label=l1)
ax.plot(P_s, Q_s, color=c2, label=l2)

ax.legend(loc=0)    # 凡例
fig.tight_layout()  # レイアウトの設定
# plt.savefig('hoge.png') # 画像の保存
plt.show()