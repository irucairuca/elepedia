#ログファイルの作成
import os

path = 'out_log.txt'
f = open(path, 'w')


#円周率を扱うため
import math
#ベクトルオペレーターの定義
a= math.cos(2*math.pi/3)+math.sin(2*math.pi/3)*1j
print("ベクトルオペレーター")
print(a)



#Y結線パラメーターの定義
z_a=1+1j
z_b=1+1j
z_c=1+1j

E=100
E_a=E
E_b=E*a**2
E_c=E*a

f.write("z_a="+str(z_a)+"\n") 
f.write("z_b="+str(z_b)+"\n") 
f.write("z_c="+str(z_c)+"\n") 

f.write("E_a="+str(E_a)+"\n") 
f.write("E_b="+str(E_b)+"\n") 
f.write("E_c="+str(E_c)+"\n") 

#ミルマンの定理
V=(E_a/z_a+E_b/z_b+E_c/z_c)/(1/z_a+1/z_b+1/z_c)
print("中性点電位差")
print(abs(V))


f.write("中性点電位差="+str(abs(V))+"\n") 

#相電流（線電流）
I_a=(E_a-V)/z_a
I_b=(E_b-V)/z_b
I_c=(E_c-V)/z_c

#三相電流の和は必ず０
print("三相電流の和=0")
print(abs(I_a+I_b+I_c))

f.write("三相電流の和=0"+"\n")
f.write(str(abs(I_a+I_b+I_c))+"\n")



#負荷側の有効電力

E_aa=z_a*I_a
E_bb=z_b*I_b
E_cc=z_c*I_c

#複素電力を計算する

S= E_aa*I_a.conjugate()+E_bb*I_b.conjugate()+E_cc*I_c.conjugate()

print("負荷側の有効電力")

P=S.real

print(P)
f.write("負荷側の有効電力:"+str(P)+"\n")
#負荷側の無効電力

Q=S.imag
print("負荷側の無効電力")
print(Q)
f.write("負荷側の無効電力:"+str(P)+"\n")
#2電力計法

#線間での複素電力を求める：電圧と複素共役電流の積
S_1=(E_a-E_c)*(I_a.conjugate())
S_2=(E_b-E_c)*(I_b.conjugate())

#計測される有効電力
P_1=S_1.real
P_2=S_2.real

P_c=P_1+P_2
print("計算される負荷側の有効電力")
print(P_c)
f.write("計算される負荷側の有効電力:"+str(P_c)+"\n")
#計測される無効電力



Q_c = (P_1-P_2)*3**0.5

print("計算される負荷側の無効電力(対称三相負荷のときのみ意味ある値となる)")
print(Q_c)
f.write("計算される負荷側の無効電力(対称三相負荷のときのみ意味ある値となる):"+str(Q_c)+"\n")

#計算される有効電力と実際の有効電力の差
print("計算される有効電力と実際の有効電力の差")
print(P-P_c)
f.write("計算される有効電力と実際の有効電力の差:"+str(P-P_c)+"\n")

#計算される無効電力と実際の無効電力の差
print("計算される無効電力と実際の無効電力の差(対称三相負荷のときのみ意味ある値となる)")
print(Q-Q_c)
f.write("計算される無効電力と実際の無効電力の差(対称三相負荷のときのみ意味ある値となる):"+str(Q-Q_c)+"\n")


f.close()

