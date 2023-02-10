from sympy import Symbol, symbols, solve, simplify
from sympy.plotting import plot

V_r = Symbol('V_r')
P, Q, x,r,V_s = symbols('P Q x r V_s')
#y = 0となる方程式つまり電力方程式をV＿ｒを軸にして解く
y=(P*r+Q*x+V_r**2)**2+(Q*r-P*x)**2-(V_r*V_s)**2
solved = solve(y,V_r)
solved
#受電端電圧の解全ての表示
print(solved)

V_r_1=solved[1].subs([(Q,0),(r,0),(x,1),(V_s,2),])
V_r_2=solved[3].subs([(Q,0),(r,0),(x,1),(V_s,2),])
#グラフ化、2つのグラフを重ねる
p = plot(V_r_1, V_r_2,(P, 0, 2), legend = True, show = False)

p[0].line_color = 'b'#配色
p[1].line_color = 'r'

p.show()
