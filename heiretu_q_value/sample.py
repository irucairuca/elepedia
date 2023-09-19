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



def qr(R):
  L=100*10**(-3)
  omega_0=2000

  C=1/(L*omega_0**2)


  V=float(100)

  #omega_0=1/(L*C)**0.5
  q_value = R*(C/L)**0.5

  #print("共振角速度:%f"%omega_0)
  #print("Q値:%f"%q_value)


  omega = np.linspace(0,10*omega_0,100)#ωの定義域

  Y=((1/R)**2+(-1/(omega*L)+(omega*C))**2)**0.5#アドミタンス

  I = V*Y#回路全体に流れる電流
  plt.plot(omega,I)#図示
  plt.title('RLC並列回路:共振周波数と電流値_Q値:%f' %q_value,fontname="MS Gothic")
  plt.xlabel('角速度',fontname="MS Gothic")
  plt.ylabel('電流',fontname="MS Gothic")

  #plt.show()

  #保存
  plt.savefig(f"./graphs/q_vqlue_tixyokuretu{R}.png")
  #グラフの図示
  #plt.show()
  img = Image.open(f"./graphs/q_vqlue_tixyokuretu{R}.png")
  pictures.append(img)




for R in range(1,100):
    print(R)
    qr(R*100)

#gifアニメを出力する
pictures[0].save('anime.gif',save_all=True, append_images=pictures[1:],
optimize=True, duration=500, loop=0)
