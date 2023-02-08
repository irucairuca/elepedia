# -*- coding: utf-8 -*-
#一次遅れ系
from scipy import signal
import matplotlib.pyplot as plt


T=float(input("時定数を入力してください"))
print("折点周波数における角速度:"+str(1/T)+"[rad/sec]")

# 伝達関数の定義
num = [1] # 分子の係数
den = [T, 1] # 分母の係数
G = signal.lti(num, den)

# ボード線図の計算
w, mag, phase = signal.bode(G)

# ゲイン線図の描画
plt.subplot(2, 1, 1)
plt.semilogx(w, mag)
plt.ylabel("Gain[dB]")
plt.grid()

# 位相線図の描画
plt.subplot(2, 1, 2)
plt.semilogx(w, phase)
plt.xlabel("w[rad/sec]")
plt.ylabel("Phase[deg]")
plt.grid()
plt.show()