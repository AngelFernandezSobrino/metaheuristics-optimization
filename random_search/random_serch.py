import random
from typing import Callable
import time

from matplotlib.pylab import f


def basin_function_2(x: tuple[float]) -> float:
    n = 2
    return sum(xi**2 for xi in x)


def basin_function_1(x: tuple[float]) -> float:
    a, h, k = 0.5, 2, -5
    return sum(a * (xi - h) ** 2 + k for xi in x)


def random_solution(min: float, max: float, size: int) -> tuple[float]:
    return tuple(min + (max - min) * random.random() for _ in range(size))


def random_search_min(
    min: int,
    max: int,
    size: int,
    minimize_function: Callable,
    max_iterations: int,
):
    best_value = float("inf")

    for _ in range(max_iterations):
        new_solution = random_solution(min, max, size)
        new_value = minimize_function(new_solution)
        if new_value < best_value:
            best_value = new_value
            best_solution = new_solution

    return [best_value, best_solution]


if __name__ == "__main__":

    min = -5
    max = 5
    size = 2
    max_iterations = 100000
    function_to_optimize = basin_function_1
    start = time.time()
    best_value, best_solution = random_search_min(
        min, max, size, function_to_optimize, max_iterations
    )
    end = time.time()
    print("Algorithm: Random Search")
    print(f"Function: {function_to_optimize.__name__}")
    print(f"Time: {end - start}")
    print(f"Searched space: [{min}, {max}]")
    print(f"Solution size: {size}")
    print(f"Best value found: {best_value}")
    print(f"Best solution found: {str(best_solution)}")
