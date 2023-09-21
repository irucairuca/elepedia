import numpy as np
import matplotlib.pyplot as plt
import math




#ディレクトリ生成用
import os


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






#パラメーター設定
#極数
p=4
#周波数
f=50
#2次電圧
E_2=100.0
#2次抵抗とインダクタンス

#r_2=5.0
x_2=10.0

def torque(r_2):
  #滑りの範囲の指定
  s = np.arange(-1.0, 2.0, 0.02)
  #トルクの式
  T=(p/(4*math.pi*f))*(((E_2**2*(r_2/s))/((r_2/s)**2+x_2**2)))

  fig, ax = plt.subplots()



  # x 軸のラベルを設定する。
  ax.set_xlabel("滑りs", fontname="MS Gothic")

  # y 軸のラベルを設定する。
  ax.set_ylabel("トルクT", fontname="MS Gothic")

  # タイトルを設定する。
  ax.set_title("トルクと滑りの関連式:二次抵抗%f"%r_2, fontname="MS Gothic")

  #x軸の反転
  ax.invert_xaxis()
  ax.plot(s, T)
  ax.grid()

  plt.savefig(f"./graphs/hireisuii{r_2}.png") # 画像の保存

  #plt.show()

  img = Image.open(f"./graphs/hireisuii{r_2}.png")
  pictures.append(img)




for i in range(1,100):
    print(i)
    r_2=i*0.1
    torque(r_2)

#gifアニメを出力する
pictures[0].save('anime.gif',save_all=True, append_images=pictures[1:],
optimize=True, duration=500, loop=0)

