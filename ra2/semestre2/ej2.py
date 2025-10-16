#importacion
import pulp as pl

#construccion del modelo

ej2 = pl.LpProblem("ejemplo de transbordo",pl.LpMinimize)


#caminos/variables

xf1a1 =pl.LpVariable("Xf1a1",0, cat= 'Integer')
xf1a2= pl.LpVariable("Xf1a2",0, cat= 'Integer')
xf1a3= pl.LpVariable("Xf1a3",0, cat= 'Integer')
xf2a1= pl.LpVariable("Xf2a1",0, cat= 'Integer')
xf2a2= pl.LpVariable("Xf2a2",0, cat= 'Integer')
xf2a3= pl.LpVariable("Xf2a3",0, cat= 'Integer')
xa1c1= pl.LpVariable("Xa1c1",0, cat= 'Integer')
xa1c2= pl.LpVariable("Xa1c2",0, cat= 'Integer')
xa1c3= pl.LpVariable("Xa1c3",0, cat= 'Integer')
xa2c1= pl.LpVariable("Xa2c1",0, cat= 'Integer')
xa2c2= pl.LpVariable("Xa2c2",0, cat= 'Integer')
xa2c3= pl.LpVariable("Xa2c3",0, cat= 'Integer')
xa3c1= pl.LpVariable("Xa3c1",0, cat= 'Integer')
xa3c2= pl.LpVariable("Xa3c2",0, cat= 'Integer')
xa3c3= pl.LpVariable("Xa3c3",0, cat= 'Integer')



#funcion objetivo

ej2 += 15*xf1a1+10*xf1a2+13*xf1a3+15*xf2a1+16*xf2a2+10*xf2a3+8*xa1c1+14*xa1c2+10*xa1c3+12*xa2c1+10*xa2c2+16*xa2c3+10*xa3c1+12*xa3c2+15*xa3c3,"ct"

#restricciones

ej2+= xf1a1+xf1a2+xf1a3 <= 380, "f1"
ej2+=xf2a1+xf2a2+xf2a3<= 350, "f2"
ej2+=xa1c1+xa1c2+xa1c3-xf1a1-xf2a1==0, "a1"
ej2+=xa2c1+xa2c2+xa2c3-xf1a2-xf2a2==0,"a2"
ej2+=xa3c1+xa3c2+xa3c3-xf1a3-xf2a3==0,"a3"
ej2+=150-xa1c1-xa2c1-xa3c1==0,"c1"
ej2+=270-xa1c2-xa2c2-xa3c2==0,"c2"
ej2+=210-xa1c3-xa2c3-xa3c3 ==0 ,"c3"

ej2.solve()

print("Estado: ", pl.LpStatus[ej2.status])

for variable in ej2.variables():
    print('{}->{}'.format(variable.name,variable.varValue))

print("Z->{}".format(pl.value(ej2.objective)))

