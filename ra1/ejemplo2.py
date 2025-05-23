import pulp as pl

#creacion de modelo
ejemplo2=pl.LpProblem("tutorial",pl.LpMaximize)

#variables
x1= pl.LpVariable('x1', lowBound=0, upBound=1, cat='Continuous')
x2= pl.LpVariable('x2', lowBound=0, upBound=1, cat='Continuous')
x3=pl.LpVariable('x3', lowBound=0, upBound=1, cat='Continuous')

#funcion objetivo

ejemplo2+=4*x1+3*x2+2*x3,"z"

#restricciones

ejemplo2+=6*x1+4*x2+3*x3<=8.5,"r1"
ejemplo2+=2*x1+x2+2*x3<=3,"r2"
ejemplo2+=4*x1+2*x2+3*x3<=7,"r3"


#x1->0,75
#x2->1
#x3->0
#z->6

#cob
#rama 1 x1<=0
#ejemplo2+=x1<=0,"cb1" #x1->0, x2->1, x3->1, z->5  cota
##fin

#rama 2 x1>=1
ejemplo2+=x1>=1,"co2"#x1->1, x2->0,625, x3->0 z->5,875

#rama 2.1 x1>=1 y x2<=0

ejemplo2+=x2<=0,"co2.1"#x1->1, x2->0, x3->0,5 z->5

#rama 2.2 x1>=1 y x2<=0

ejemplo2+=x2>=1,"co2.2"#inf


#solver
ejemplo2.writeLP("ejemplo2.lp")
ejemplo2.solve()
print("estado: ", pl.LpStatus[ejemplo2.status])
for variable in ejemplo2.variables():
    print ('{}={}'.format(variable.name, variable.varValue))

#resultado
print(pl.value(ejemplo2.objective))

