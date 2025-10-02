import pulp as pl

trns = pl.LpProblem("ej2",pl.LpMinimize)

#variables

xp1a=pl.LpVariable('xp1a', lowBound=0, cat='Integer')
xp1b=pl.LpVariable('xp1b', lowBound=0, cat='Integer')
xp1c=pl.LpVariable('xp1c', lowBound=0, cat='Integer')
xp2a=pl.LpVariable('xp2a', lowBound=0, cat='Integer')
xp2b=pl.LpVariable('xp2b', lowBound=0, cat='Integer')
xp2c=pl.LpVariable('xp2c', lowBound=0, cat='Integer')
xac=pl.LpVariable('xac', lowBound=0, cat='Integer')
xad=pl.LpVariable('xad', lowBound=0, cat='Integer')
xba=pl.LpVariable('xba', lowBound=0, cat='Integer')
xbc=pl.LpVariable('xbc', lowBound=0, cat='Integer')
xbd=pl.LpVariable('xbd', lowBound=0, cat='Integer')
xbe=pl.LpVariable('xbe', lowBound=0, cat='Integer')
xcd=pl.LpVariable('xcd', lowBound=0, cat='Integer')
xce=pl.LpVariable('xce', lowBound=0, cat='Integer')
xcC2=pl.LpVariable('xcC2', lowBound=0, cat='Integer')
xde=pl.LpVariable('xde', lowBound=0, cat='Integer')
xdC1=pl.LpVariable('xdC1', lowBound=0, cat='Integer')
xdC2=pl.LpVariable('xdC2', lowBound=0, cat='Integer')
xed=pl.LpVariable('xed', lowBound=0, cat='Integer')
xeC1=pl.LpVariable('xeC1', lowBound=0, cat='Integer')
xeC2=pl.LpVariable('xeC2', lowBound=0, cat='Integer')
xC1C2=pl.LpVariable('xC1C2', lowBound=0, cat='Integer')
xC2C1=pl.LpVariable('xC2C1', lowBound=0, cat='Integer')

#funcion objectivo

trns+= 260*xp1a+250*xp1b+280*xp1c+280*xp2a+290*xp2b+260*xp2c+200*xac+180*xad+160*xba+150*xbc+140*xbd+150*xbe+130*xcd+120*xce+160*xcC2+140*xde+150*xdC1+180*xdC2+140*xed+180*xeC1+170*xeC2+210*xC1C2+190*xC2C1,"z"

#restricciones

trns+=xp1a+xp1b+xp1c-3500==0,"pr1"
trns+=xp2a+xp2b+xp2c-3250==0,"pr2"
trns+=xac+xad-xp1a-xp2a-xba==0,"a"
trns+=xba+xbc+xbd+xbe-xp1b-xp2b==0,"b"
trns+=xcd+xce+xcC2-xp1c-xp2c-xac-xbc==0,"c"
trns+=xde+xdC1+xdC2-xad-xbd-xcd-xed==0,"d"
trns+=xed+xeC1+xeC2-xbe-xce-xde==0,"e"
trns+=xC1C2+3150-xdC1-xeC1-xC2C1==0,"c1"
trns+=xC2C1+3600-xcC2-xdC2-xeC2-xC1C2==0,"c2"

#solver
trns.writeLP("ej2.lp")
trns.solve()
print("estado: ", pl.LpStatus[trns.status])
for variable in trns.variables():
    print ('{}={}'.format(variable.name, variable.varValue))

#resultado
print(pl.value(trns.objective))