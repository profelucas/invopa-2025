import pulp as pl
#creacion de objeto
ejemplo = pl.LpProblem("ejemplo",pl.LpMaximize)

#variables
x1 = pl.LpVariable('x1', lowBound=0, cat='Continuous')
x2 = pl.LpVariable('x2', lowBound=0, cat='Interger')

#funcion objetivo
ejemplo+= 4 * x1 +  x2, "Z"

#restricciones
ejemplo += x2 <= 3 + x1,"r1"
ejemplo += 6*x2 >= 6 +x1,"r2"
ejemplo += 3*x2 <= 25 - 5*x1 ,"r3"
ejemplo += x2>= 4 -2*x1,"r4"


#solver
ejemplo.writeLP("ejemplo.lp")
ejemplo.solve()
print("estado: ", pl.LpStatus[ejemplo.status])
for variable in ejemplo.variables():
    print ('{}={}'.format(variable.name, variable.varValue))

#resultado
print(pl.value(ejemplo.objective))
