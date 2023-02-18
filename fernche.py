# coding: utf-8

import math

#数値設定（力率以外単位法）
V_r=1.0
I=1.0
r=0.1
x=1.0
theta = float(input("力率を入力してください（度数）"))


#ベクトル図
V_s=((V_r+r*I*math.cos(math.radians(theta))+x*I*math.sin(math.radians(theta)))**2+(r*I*math.sin(math.radians(theta))-x*I*math.cos(math.radians(theta)))**2)**0.5


print("V_s:"+str(V_s))

V_s_kinji=V_r+r*I*math.cos(math.radians(theta))+x*I*math.sin(math.radians(theta))


print("V_s近似式計算:"+str(V_s_kinji))#近似式計算

gosa=(V_s-V_s_kinji)/V_s

print("近似式計算の誤差:"+str(gosa*100)+"[%]")


#電圧変動率
hendouritu=100*(V_s-V_r)/V_r
print("電圧変動率:"+str(hendouritu)+"[%]")


if V_s<V_r:
  print("フェランチ効果が発生した")
else:
  print("フェランチ効果が発生してない")



#相差角:当然だが、相差角が小さいほど近似式の誤差が小さくなる
print("相差角:"+str(math.degrees(math.acos(V_s_kinji/V_s))))







