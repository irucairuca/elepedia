import numpy as np
import matplotlib.pyplot as plt

PI = np.pi  # 円周率をPIで使えるようにする

#ディレクトリ生成用
import os

import japanize_matplotlib

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



def den_en(i):
  X=i*0.1
  fig, ax = plt.subplots()

  # delta の範囲
  delta = np.linspace(0, 2*PI, 10000)

  #X= 1.0


  E_s=1.0
  E_r=1.0

  #送電端電圧の複素表示
  E_s1=E_s*(np.cos(delta)+1j*np.sin(delta))

  I=(E_s1-E_r)/(1j*X)


  #共役複素電流
  I_var=I.conjugate()
  #受電端、送電端複素電流
  S_r=E_r*I_var
  S_s=E_s1*I_var
  #実部、虚部の分解
  P_r=S_r.real
  Q_r=S_r.imag

  P_s=S_s.real
  Q_s=S_s.imag






  # 関数を記述
  # P_r = np.sin(delta)/X
  # Q_r = (1-np.cos(delta))/X

  # P_s = np.sin(delta)/X
  # Q_s = (-1+np.cos(delta))/X

  c1,c2 = "blue","green"    # 各プロットの色
  l1,l2 = "送電円","受電円"  # 各ラベル

  ax.set_xlabel('有効電力')  # x軸ラベル
  ax.set_ylabel('無効電力')  # y軸ラベル
  ax.set_title("電力円線図:インダクタンスのみ:X=%f"%X) # グラフタイトル
  ax.set_aspect('equal') # スケールを揃える
  ax.grid()            # 罫線
  ax.set_xlim([-10, 10]) # x方向の描画範囲を指定
  ax.set_ylim([-10, 10])    # y方向の描画範囲を指定
  ax.plot(P_r, Q_r, color=c1, label=l1)
  ax.plot(P_s, Q_s, color=c2, label=l2)

  ax.legend(loc=0)    # 凡例
  fig.tight_layout()  # レイアウトの設定
  # plt.savefig('hoge.png') # 画像の保存
  #plt.show()


  #plt.show()

  #保存
  path=f"./graphs/den_en{X}.png"
  plt.savefig(path)
  #グラフの図示
  #plt.show()
  img = Image.open(path)
  pictures.append(img)




for i in range(1,100):
    print(i)
    #X=i*0.1
    den_en(i)

#gifアニメを出力する
pictures[0].save('anime.gif',save_all=True, append_images=pictures[1:],
optimize=True, duration=500, loop=0)
