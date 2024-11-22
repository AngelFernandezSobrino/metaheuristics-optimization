## Python script to solve the TOP with the PJS heuristic
## Author: Angel Fernandez Sobrino
## Optimizacion metaheuristica
##

from graph import Node, Edge, Route, Solution
import time
import pathlib
import os

""" Set algorithm parameters """
# Parametros del algoritmo, se ha utilizado directamente el codigo proporcionado
# alpha is used to compute the edge efficiency (enriched savings), its best va
# might depend on the specific instance as explained in Panadero et al. (2020)
alpha = 0.7


""" Read instance data from txt file """
# Entrada de datos del problema, se ha utilizado directamente el codigo
# proporcionado por el profesor. Lee los datos de un archivo txt y crea nodos
# con la informacion de cada fila

instance_name = "p5.3.q"  # name of the instance

# Create the solution object to store data
solution = Solution(instance_name, alpha)

# De esta manera da igual desde donde se llame el script, siempre se leera el
# archivo desde la carpeta data en el mismo directorio que el script
file_name = pathlib.Path(__file__).parent / "data" / f"{instance_name}.txt"

with file_name.open() as instance:
    i = -3  # we start at -3 so that the first node is node 0
    nodes: list[Node] = []
    for line in instance:
        if i == -3:
            pass  # line 0 contains the number of nodes, not needed
        elif i == -2:
            solution.fleet_size = int(line.split(";")[1])
        elif i == -1:
            solution.route_max_cost = float(line.split(";")[1])
        else:
            # array data with node data: x, y, demand (reward in TOP)
            data = [float(x) for x in line.split(";")]
            node = Node(i, data[0], data[1], data[2])
            nodes.append(node)
        i += 1


solution.start_time = time.time()

start_node = nodes[0]
end_node = nodes[-1]


# Partimos de una solucion con una ruta desde el nodo inicial al final pasando
# solo por un nodo intermedio.
# Este edge se incluye en cada nodo

for node in nodes[1:-1]:
    # El coste de cada arista se calcula directamente en la creacion del edge
    node.start_depot_edge = Edge(start_node, node, alpha)
    node.end_depot_edge = Edge(node, end_node, alpha)


efficiency_list: list[Edge] = []

# Iteramos por cada nodo, creando las aristas entre cada par de nodos,
# el segundo nodo lo llamaremos other, es mas facil de leer


for index, node in enumerate(nodes[1:-2], 1):
    for other_node in nodes[index + 1 : -1]:
        direct_edge = Edge(node, other_node, solution.alpha)
        inverse_edge: Edge = direct_edge.inverse_edge()

        direct_edge.calculate_efficiency()
        inverse_edge.calculate_efficiency()

        efficiency_list.append(direct_edge)
        efficiency_list.append(inverse_edge)


# sort the list of edges from higher to lower efficiency
efficiency_list.sort(key=lambda edge: edge.efficiency, reverse=True)


""" Construct the initial solution """
# Construimos la solucion inicial, utilizando rutas que pasan por un solo nodo

for node in nodes[1:-1]:
    route = Route()  # construct the route (start, node, finish)

    # Add the node to the route
    # This function adds start and end edges of the node to the route
    route.add_node_initial_depots(node)

    node.is_linked_to_start = True
    node.is_linked_to_end = True

    # Add the route to the solution

    solution.add_route(route)

""" perform the edge-selection and routing-merging iterative process """


def check_mergin_conditions(
    edge: Edge,
):
    # Checkea las condiciones para fusionar
    # Las rutas no pueden ser la misma ruta
    # El nodo origen debe estar enlazado al final o el nodo destino al inicio
    # El coste de la ruta no puede ser mayor al maximo permitido

    if edge.origin.route == edge.destiny.route:
        # print("Same route")
        return False

    if (
        edge.origin.is_linked_to_end == False
        or edge.destiny.is_linked_to_start == False
    ):
        # print("Not tail-head")
        return False

    if solution.route_max_cost < (
        edge.origin.route.cost + edge.destiny.route.cost - edge.savings
    ):
        # print("Exceeds max cost")
        return False
    # print(
    #     "Merge route: ",
    #     edge.origin.route.get_route_str(),
    #     " with route: ",
    #     edge.destiny.route.get_route_str(),
    # )
    return True


# Mientras haya aristas en la lista de eficiencia
# Obtenemos la arista con mayor eficiencia y hacemos el merge si el posible
# La arista se elimina de la lista al procesarse, independientemente de si se
# fusiona o no


while len(efficiency_list) > 0:
    # El indice siempre sera 0, ya que algoritmo es greedy y las aristas se
    # procesan en orden de mayor a menor eficiencia de forma determinista
    # Para aplicar un comportamiento mas aleatorio, se podrian aplicar tecnicas
    # como GRASP
    index = 0
    optimum_edge = efficiency_list.pop(index)

    # Podemos obtener los nodos de la arista directamente, asi como las rutas
    # asignadas a los nodos
    # os.system("clear")
    # print(f"Checking edge: {optimum_edge.plot()}")
    # for route in solution.routes:
    #     print(route.route_str)

    if check_mergin_conditions(optimum_edge):
        # Delete the inverse edge from the efficiency list if it is there
        # Maybe we should use a set to track the inverse edges in the
        # efficiency list to make this operation faster, but maybe it is not
        # worth it the work
        if optimum_edge.inverse_edge in efficiency_list:
            efficiency_list.remove(optimum_edge.inverse_edge)

        origin_node = optimum_edge.origin
        origin_route = optimum_edge.origin.route
        end_node = optimum_edge.destiny
        end_route = optimum_edge.destiny.route

        # Remove the last edge from the origin route
        origin_route.remove_last_edge()

        # The origin node will not be linked to the start depot anymore
        origin_node.is_linked_to_end = False

        # Remove the first edge from the end route
        end_route.remove_first_edge()

        # The end node will not be linked to the start depot anymore
        end_node.is_linked_to_start = False

        # The more efficient edge is added to the origin route
        origin_route.add_edge(optimum_edge)

        # And the route of the end node is merged with the route of the origin
        # node
        origin_route.merge(end_route)

        # The cost of the solution is updated
        solution.cost -= optimum_edge.savings
        # The route of the end node is removed, as it has been merged with the
        # route of the origin node
        solution.routes.remove(end_route)


solution.routes.sort(key=lambda route: route.demand, reverse=True)

print(f"Checking edge: {optimum_edge.plot()}")
check_margin = check_mergin_conditions(optimum_edge)
for route in solution.routes:
    print(route.route_str)

# Remove routes that exceed the fleet size
# Routes with index from 0 to fleet_size are the routes that are going to be
# kept in the solution, the rest are going to be removed.
for route in solution.routes[solution.fleet_size :]:
    solution.demand -= route.demand  # Update demand
    solution.cost -= route.cost  # Update cost
    solution.routes.remove(route)

solution.end_time = time.time()


## Print the solution

solution.pprint()

import networkx as nx

# Plot the solution
G = nx.Graph()
G.add_node(start_node.id, coord=(start_node.x, start_node.y))
for route in solution.routes:
    for edge in route.edges:
        G.add_edge(edge.origin.id, edge.destiny.id)
        G.add_node(edge.destiny.id, coord=(edge.destiny.x, edge.destiny.y))

coord = nx.get_node_attributes(G, "coord")
nx.draw_networkx(G, coord, node_color="pink")

import matplotlib.pyplot as plt

plt.show()
