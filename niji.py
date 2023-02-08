# -*- coding: utf-8 -*-

#2次元遅れ系
from scipy import signal
import matplotlib.pyplot as plt


jita=float(input("減衰係数"))
omega_n=float(input("共振角周波数"))

# 伝達関数の定義
num = [omega_n] # 分子の係数
den = [1,2*jita*omega_n ,omega_n**2] # 分母の係数
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