import matplotlib.pyplot as plt
import math 
import numpy as np

#変数項
R=np.linspace(0, 1000, 10**6)
#定数項
E=2.0

L=10**-3
omega=2*math.pi*50

I_dot=E/(R+1j*omega*L)
V_dot=R*E/(R+1j*omega*L)

S_dot=V_dot*I_dot.conjugate()
P=S_dot.real
plt.xlabel("P")
plt.ylabel("V")
plt.plot(P,V_dot)
plt.show()