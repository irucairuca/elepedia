from scipy import signal#方形波を作るのに使用
import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib
import math
V=1

n= int(input("和の回数を入力してください"))


x = np.arange(0.0, 2*math.pi, 0.02)
y=0

for num in range(n):
    y=y+(1/(2*num+1))*np.sin((2*num+1)*x)

y=y*(4*V/math.pi)

plt.plot(x, y,color="red", label="フーリエ変換")


y2 = signal.square(x)

plt.plot(x, y2,color="blue", label="方形波")
plt.title('フーリエ変換:方形波,n='+str(num+1))
plt.legend() #凡例

#グラフを画像として保存
plt.savefig('フーリエ変換' +str(num+1)+ ".png")

plt.show()


