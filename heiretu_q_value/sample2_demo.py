import numpy as np
import matplotlib.pyplot as plt



R=float(input("抵抗値を入力してください"))
L=float(int(input("インダクタンス(mL)を入力してください"))**(-3))
C=float(int(input("静電容量(uC)を入力してください"))*10**(-6))
V=float(100)

omega_0=1/(L*C)**0.5
q_value = R*(C/L)**0.5

print("共振角速度:%f"%omega_0)
print("Q値:%f"%q_value)


omega = np.linspace(0,10*omega_0,100)#ωの定義域

Y=((1/R)**2+(-1/(omega*L)+(omega*C))**2)**0.5#アドミタンス

I = V*Y#回路全体に流れる電流
plt.plot(omega,I)#図示
plt.title('RLC並列回路:共振周波数と電流値',fontname="MS Gothic")
plt.xlabel('角速度',fontname="MS Gothic")
plt.ylabel('電流',fontname="MS Gothic")

plt.show()