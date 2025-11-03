import pulp as pl

#creacion de solver
ej4 = pl.LpProblem("distribucion",pl.LpMinimize)


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
f3=pl.LpVariable("f3",0,cat="Integer")

#caso 1 = ct = 3635000
#f1=950
#f2=0

#caso 2 = ct = 3178500
#f1=0
#f2=950


#funcion objetivo

ej4+=1200*x12+1350*x13+1150*x14+1200*x21+1300*x23+1250*x24+1100*x25+1850*x36+1050*x43+1100*x45+1400*x46+1550*x4c+1650*x5c+1700*x6c

#restriciones


ej4+=x12+x13+x14-x21-f1==0
ej4+=x21+x23+x24+x25-x12==0
ej4+=x36-x13-x23-x43-f3==0
ej4+=x43+x45+x46+x4c-x14-x24==0
ej4+=x5c-x45-x25==0
ej4+=x6c-x36-x46==0
ej4+=1200-x4c-x5c-x6c==0
ej4+=f1+f3==1200
ej4.solve()

print("estado: ",pl.LpStatus[ej4.status])
for variable in ej4.variables():
    print('{}=>{}'.format(variable.name,variable.varValue))

print(pl.value(ej4.objective))
