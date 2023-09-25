
#ディレクトリ生成用
import os

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
#グラフの日本語化
import japanize_matplotlib 


#ライブラリのインポート
from PIL import Image
#画像を入れる箱を準備
pictures=[]
#画像を箱に入れていく




#R=100
L=1.0*10**-3
C=1.0*10**-6
 
#gjfを生成するための画像を保存する為のディレクトリを無い場合は新規に作成する


 
SAMPLE_DIR = "./graphs"
 
if not os.path.exists(SAMPLE_DIR):
    # ディレクトリが存在しない場合、ディレクトリを作成する
    os.makedirs(SAMPLE_DIR)






#d2i/d2t + (R/L)di/dt +(1/CL)i=0

def func(I,t):
    dIdt=[I[1],-(R/L)*I[1]-(1/(C*L))*I[0]]
    return dIdt

def rlc(R):
    if((R/(2*L))**2>1/(L*C)):
        title="振動せずに収束する"
    else:
        title="振動しながら収束する"

    I0 = [1,0]
    #t = np.arange(0,1000*(L*C)**0.5,0.1)
    t=np.linspace(0, 10*(L*C)**0.5, 1000)
    I = odeint(func,I0,t) #微分方程式を解く
    plt.xlabel('時間t[s]')
    plt.ylabel('電流I[A]')
    plt.title('RLC回路の電流特性:'+title)



    plt.plot(t,I[:,0]) #グラフの作成

    #plt.show() #グラフの表示
    #保存
    path=f"./graphs/rlc_{R}.png"
    plt.savefig(path)
    #グラフの図示
    #plt.show()
    img = Image.open(path)
    pictures.append(img)
    plt.close()


for R in range(0,100):
    print(R)
    rlc(R)

#gifアニメを出力する
pictures[0].save('anime.gif',save_all=True, append_images=pictures[1:],
optimize=True, duration=500, loop=0)

