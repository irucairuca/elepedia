import sympy
import numpy as np
import matplotlib.pyplot as plt

# シンボル（変数記号）の定義
q,i = sympy.symbols('q i', cls=sympy.Function)
t,E,R,C,C1 = sympy.symbols('t E R C C1')

# 方程式 eq1 を立てる
eq1 = sympy.Eq( E, R * sympy.Derivative(q(t), t) + q(t)/C )
display(eq1)
sympy.latex(eq1) 