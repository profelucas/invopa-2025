import pulp as pl

#creacion de solver
ej4 = pl.LpProblem("distribucion",pl.LpMaximize)


x12=pl.LpVariable("x12",0,450,"Integer")
x13=pl.LpVariable("x13",0,380,"Integer")
x14=pl.LpVariable("x14",0,390,"Integer")
x21=pl.LpVariable("x21",0,450,"Integer")
x23=pl.LpVariable("x23",0,250,"Integer")
x24=pl.LpVariable("x24",0,520,"Integer")
x25=pl.LpVariable("x25",0,410,"Integer")
x36=pl.LpVariable("x36",0,420,"Integer")
x43=pl.LpVariable("x43",0,470,"Integer")
x45=pl.LpVariable("x45",0,350,"Integer")
x46=pl.LpVariable("x46",0,410,"Integer")
x4c=pl.LpVariable("x4c",0,280,"Integer")
x5c=pl.LpVariable("x5c",0,350,"Integer")
x6c=pl.LpVariable("x6c",0,410,"Integer")

f1=pl.LpVariable("f1",0,cat="Integer")
f2=pl.LpVariable("f2",0,cat="Integer")
f3=pl.LpVariable("f3",0,cat="Integer")


#funcion objetivo
f= f1+f2+f3

ej4+=f

ej4+=x12+x13+x14-x21-f1==0
ej4+=x21+x23+x24+x25-x12-f2==0
ej4+=x36-x13-x23-x43-f3==0
ej4+=x43+x45+x46+x4c-x14-x24==0
ej4+=x5c-x45-x25==0
ej4+=x6c-x36-x46==0
ej4+=f-x4c-x5c-x6c==0

ej4.solve()

print("estado: ",pl.LpStatus[ej4.status])
for variable in ej4.variables():
    print('{}=>{}'.format(variable.name,variable.varValue))

print(pl.value(ej4.objective))
