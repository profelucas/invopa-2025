import pulp as pl


def resolucion_1(a)->bool:
    p1 = pl.LpProblem("ejercicio 1",pl.LpMaximize)

    x1 = pl.LpVariable('x1', lowBound=0, cat='Integer')
    x2 = pl.LpVariable('x2', lowBound=0, cat='Integer')

    #función objetivo
    p1 += 3 * x1 + 2 * x2, "Función Objetivo"

    #SA
    p1 += x1 + 2 * x2 <= a, "r1"
    p1 += -x1 + x2 <= 4, "r2"
    p1 += x1 - x2 <= 5, "r3"


    p1.solve()

    print("estado: ", pl.LpStatus[p1.status])

    if (x1.varValue == 5 and x2.varValue==1):
        return True
    else:
        return False


def resolucion_2(a, b)->None:
    p1 = pl.LpProblem("ejercicio 1",pl.LpMaximize)

    x1 = pl.LpVariable('x1', lowBound=0, cat='Integer')
    x2 = pl.LpVariable('x2', lowBound=0, cat='Integer')

    #función objetivo
    p1 += a * x1 + b * x2, "Función Objetivo"

    #SA
    p1 += x1 + 2 * x2 <= 7, "r1"
    p1 += -x1 + x2 <= 4, "r2"
    p1 += x1 - x2 <= 5, "r3"


    p1.solve()

    print("estado: ", pl.LpStatus[p1.status])
    for variable in p1.variables():
        print ('{}={}'.format(variable.name, variable.varValue))

    #resultado
    print(pl.value(p1.objective))

#solucion 1
print(resolucion_1(6.5)) #output false

print(resolucion_1(8)) #output false


#solucion 2

print(resolucion_2(2,4))

print(resolucion_2(3,3))