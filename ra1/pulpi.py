import pulp as pl

ejemplo = pl.LpProblem("ejemplo",pl.LpMaximize)

x = pl.LpVariable('x', lowBound=0, cat='Continuous')
y = pl.LpVariable('y', lowBound=2, cat='Continuous')

ejemplo+= 4 * x + 3 * y, "Z"

ejemplo +=2 * y <= 25 - x,"r1"
ejemplo += 4 * y >= 2 * x - 8,"r2"
ejemplo += y <= 2 * x - 5,"r3"

ejemplo.writeLP("ejemplo.lp")
ejemplo.solve()
print("estado: ", pl.LpStatus[ejemplo.status])
for variable in ejemplo.variables():
    print ('{}={}'.format(variable.name, variable.varValue))


print(pl.value(ejemplo.objective))
