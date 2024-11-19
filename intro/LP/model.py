# Informacion de pyomo
# https://pyomo.readthedocs.io/en/stable/getting_started/pyomo_overview/simple_examples.html

# Se ha implementado con AbstractModel, siguiendo la linea del ejemplo, pero en el Google Groups y en diversas publicaciones se puede ver como el uso de concretemodels es mas recomendado.
# En este caso se ha evitaro usar el import del modulo completo al namespace del script, ya que se considera un mala practica. Se ha utilizado el alias pyo, como aconseja la documentacion.

import pyomo.environ as pyo

model = pyo.AbstractModel()

# Food
model.Foods = pyo.Set()
# Nutrients
model.Nutrients = pyo.Set()

# Cost of each food
model.FoodsCost = pyo.Param(model.Foods, within=pyo.PositiveReals)
# Nutrients of each food
model.FoodsNutrients = pyo.Param(model.Foods, model.Nutrients, within=pyo.NonNegativeReals)

# Nutrients boundary conditions
model.NutrientsMin = pyo.Param(model.Nutrients, within=pyo.NonNegativeReals, default=0.0)
model.NutrientsMax = pyo.Param(model.Nutrients, within=pyo.NonNegativeReals, default=float('inf'))

# Variable to optimze
# Amout of each food
model.FoodsAmmount = pyo.Var(model.Foods, within=pyo.NonNegativeReals)

# Cost function objetive
# Function to minimize
def cost_function(model):
    return sum(model.FoodsCost[food]*model.FoodsAmmount[food] for food in model.Foods)

# Nutrient boundary constraints
# Checks if nutrients are out of bounds
def nutrients_boundary_check(model, nutrient):
    total = sum(model.FoodsNutrients[food, nutrient]*model.FoodsAmmount[food] for food in model.Foods)
    return (model.NutrientsMin[nutrient], total, model.NutrientsMax[nutrient])


# Assigns the cost function to the model as the objetive
model.CostObjetive = pyo.Objective(rule = cost_function, sense=pyo.minimize)

# Assigns the boundary constraints calculation to the model
model.NutrientsConstraints = pyo.Constraint(model.Nutrients, rule=nutrients_boundary_check)

data = {None: {
    'Foods': ['p1', 'p2' , 'p3'],
    'Nutrients': ['Calc', 'Iron', 'Prot', 'Fat'],
    'FoodsCost': {'p1': 0.25, 'p2': 0.10, 'p3': 0.08},
    'NutrientsMin': {'Calc': 10.0, 'Iron': 12.0, 'Prot': 15.0},
    'NutrientsMax': {'Fat': 7.5},
    'FoodsNutrients': {('p1', 'Calc'): 0.7, ('p1', 'Iron'): 0.9, ('p1', 'Prot'): 0.8, ('p1', 'Fat'):0.5,
                       ('p2', 'Calc'): 0.8, ('p2', 'Iron'): 0.8, ('p2', 'Prot'): 1.5, ('p2', 'Fat'):0.6,
                       ('p3', 'Calc'): 0.0, ('p3', 'Iron'): 0.8, ('p3', 'Prot'): 0.9, ('p3', 'Fat'):0.4},
}}

instance = model.create_instance('./intro/LP/model.dat')
solver = pyo.SolverFactory('glpk')
solver.solve(instance, tee=True)

instance.pprint()