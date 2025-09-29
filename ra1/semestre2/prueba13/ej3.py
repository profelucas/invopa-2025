import pulp as pl

ej3 = pl.LpProblem("ejercicio 3",pl.LpMinimize)

x1 = pl.LpVariable("x1",lowBound=0,upBound=1,cat="Binary")
x2 = pl.LpVariable("x2",lowBound=0,upBound=1,cat="Binary")
x3 = pl.LpVariable("x3",lowBound=0,upBound=1,cat="Binary")
x4 = pl.LpVariable("x4",lowBound=0,upBound=1,cat="Binary")
x5 = pl.LpVariable("x5",lowBound=0,upBound=1,cat="Binary")
x6 = pl.LpVariable("x6",lowBound=0,upBound=1,cat="Binary")
x7 = pl.LpVariable("x7",lowBound=0,upBound=1,cat="Binary")
x8 = pl.LpVariable("x8",lowBound=0,upBound=1,cat="Binary")
x9 = pl.LpVariable("x9",lowBound=0,upBound=1,cat="Binary")


ej3+=x1+x2+x3+x4+x5+x6+x7+x8+x9,"z"

ej3+=x1+x2>=1,"s1"
ej3+=x1+x7>=1,"s2"
ej3+=x2+x3>=1,"s3"
ej3+=x3+x6>=1,"s4"
ej3+=x6+x7+x8+x9>=1,"s5"
ej3+=x4>=1,"s6"
ej3+=x4+x5>=1,"s7"
ej3+=x5+x8>=1,"s8"

ej3.solve()

for variable in ej3.variables():
    print('{}->{}'.format(variable.name, variable.varValue))

print(pl.value(ej3.objective))





