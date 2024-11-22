import pyomo.environ as pyoenv
import pyomo.opt as pyoopt
import os

# Utilizaremos NEOS server para resolver el problema con CBC
os.environ['NEOS_EMAIL'] = 'afs121196@uoc.edu'

# En este caso he decidido trabajar con modelos concretos
# Por tanto, debemos generar los datos para cargar a los parametros

# A es una array para generar el set de objetos
A = ['m1', 'm2', 'm3', 'm4']
# b es un dict con el value de cada objeto
b = {'m1':8, 'm2':3, 'm3':6, 'm4':11}
# w es el dict con el peso de cada objeto
w = {'m1':5, 'm2':7, 'm3':4, 'm4':3}
# Limite superior de x, cantidad maxima de objetos de cada tipo que se pueden anadir
q = 2

# Peso maximo admisible en la bolsa
W_max = 14

# Implementado utilizado ConcreteModels
model = pyoenv.ConcreteModel()

model.A = pyoenv.Set(initialize=A)

# Variable solucion
# Debe ser un numero enterior
# Acotado a 2, que es la q
model.x = pyoenv.Var( model.A, within=pyoenv.Integers, bounds=(0,q))

# Función objetivo
def objective_value(m):
    return sum( b[i]*m.x[i] for i in model.A )
model.objective = pyoenv.Objective(rule=objective_value, sense = pyoenv.maximize )

# Constraint de peso maximo admisible
def constraint_weight(m):
    return sum( w[i]*m.x[i] for i in model.A ) <= W_max
model.constraint_weight = pyoenv.Constraint(rule=constraint_weight)

# Utilizaremos de nuevo glpk

solver_manager = pyoenv.SolverManagerFactory('neos')

results = solver_manager.solve(model, solver='cbc')

model.pprint()

# Para poder detectar si el solver no ha logrado una solución se checkean su estado al terminar
print(results)
if (results.solver.status == pyoopt.SolverStatus.ok) and (results.solver.termination_condition == pyoopt.TerminationCondition.optimal):
    # Do something when the solution in optimal and feasible
    pass
elif (results.solver.termination_condition == pyoopt.TerminationCondition.infeasible):
    # Do something when model in infeasible
    pass
else:
    # Something else is wrong
    pass
    print("Solver Status:",  results.solver.status)
    print("Solver termination condition: ", results.solver.termination_condition)

total_weight = sum( w[i]*pyoenv.value(model.x[i]) for i in model.A )
print('Total Weight:', total_weight)
print('Total Benefit:', pyoenv.value(model.objective))

print('%12s %12s' % ('Item', '# Selected'))
print('=========================')
for i in A:
    print('%12s %12s' % (i, pyoenv.value(model.x[i])))
print('-------------------------')