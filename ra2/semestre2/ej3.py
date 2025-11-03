import pulp as pl

#creacion de solver
cmc = pl.LpProblem("camino mas corto",pl.LpMinimize)

#variables

x12=pl.LpVariable("x12",0,1,pl.LpBinary)
x13=pl.LpVariable("x13",0,1,pl.LpBinary)
x14=pl.LpVariable("x14",0,1,pl.LpBinary)
x15=pl.LpVariable("x15",0,1,pl.LpBinary)
x23=pl.LpVariable("x23",0,1,pl.LpBinary)
x25=pl.LpVariable("x25",0,1,pl.LpBinary)
x35=pl.LpVariable("x35",0,1,pl.LpBinary)
x45=pl.LpVariable("x45",0,1,pl.LpBinary)
x46=pl.LpVariable("x46",0,1,pl.LpBinary)
x56=pl.LpVariable("x56",0,1,pl.LpBinary)

#funcion objetivo

cmc+= 350*x12+800*x13+600*x14+1200*x15+300*x23+600*x25+300*x35+300*x45+500*x46+200*x56

#restricciones

cmc+=x12+x13+x14+x15-1==0
cmc+=x23+x25-x12==0
cmc+=x35-x13-x23==0
cmc+=x45+x46-x14==0
cmc+=x56-x35-x45-x15==0
cmc+=1-x56-x46==0

cmc.solve()

print("estado: ",pl.LpStatus[cmc.status])
for variable in cmc.variables():
    print('{}=>{}'.format(variable.name,variable.varValue))

print(pl.value(cmc.objective))