

import numpy as np
import matplotlib.pyplot as plt


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




def nose_cu(X):
  P = np.arange(0.0, 1.0, 0.01)


  Q=0.0

  V_s=1.0

  #X=1.0
  Y=0.00




  #簡単のため

  alpha = Q/P


  #y=ax**2+b*x+c(x=V,y=P)

  a=(1/X-Y)**2
  b=2*P*(1/X-Y)*alpha-(V_s/X)**2
  c=(1+alpha**2)*P**2

  #安定解
  V_r_1=((-b+(b**2-4*a*c)**0.5)/2*a)**0.5
  #不安定解
  V_r_2=((-b-(b**2-4*a*c)**0.5)/2*a)**0.5




  plt.plot(P,V_r_1, 'r-')
  plt.plot(P,V_r_2,'b-')
  plt.xlim(0,0.5)
  plt.ylim(0,1)

  plt.title('ノーズカーブ,X=%f'%X,fontname="MS Gothic")
  plt.xlabel('有効電力P',fontname="MS Gothic")
  plt.ylabel('受電端電圧V_r',fontname="MS Gothic")


  #plt.show()


  #保存
  plt.savefig(f"./graphs/nose{X}.png")
  #グラフの図示
  #plt.show()
  img = Image.open(f"./graphs/nose{X}.png")
  pictures.append(img)





for i in range(1,10):
    print(i)
    X=1.0+0.1*i
    nose_cu(X)

#gifアニメを出力する
pictures[0].save('anime.gif',save_all=True, append_images=pictures[1:],
optimize=True, duration=500, loop=0)


