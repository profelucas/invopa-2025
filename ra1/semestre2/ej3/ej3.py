import pulp as pl

# creacion de modelo

ej3 = pl.LpProblem("ejercicio 3", pl.LpMaximize)

#Lista de variables
variables = ["x1","x2","x3","x4","x5"]

constantes = {
    "x1" : 100,
    "x2": 60,
    "x3": 70,
    "x4":15,
    "x5":15,
}

restricciones = {
    "x1": 50,
    "x2": 23,
    "x3": 35,
    "x4": 15,
    "x5": 7,
}
#variables 
x = pl.LpVariable.dicts("x",variables,0,1)
#funcion objetivo
ej3+=pl.lpSum([constantes[i] * x[i] for i in variables]),"z"

#restricciones

ej3+=pl.lpSum(restricciones[i]*x[i] for i in variables)<=60,"r"

#r&a

#lado izquierdo
#ej3+=x['x3']<=0,"ri1"
#ej3+=x['x1']<=0,"ri1.1"
#ej3+=x['x1']>=1,"ri1.2"
#ej3+=x['x2']<=0,"ri1.2.1"
#ej3+=x['x2']>=1,"ri1.2.2"
#ej3+=x['x4']<=0,'ri1.2.1.1'
#ej3+=x['x4']>=1,'ri1.2.1.2'

#lado derecho

ej3+=x["x3"]>=1,"rd1"
#ej3+=x['x5']<=0,"rd1.1"
ej3+=x['x5']>=1,"rd1.2"

ej3+=x['x2']<=0,"rd1.2.1"
ej3+=x['x2']>=1,"rd1.2.2"

#ej3+=x['x1']<=0,"rd1.2.1.1"
#ej3+=x['x1']>=1,"rd1.2.1.2"

#ej3+=x['x1']<=0,"rd1.1.1"
#ej3+=x['x1']>=1,"rd1.1.2"

#ej3+=x['x4']<=0,"rd1.1.1.1"
#ej3+=x['x4']>=1,"rd1.1.1.2"
#ej3+=x['x2']<=0,"rd1.1.1.2.1"
#ej3+=x['x2']>=1,"rd1.1.1.2.2"
ej3.solve()

print("estado: ",pl.LpStatus[ej3.status])

for variable in ej3.variables():
    print('{} -> {}'.format(variable.name,variable.varValue))

print('z-> {} '.format(pl.value(ej3.objective)))


