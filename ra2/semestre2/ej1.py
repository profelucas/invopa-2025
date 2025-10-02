import pulp as pl
#construccion del problema
transporte = pl.LpProblem("ejemplo de transporte",pl.LpMinimize)

#caminos/variables
xab=pl.LpVariable("xab",0,cat="Integer")
xac=pl.LpVariable("xac",0,cat="Integer")
xbc=pl.LpVariable("xbc",0,cat="Integer")

#funcion objetivo
transporte+=100*xab+50*xac+15*xbc,"ct"

#restricciones

transporte+=50-xab-xac==0,"A"
transporte+=xab+xac==50,"B"
transporte+=xac-xbc==0,"C"

transporte.solve()

print("Estado: ", pl.LpStatus[transporte.status])

for variable in transporte.variables():
    print('{}->{}'.format(variable.name,variable.varValue))

print("Z->{}".format(pl.value(transporte.objective)))



