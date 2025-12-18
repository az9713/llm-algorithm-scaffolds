"""
Reference implementations for optimization algorithms.

Implements: Gradient Descent, Simulated Annealing, Genetic Algorithm, Hill Climbing.
"""

import math
import random
from dataclasses import dataclass
from typing import Any, Callable

import numpy as np
from scipy import optimize


@dataclass
class OptimizationResult:
    """Result from an optimization algorithm."""

    value: float
    """Optimal function value found."""

    solution: Any
    """Optimal solution (x value, etc.)."""

    iterations: int = 0
    """Number of iterations performed."""

    converged: bool = True
    """Whether the algorithm converged."""

    history: list | None = None
    """History of function values (for debugging)."""

    def to_dict(self) -> dict[str, Any]:
        """Convert to dictionary for comparison."""
        return {
            "value": self.value,
            "solution": self.solution if not isinstance(self.solution, np.ndarray)
                        else self.solution.tolist(),
            "converged": self.converged,
        }


def gradient_descent(
    f: Callable,
    grad: Callable | None = None,
    x0: np.ndarray | list | float = 0.0,
    learning_rate: float = 0.01,
    tol: float = 1e-6,
    max_iter: int = 10000,
) -> OptimizationResult:
    """
    Gradient Descent for continuous optimization.

    Args:
        f: Objective function to minimize.
        grad: Gradient of f. If None, uses numerical gradient.
        x0: Initial point.
        learning_rate: Step size.
        tol: Convergence tolerance.
        max_iter: Maximum iterations.

    Returns:
        OptimizationResult with optimal solution.
    """
    x = np.atleast_1d(np.array(x0, dtype=float))

    if grad is None:
        # Use numerical gradient
        def grad(x):
            eps = 1e-8
            g = np.zeros_like(x)
            for i in range(len(x)):
                x_plus = x.copy()
                x_minus = x.copy()
                x_plus[i] += eps
                x_minus[i] -= eps
                g[i] = (f(x_plus) - f(x_minus)) / (2 * eps)
            return g

    history = [f(x)]

    for i in range(max_iter):
        g = grad(x)
        x_new = x - learning_rate * g

        history.append(f(x_new))

        if np.linalg.norm(x_new - x) < tol:
            return OptimizationResult(
                value=f(x_new),
                solution=x_new.tolist() if len(x_new) > 1 else float(x_new[0]),
                iterations=i + 1,
                converged=True,
                history=history,
            )

        x = x_new

    return OptimizationResult(
        value=f(x),
        solution=x.tolist() if len(x) > 1 else float(x[0]),
        iterations=max_iter,
        converged=False,
        history=history,
    )


def hill_climbing(
    f: Callable,
    x0: np.ndarray | list | float = 0.0,
    step_size: float = 0.1,
    max_iter: int = 1000,
    minimize: bool = True,
) -> OptimizationResult:
    """
    Hill Climbing local search optimization.

    Args:
        f: Objective function.
        x0: Initial point.
        step_size: Size of random steps.
        max_iter: Maximum iterations.
        minimize: If True, minimize; otherwise maximize.

    Returns:
        OptimizationResult with best solution found.
    """
    x = np.atleast_1d(np.array(x0, dtype=float))
    best_value = f(x)
    history = [best_value]

    sign = 1 if minimize else -1

    for i in range(max_iter):
        # Generate random neighbor
        neighbor = x + np.random.randn(len(x)) * step_size
        neighbor_value = f(neighbor)

        # Accept if better
        if sign * neighbor_value < sign * best_value:
            x = neighbor
            best_value = neighbor_value

        history.append(best_value)

    return OptimizationResult(
        value=best_value,
        solution=x.tolist() if len(x) > 1 else float(x[0]),
        iterations=max_iter,
        converged=True,
        history=history,
    )


def simulated_annealing(
    f: Callable,
    x0: np.ndarray | list | float = 0.0,
    temp_init: float = 100.0,
    temp_final: float = 0.001,
    cooling_rate: float = 0.99,
    max_iter: int = 10000,
    minimize: bool = True,
    seed: int | None = None,
) -> OptimizationResult:
    """
    Simulated Annealing for global optimization.

    Args:
        f: Objective function.
        x0: Initial point.
        temp_init: Initial temperature.
        temp_final: Final temperature.
        cooling_rate: Temperature decay rate.
        max_iter: Maximum iterations.
        minimize: If True, minimize; otherwise maximize.
        seed: Random seed.

    Returns:
        OptimizationResult with best solution found.
    """
    if seed is not None:
        np.random.seed(seed)
        random.seed(seed)

    x = np.atleast_1d(np.array(x0, dtype=float))
    current_value = f(x)
    best_x = x.copy()
    best_value = current_value

    sign = 1 if minimize else -1
    temp = temp_init
    history = [current_value]

    i = 0
    while temp > temp_final and i < max_iter:
        # Generate neighbor
        neighbor = x + np.random.randn(len(x)) * temp * 0.1
        neighbor_value = f(neighbor)

        # Calculate acceptance probability
        delta = sign * (neighbor_value - current_value)

        if delta < 0 or random.random() < math.exp(-delta / temp):
            x = neighbor
            current_value = neighbor_value

            if sign * current_value < sign * best_value:
                best_x = x.copy()
                best_value = current_value

        temp *= cooling_rate
        history.append(best_value)
        i += 1

    return OptimizationResult(
        value=best_value,
        solution=best_x.tolist() if len(best_x) > 1 else float(best_x[0]),
        iterations=i,
        converged=True,
        history=history,
    )


