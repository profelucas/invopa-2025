import pulp as pl

ej2 = pl.LpProblem("ejemplo_error",pl.LpMaximize)

x1 = pl.LpVariable("x1",lowBound=0,cat="continuous")
x2 = pl.LpVariable("x2",lowBound=0,cat="continuous")
#funcion objetivo
ej2+=x1+2*x2,"z"
#restricciones
ej2+=-3*x1+15*x2<=60,"r1"
ej2+=11*x1+4*x2<=62,"r2"
ej2+=3*x1+7*x2>=21,"r3"

#ramificacion

#ej2+=x1<=3,"ri1"
#ej2+=x2<=4,"ri1.1"
#ej2+=x2>=5,"ri1.2"

ej2+=x1>=4,"rd1"
#ej2+=x2<=4,"rd1.1"
#ej2+=x1<=4,"rd1.1.1"
#ej2+=x1>=5,"rd1.1.2"
ej2+=x2>=5,"rd1.2"

ej2.solve()
print("estado= ", pl.LpStatus[ej2.status])
print(pl.value(ej2.objective))

for variable in ej2.variables():
    print('{} -> {}'.format(variable.name, variable.varValue))


