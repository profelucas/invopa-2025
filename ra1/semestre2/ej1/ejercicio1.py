import pulp as pl
#modelo
ej1 = pl.LpProblem("ejemplo1",pl.LpMaximize)

#variables
x1=pl.LpVariable("x1",lowBound=0,cat='continuous')
x2=pl.LpVariable("x2",lowBound=0,cat='continuous')

#funcion objetivo
ej1+=6*x1+4*x2,"z"

#restricciones

ej1+=-1*x1+3*x2<=9,"r1"
ej1+=9*x1+10*x2<=80,"r2"
ej1+=14*x1+6*x2<=91,"r3"

#candb
#izquierdo
#ej1+=x2<=3,"ri1"
#ej1+=x1<=5,'ri1.1'
#ej1+=x1>=6,'ri1.2'
#ej1+=x2<=1,'ri12'
#ej1+=x2>=2,'ri122'
#ej1+=x1<=6,'ri12.1'
#ej1+=x1>=7,'ri12.2'

#derecha
ej1+=x2>=4,'rd1'
#ej1+=x1<=4,'rd1.1'
#ej1+=x2<=4,'rd1.1.1'
#ej1+=x2>=5,'rd1.1.2'
ej1+=x1>=5,'rd1.2'
ej1.solve()

print("Estado: ",pl.LpStatus[ej1.status])
print(pl.value(ej1.objective))
for variable in ej1.variables():
    print('{}={}'.format(variable.name,variable.varValue))
