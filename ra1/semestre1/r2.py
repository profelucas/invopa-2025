import pulp as pl

p2 = pl.LpProblem("ejercicio 2",pl.LpMaximize)

x1 = pl.LpVariable('x1', lowBound=0, cat='Integer')
x2 = pl.LpVariable('x2', lowBound=10, cat='Integer')
x3 = pl.LpVariable('x3', lowBound=0, cat='Integer')

p2+=70000*x1+50000*x2+30000*x3,"z"

#restricciones

p2+=4*x1+3*x2+2*x3<=75,"cantidad de carton"
p2+=5*x1+4*x2+2*x3<=150,"cantidad de horas"


p2.solve()
print("estado: ", pl.LpStatus[p2.status])
for variable in p2.variables():
    print ('{}={}'.format(variable.name, variable.varValue))

#resultado
print(pl.value(p2.objective))