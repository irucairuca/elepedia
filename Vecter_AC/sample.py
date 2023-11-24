import numpy as np
import matplotlib.pyplot as plt



#ディレクトリ生成用
import os

#ベクトル描写用
import matplotlib.pyplot as plt
import japanize_matplotlib
import math


#ライブラリのインポート
from PIL import Image
#画像を入れる箱を準備
pictures=[]
#画像を箱に入れていく



#gjfを生成するための画像を保存する為のディレクトリを無い場合は新規に作成する


 
SAMPLE_DIR = "./graphs"
 
if not os.path.exists(SAMPLE_DIR):
    # ディレクトリが存在しない場合、ディレクトリを作成する
    os.makedirs(SAMPLE_DIR)



# ベクトルを表示
# quiver(始点x,始点y,成分x,成分y)
I=1.0
#受電端電圧
V_r=1.0
#送電線の抵抗値
r=1
#送電線のインダクタンス
x=1

def vector(theta):
  # 5×5サイズのFigureを作成してAxesを追加
  fig = plt.figure(figsize = (5, 5))
  ax = fig.add_subplot(111)

  # 格子点を表示
  ax.grid()

  # 軸ラベルの設定
  ax.set_xlabel("実軸", fontsize = 16)
  ax.set_ylabel("虚軸", fontsize = 16)

  # 軸範囲の設定
  ax.set_xlim(0,3)
  ax.set_ylim(-3,3)

  # x軸とy軸
  ax.axhline(0, color = "gray")
  ax.axvline(0, color = "gray")

  #力率角
  theta = math.radians(theta)
  #複素電流
  I_bar=I*(np.cos(theta)-1j*np.sin(theta))

  #送電端電圧
  V_s=V_r+ (r+1j*x)*I_bar


  #電流ベクトル
  ax.quiver(0, 0, I_bar.real, I_bar.imag, color = "red",
            angles = 'xy', scale_units = 'xy', scale = 1)

  #受電電圧（位相の基準）


  #受電電圧（位相の基準）
  ax.quiver(0, 0, V_r.real, V_r.imag, color = "black",
            angles = 'xy', scale_units = 'xy', scale = 1)




  #抵抗にかかる電圧

  ax.quiver(V_r, 0, (r*I_bar).real, (r*I_bar).imag, color = "blue",
            angles = 'xy', scale_units = 'xy', scale = 1)



  #インダクタンスにかかる電圧

  ax.quiver((V_r+r*I_bar).real, (V_r+r*I_bar).imag, (1j*x*I_bar).real, (1j*x*I_bar).imag, color = "yellow",
            angles = 'xy', scale_units = 'xy', scale = 1)



  #送電端電圧ベクトル
  ax.quiver(0,0, V_s.real, V_s.imag, color = "pink",
            angles = 'xy', scale_units = 'xy', scale = 1)


  #plt.show()

  #plt.show()
  Path =f"./graphs/vector_AC_{theta}.png"
  #保存
  plt.savefig(Path)
  #グラフの図示
  #plt.show()
  img = Image.open(Path)
  pictures.append(img)




for i in range(1,100):
    print(i)
    theta = 30-1.2*i
    vector(theta)

#gifアニメを出力する
pictures[0].save('anime.gif',save_all=True, append_images=pictures[1:],
optimize=True, duration=500, loop=0)