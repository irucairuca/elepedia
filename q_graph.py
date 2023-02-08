import numpy as np
import matplotlib.pyplot as plt



R=float(input("抵抗値を入力してください"))
L=float(int(input("インダクタンス(mL)を入力してください"))**(-3))
C=float(int(input("静電容量(uC)を入力してください"))*10**(-6))
V=float(100)

omega_0=1/(L*C)**0.5
q_value = (1/R)*(L/C)**0.5

print("共振角速度:%f"%omega_0)
print("Q値:%f"%q_value)


omega = np.linspace(0,2*omega_0,100)

Z=(R**2+(omega*L-(omega*C)**(-1))**2)**0.5

I = V/Z
plt.plot(omega,I)
plt.title('共振周波数と電流値',fontname="MS Gothic")
plt.xlabel('角速度',fontname="MS Gothic")
plt.ylabel('電流',fontname="MS Gothic")

plt.show()