def genetic_algorithm(
    f: Callable,
    bounds: list[tuple[float, float]],
    population_size: int = 50,
    generations: int = 100,
    mutation_rate: float = 0.1,
    crossover_rate: float = 0.7,
    minimize: bool = True,
    seed: int | None = None,
) -> OptimizationResult:
    """
    Genetic Algorithm for optimization.

    Args:
        f: Objective function.
        bounds: List of (min, max) tuples for each dimension.
        population_size: Size of population.
        generations: Number of generations.
        mutation_rate: Probability of mutation.
        crossover_rate: Probability of crossover.
        minimize: If True, minimize; otherwise maximize.
        seed: Random seed.

    Returns:
        OptimizationResult with best solution found.
    """
    if seed is not None:
        np.random.seed(seed)
        random.seed(seed)

    n_dims = len(bounds)
    sign = 1 if minimize else -1

    # Initialize population
    population = []
    for _ in range(population_size):
        individual = [random.uniform(b[0], b[1]) for b in bounds]
        population.append(np.array(individual))

    def fitness(x):
        return sign * f(x)

    best_x = population[0].copy()
    best_value = f(best_x)
    history = [best_value]

    for gen in range(generations):
        # Evaluate fitness
        fitness_values = [fitness(ind) for ind in population]

        # Update best
        for i, ind in enumerate(population):
            val = f(ind)
            if sign * val < sign * best_value:
                best_x = ind.copy()
                best_value = val

        history.append(best_value)

        # Selection (tournament)
        def tournament_select():
            i, j = random.sample(range(population_size), 2)
            return population[i] if fitness_values[i] < fitness_values[j] else population[j]

        # Create new population
        new_population = []
        while len(new_population) < population_size:
            parent1 = tournament_select()
            parent2 = tournament_select()

            # Crossover
            if random.random() < crossover_rate:
                alpha = random.random()
                child1 = alpha * parent1 + (1 - alpha) * parent2
                child2 = (1 - alpha) * parent1 + alpha * parent2
            else:
                child1, child2 = parent1.copy(), parent2.copy()

            # Mutation
            for child in [child1, child2]:
                for i in range(n_dims):
                    if random.random() < mutation_rate:
                        child[i] = random.uniform(bounds[i][0], bounds[i][1])

            new_population.extend([child1, child2])

        population = new_population[:population_size]

    return OptimizationResult(
        value=best_value,
        solution=best_x.tolist() if len(best_x) > 1 else float(best_x[0]),
        iterations=generations,
        converged=True,
        history=history,
    )


# Helper to parse function strings
def parse_optimization_function(func_str: str) -> Callable:
    """Parse simple optimization function strings."""
    import math

    def f(x):
        if isinstance(x, (list, np.ndarray)):
            if len(x) == 1:
                x = x[0]
            else:
                # Multi-dimensional
                expr = func_str
                for i, xi in enumerate(x):
                    expr = expr.replace(f"x{i}", str(xi))
                    expr = expr.replace(f"x[{i}]", str(xi))
                return eval(expr)

        expr = func_str
        expr = expr.replace("^", "**")
        expr = expr.replace("x", str(x))
        expr = expr.replace("sin", "math.sin")
        expr = expr.replace("cos", "math.cos")
        expr = expr.replace("exp", "math.exp")
        return eval(expr)

    return f


# Convenience function to run any optimization algorithm
def run_optimization_algorithm(
    algorithm: str,
    **kwargs,
) -> OptimizationResult:
    """
    Run an optimization algorithm by name.

    Args:
        algorithm: Algorithm name (gradient_descent, hill_climbing,
                   simulated_annealing, genetic_algorithm).
        **kwargs: Algorithm-specific arguments.

    Returns:
        OptimizationResult from the algorithm.
    """
    algorithms = {
        "gradient_descent": gradient_descent,
        "hill_climbing": hill_climbing,
        "simulated_annealing": simulated_annealing,
        "genetic_algorithm": genetic_algorithm,
    }

    algorithm = algorithm.lower().replace("-", "_")
    if algorithm not in algorithms:
        raise ValueError(f"Unknown algorithm: {algorithm}")

    func = algorithms[algorithm]

    # Parse function if string
    f = kwargs.get("f")
    if isinstance(f, str):
        f = parse_optimization_function(f)
        kwargs["f"] = f

    grad = kwargs.get("grad")
    if isinstance(grad, str):
        grad = parse_optimization_function(grad)
        kwargs["grad"] = grad

    if algorithm == "gradient_descent":
        return func(
            kwargs["f"],
            kwargs.get("grad"),
            kwargs.get("x0", 0.0),
            kwargs.get("learning_rate", 0.01),
            kwargs.get("tol", 1e-6),
            kwargs.get("max_iter", 10000),
        )
    elif algorithm == "hill_climbing":
        return func(
            kwargs["f"],
            kwargs.get("x0", 0.0),
            kwargs.get("step_size", 0.1),
            kwargs.get("max_iter", 1000),
            kwargs.get("minimize", True),
        )
    elif algorithm == "simulated_annealing":
        return func(
            kwargs["f"],
            kwargs.get("x0", 0.0),
            kwargs.get("temp_init", 100.0),
            kwargs.get("temp_final", 0.001),
            kwargs.get("cooling_rate", 0.99),
            kwargs.get("max_iter", 10000),
            kwargs.get("minimize", True),
            kwargs.get("seed"),
        )
    elif algorithm == "genetic_algorithm":
        return func(
            kwargs["f"],
            kwargs["bounds"],
            kwargs.get("population_size", 50),
            kwargs.get("generations", 100),
            kwargs.get("mutation_rate", 0.1),
            kwargs.get("crossover_rate", 0.7),
            kwargs.get("minimize", True),
            kwargs.get("seed"),
        )
    else:
        raise ValueError(f"Unhandled algorithm: {algorithm}")
