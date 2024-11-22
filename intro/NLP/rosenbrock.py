import pyomo.environ as pyoenv
import pyomo.opt as pyoopt
import os

# Utilizaremos NEOS server para resolver el problema con CBC
os.environ['NEOS_EMAIL'] = 'afs121196@uoc.edu'

# Parametros de la funcion
a = 1
b = 100

model = pyoenv.ConcreteModel()

model.x = pyoenv.Var(initialize=20)
model.y = pyoenv.Var(initialize=20)

model.minimize = pyoenv.Objective(expr= (a-model.x)**2 + b*(model.y - model.x**2)**2, sense=pyoenv.minimize)

solver_manager = pyoenv.SolverManagerFactory('neos')

results = solver_manager.solve(model, solver='ipopt')

model.pprint()