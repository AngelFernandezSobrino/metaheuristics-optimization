# Nos permite usar typar un elemento de la clase en la misma clase
from __future__ import annotations

import math


class Node:

    def __init__(self, id, x, y, demand) -> None:
        self.id = id
        self.x = x
        self.y = y
        self.demand = demand

        self.route: Route = None
        self.is_interior = False
        self.start_depot_edge: Edge = None
        self.end_depot_edge: Edge = None
        self.is_linked_to_start = False
        self.is_linked_to_end = False


class Edge:
    def __init__(self, origin: Node, destiny: Node, alpha: int) -> None:
        self.origin: Node = origin
        self.destiny: Node = destiny

        # Simplificamos el codigo, calculando el coste en el constructor
        self.cost = math.sqrt(
            (origin.x - destiny.x) ** 2 + (origin.y - destiny.y) ** 2
        )

        self.alpha = alpha

    def inverse_edge(self) -> Edge:
        inverse_edge = Edge(self.destiny, self.origin, self.alpha)
        inverse_edge.inverse_edge = self

        return inverse_edge

    def calculate_efficiency(self) -> None:
        # compute efficiency as proposed by Panadero et al.(2020)
        self.savings = (
            self.origin.end_depot_edge.cost
            + self.destiny.start_depot_edge.cost
            - self.cost
        )
        self.edge_reward = self.origin.demand + self.destiny.demand

        self.efficiency = (
            self.alpha * self.savings + (1 - self.alpha) * self.edge_reward
        )

    def plot(self) -> None:
        return f"Edge: {self.origin.id} -> {self.destiny.id} || Cost = {self.cost:.2f}"


class Route:
    def __init__(self) -> None:
        self.cost: float = 0
        self.edges: list[Edge] = []
        self.demand: float = 0
        self.route_str = ""

    def remove_last_edge(self) -> None:
        edge = self.edges.pop(-1)
        self.cost -= edge.cost

        self.update_route_str()

    def remove_first_edge(self) -> None:
        edge = self.edges.pop(0)
        self.cost -= edge.cost

        self.update_route_str()

    def add_edge(self, edge: Edge) -> None:
        self.edges.append(edge)
        self.demand += edge.destiny.demand
        self.cost += edge.cost

        # La ruta se asigna a los nodos origen y destino de la arista
        # El nodo de origen ya tiene asignada la ruta al añadir el edge a la ruta por lo que solo se seria necesario asignar el destino
        # De todas formas, se asigna la ruta a ambos nodos para evitar errores en caso de que este metodo tenga otro caso de uso en el futuro
        # Pero para mejorar la eficiencia, se podria eliminar la asignacion al origen
        edge.origin.route = self
        edge.destiny.route = self

        self.update_route_str()

    def merge(self, other_route: Route) -> None:
        for edge in other_route.edges:
            self.add_edge(edge)

        self.update_route_str()

    def add_node_initial_depots(self, node: Node) -> None:
        self.edges.append(node.start_depot_edge)
        self.demand += node.demand
        self.cost += node.start_depot_edge.cost
        self.edges.append(node.end_depot_edge)
        self.cost += node.end_depot_edge.cost
        node.route = self

        self.update_route_str()

    def get_route_str(self) -> str:
        route_str = ""
        for edge in self.edges:
            route_str += f"{edge.origin.id} -> "
        route_str += f"{self.edges[-1].destiny.id}"
        return route_str

    def update_route_str(self) -> None:
        self.route_str = self.get_route_str()

    def pprint(self) -> str:
        print(
            f"Route: {self.get_route_str()} || Reward = {self.demand:.2f} || Cost / Time = {self.cost:.2f}"
        )


class Solution:
    last_id = -1

    def __init__(self, instance_name: str, alpha: float) -> None:
        Solution.last_id += 1
        self.id = Solution.last_id
        self.instance_name = instance_name
        self.alpha = alpha
        self.fleet_size: int = 0
        self.route_max_cost: float = 0
        self.start_time: float = 0
        self.end_time: float = 0
        self.routes: list[Route] = []
        self.cost: float = 0
        self.demand: float = 0

    # This function adds the route to the solution, updating
    # the solution cost and demand
    def add_route(self, route: Route) -> None:
        self.routes.append(route)
        self.cost += route.cost
        self.demand += route.demand

    def pprint(self):
        print(f"Solution: {self.id}")
        print(f"Instance: {self.instance_name}")
        print(f"Reward obtained = {self.demand:.2f}")
        print(
            f"Computational time: {self.end_time - self.start_time:.2f} sec."
        )
        print("Alpha used {self.alpha:.2f}")
        for route in self.routes:
            route.pprint()
