import pulp as pl

#creacion de solver
ej5 = pl.LpProblem("asignacion",pl.LpMinimize)

#variables
x11= pl.LpVariable("x11",0,1,"Integer")
x12= pl.LpVariable("x12",0,1,"Integer")
x13= pl.LpVariable("x13",0,1,"Integer")
x21= pl.LpVariable("x21",0,1,"Integer")
x22= pl.LpVariable("x22",0,1,"Integer")
x23= pl.LpVariable("x23",0,1,"Integer")
x31= pl.LpVariable("x31",0,1,"Integer")
x32= pl.LpVariable("x32",0,1,"Integer")
x33= pl.LpVariable("x33",0,1,"Integer")

#funcion objetivo

ej5+=10*x11+9*x12+5*x13+9*x21+8*x22+3*x23+6*x31+4*x32+7*x33

#restricciones

ej5+=x11+x12+x13-1==0,"r1"
ej5+=x21+x22+x23-1==0,"r2"
ej5+=x31+x32+x33-1==0,"r3"
ej5+=1-x11-x21-x31==0,"r4"
ej5+=1-x12-x22-x32==0,"r5"
ej5+=1-x13-x23-x33==0,"r6"


ej5.solve()


print("estado: ",pl.LpStatus[ej5.status])
for variable in ej5.variables():
    print('{}=>{}'.format(variable.name,variable.varValue))

print(pl.value(ej5.objective))



