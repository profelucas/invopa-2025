import pulp as pl

#modelo
transporte = pl.LpProblem("transporte",pl.LpMinimize)

#variables

xf1t1=pl.LpVariable("xf1t1",lowBound=0,cat="Integer")
xf1t2=pl.LpVariable("xf1t2",lowBound=0,cat="Integer")
xf2t1=pl.LpVariable("xf2t1",lowBound=0,cat="Integer")
xf2t2=pl.LpVariable("xf2t2",lowBound=0,cat="Integer")
xt1c1=pl.LpVariable("xt1c1",lowBound=0,cat="Integer")
xt1c2=pl.LpVariable("xt1c2",lowBound=0,cat="Integer")
xt2c1=pl.LpVariable("xt2c1",lowBound=0,cat="Integer")
xt2c2=pl.LpVariable("xt2c2",lowBound=0,cat="Integer")
xc2c1=pl.LpVariable("xc2c1",lowBound=0,cat="Integer")
xc1c2=pl.LpVariable("xc1c2",lowBound=0,cat="Integer")
xt2t1=pl.LpVariable("xt2t1",lowBound=0,cat="Integer")

#funcion objetivo
transporte+=260*xf1t1+250*xf1t2+280*xf2t1+290*xf2t2+255*xt1c1+249*xt1c2+267*xt2c1+270*xt2c2+185*xc1c2+170*xc2c1+160*xt2t1,"ct"

#restricciones

transporte+=xf1t1+xf1t2-1450==0,"f1"
transporte+=xf2t1+xf2t2-1180==0,"f2"
transporte+=xt1c1+xt1c2-xf1t1-xf2t1-xt2t1==0,"t1"
transporte+=xt2t1+xt2c1+xt2c2-xf1t2-xf2t2==0,"t2"
transporte+=1250+xc1c2-xc2c1-xt1c1-xt2c1==0,"c1"
transporte+=1380+xc2c1-xc1c2-xt1c2-xt2c2==0,"c2"


#solver
transporte.writeLP("transporte.lp")
transporte.solve()
print("estado: ", pl.LpStatus[transporte.status])
for variable in transporte.variables():
    print ('{}={}'.format(variable.name, variable.varValue))

#resultado
print(pl.value(transporte.objective))