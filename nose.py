from sympy import Symbol, symbols, solve, simplify
V_r = Symbol('V_r')
P, Q, x,r,V_s = symbols('P Q x r V_s')
#y = a * x ** 2 + x * b + c
y=(P*r+Q*x+V_r**2)**2+(Q*r-P*x)**2-(V_r*V_s)**2
solved = solve(y,P)
solved

print(solved)

P_r=solved[1].subs([(Q,0),(r,0),(x,1),(V_s,2),])

print(P_r)


from sympy.plotting import plot
#%matplotlib inline

#f = x**2 をプロット

plot(P_r, (V_r, 0, 2), legend = True)