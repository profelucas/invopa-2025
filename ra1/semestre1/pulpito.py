import pulp as pl

#inizializacion del modelo
prob = pl.LpProblem("whiskas",pl.LpMinimize)
#creacion de variables
x_p = pl.LpVariable('Pollo',lowBound=0,upBound=100,cat='Continuous');
x_res = pl.LpVariable('Res',lowBound=0,upBound=100,cat='Continuous');
x_co = pl.LpVariable('Cordero',lowBound=0,upBound=100,cat='Continuous');
x_ar = pl.LpVariable('Arroz',lowBound=0,upBound=100,cat='Continuous');
x_tri= pl.LpVariable('Trigo',lowBound=0,upBound=100,cat='Continuous');
x_gel = pl.LpVariable('gel',lowBound=0,upBound=100,cat='Continuous');

#funcion objetivo
prob+= 0.013 * x_p + 0.008 * x_res + 0.01 *x_co + 0.002*x_ar +0.005*x_tri+0.001*x_gel, "Z"

#restricciones
prob+=0.1*x_p+0.2*x_res+0.15*x_co+0.04*x_tri >=8,'Cantidad de proteina'
prob+=0.08*x_p+0.1*x_res+0.11*x_co+0.01*x_ar+0.01*x_tri>=6,'Cantidad de grasa'
prob+=0.001*x_p+0.005*x_res+0.003*x_co+0.1*x_ar+0.15*x_tri<=2,'Cantidad de fibra'
prob+=0.002*x_p+0.005*x_res+0.007*x_co+0.002*x_ar+0.008*x_tri<=0.2,'Cantidad de sal'
prob+=x_p+x_res+x_co+x_ar+x_tri+x_gel==100,'Cantidad de productos en lata'

#resolver
prob.solve()
print("Estado : ",pl.LpStatus[prob.status])

#mostrar las variables
for variable in prob.variables():
    print(variable.name, " = ",variable.varValue)

#mostrar el resultado
print(pl.value(prob.objective))
