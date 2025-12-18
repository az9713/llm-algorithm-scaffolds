"""
Reference implementations for numerical methods.

Implements: Newton-Raphson, Bisection, Monte Carlo estimation.
"""

import random
from dataclasses import dataclass
from typing import Any, Callable

from scipy import optimize


@dataclass
class NumericalResult:
    """Result from a numerical algorithm."""

    value: float
    """The computed value (root, estimate, etc.)."""

    iterations: int = 0
    """Number of iterations performed."""

    converged: bool = True
    """Whether the algorithm converged."""

    error: float | None = None
    """Estimated error or residual."""

    def to_dict(self) -> dict[str, Any]:
        """Convert to dictionary for comparison."""
        return {
            "value": self.value,
            "converged": self.converged,
            "iterations": self.iterations,
        }


def newton_raphson(
    f: Callable[[float], float],
    df: Callable[[float], float] | None = None,
    x0: float = 1.0,
    tol: float = 1e-10,
    max_iter: int = 100,
) -> NumericalResult:
    """
    Newton-Raphson method for finding roots.

    Args:
        f: Function to find root of.
        df: Derivative of f. If None, uses scipy.
        x0: Initial guess.
        tol: Tolerance for convergence.
        max_iter: Maximum iterations.

    Returns:
        NumericalResult with root approximation.
    """
    if df is None:
        # Use scipy for numerical derivative
        result = optimize.newton(f, x0, tol=tol, maxiter=max_iter, full_output=True)
        root = result[0]
        info = result[1]
        return NumericalResult(
            value=root,
            iterations=info.iterations,
            converged=info.converged,
        )

    x = x0
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)

        if abs(dfx) < 1e-15:
            return NumericalResult(
                value=x,
                iterations=i + 1,
                converged=False,
                error=abs(fx),
            )

        x_new = x - fx / dfx

        if abs(x_new - x) < tol:
            return NumericalResult(
                value=x_new,
                iterations=i + 1,
                converged=True,
                error=abs(f(x_new)),
            )

        x = x_new

    return NumericalResult(
        value=x,
        iterations=max_iter,
        converged=False,
        error=abs(f(x)),
    )


def bisection(
    f: Callable[[float], float],
    a: float,
    b: float,
    tol: float = 1e-10,
    max_iter: int = 100,
) -> NumericalResult:
    """
    Bisection method for finding roots.

    Args:
        f: Function to find root of.
        a: Left endpoint of interval.
        b: Right endpoint of interval.
        tol: Tolerance for convergence.
        max_iter: Maximum iterations.

    Returns:
        NumericalResult with root approximation.

    Raises:
        ValueError: If f(a) and f(b) have the same sign.
    """
    fa, fb = f(a), f(b)

    if fa * fb > 0:
        raise ValueError(f"f(a) and f(b) must have opposite signs: f({a})={fa}, f({b})={fb}")

    if abs(fa) < tol:
        return NumericalResult(value=a, iterations=0, converged=True)
    if abs(fb) < tol:
        return NumericalResult(value=b, iterations=0, converged=True)

    for i in range(max_iter):
        c = (a + b) / 2
        fc = f(c)

        if abs(fc) < tol or (b - a) / 2 < tol:
            return NumericalResult(
                value=c,
                iterations=i + 1,
                converged=True,
                error=abs(fc),
            )

        if fc * fa < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

    c = (a + b) / 2
    return NumericalResult(
        value=c,
        iterations=max_iter,
        converged=False,
        error=abs(f(c)),
    )


def monte_carlo_pi(
    n_samples: int = 10000,
    seed: int | None = None,
) -> NumericalResult:
    """
    Monte Carlo estimation of pi using random points in unit square.

    Args:
        n_samples: Number of random samples.
        seed: Random seed for reproducibility.

    Returns:
        NumericalResult with pi estimate.
    """
    if seed is not None:
        random.seed(seed)

    inside_circle = 0
    for _ in range(n_samples):
        x = random.random()
        y = random.random()
        if x * x + y * y <= 1:
            inside_circle += 1

    pi_estimate = 4 * inside_circle / n_samples

    return NumericalResult(
        value=pi_estimate,
        iterations=n_samples,
        converged=True,
        error=abs(pi_estimate - 3.14159265358979),
    )


def monte_carlo_integration(
    f: Callable[[float], float],
    a: float,
    b: float,
    n_samples: int = 10000,
    seed: int | None = None,
) -> NumericalResult:
    """
    Monte Carlo integration of f over [a, b].

    Args:
        f: Function to integrate.
        a: Lower bound.
        b: Upper bound.
        n_samples: Number of random samples.
        seed: Random seed for reproducibility.

    Returns:
        NumericalResult with integral estimate.
    """
    if seed is not None:
        random.seed(seed)

    total = 0.0
    for _ in range(n_samples):
        x = random.uniform(a, b)
        total += f(x)

    integral = (b - a) * total / n_samples

    return NumericalResult(
        value=integral,
        iterations=n_samples,
        converged=True,
    )


# Helper functions for common test cases
def parse_function_string(func_str: str) -> Callable[[float], float]:
    """
    Parse a simple function string into a callable.

    Supports: x, x^n, sin(x), cos(x), exp(x), sqrt(x), +, -, *, /

    Args:
        func_str: Function string like "x^2 - 2" or "sin(x)"

    Returns:
        Callable function.
    """
    import math

    def f(x: float) -> float:
        # Replace common patterns
        expr = func_str
        expr = expr.replace("^", "**")
        expr = expr.replace("sin", "math.sin")
        expr = expr.replace("cos", "math.cos")
        expr = expr.replace("tan", "math.tan")
        expr = expr.replace("exp", "math.exp")
        expr = expr.replace("sqrt", "math.sqrt")
        expr = expr.replace("log", "math.log")
        expr = expr.replace("ln", "math.log")
        return eval(expr)

    return f


def parse_derivative_string(func_str: str) -> Callable[[float], float]:
    """
    Parse derivative of common functions.

    This is a simplified version - for complex functions, use numerical derivatives.
    """
    import math

    # Simple pattern matching for common cases
    if func_str == "x^2 - 2" or func_str == "x**2 - 2":
        return lambda x: 2 * x
    elif func_str == "x^3 - x - 2" or func_str == "x**3 - x - 2":
        return lambda x: 3 * x**2 - 1
    elif func_str == "sin(x)":
        return lambda x: math.cos(x)
    elif func_str == "cos(x)":
        return lambda x: -math.sin(x)
    elif func_str == "exp(x) - 2":
        return lambda x: math.exp(x)
    else:
        # Use numerical derivative
        f = parse_function_string(func_str)
        h = 1e-8
        return lambda x: (f(x + h) - f(x - h)) / (2 * h)


# Convenience function to run any numerical algorithm
def run_numerical_algorithm(
    algorithm: str,
    **kwargs,
) -> NumericalResult:
    """
    Run a numerical algorithm by name.

    Args:
        algorithm: Algorithm name (newton_raphson, bisection, monte_carlo).
        **kwargs: Algorithm-specific arguments.

    Returns:
        NumericalResult from the algorithm.
    """
    algorithms = {
        "newton_raphson": newton_raphson,
        "newton": newton_raphson,
        "bisection": bisection,
        "monte_carlo": monte_carlo_pi,
        "monte_carlo_pi": monte_carlo_pi,
        "monte_carlo_integration": monte_carlo_integration,
    }

    algorithm = algorithm.lower().replace("-", "_")
    if algorithm not in algorithms:
        raise ValueError(f"Unknown algorithm: {algorithm}")

    func = algorithms[algorithm]

    if algorithm in ("newton_raphson", "newton"):
        f = kwargs.get("f")
        if isinstance(f, str):
            f = parse_function_string(f)
        df = kwargs.get("df")
        if isinstance(df, str):
            df = parse_derivative_string(df)
        return func(
            f,
            df,
            kwargs.get("x0", 1.0),
            kwargs.get("tol", 1e-10),
            kwargs.get("max_iter", 100),
        )
    elif algorithm == "bisection":
        f = kwargs.get("f")
        if isinstance(f, str):
            f = parse_function_string(f)
        return func(
            f,
            kwargs["a"],
            kwargs["b"],
            kwargs.get("tol", 1e-10),
            kwargs.get("max_iter", 100),
        )
    elif algorithm in ("monte_carlo", "monte_carlo_pi"):
        return func(
            kwargs.get("n_samples", 10000),
            kwargs.get("seed"),
        )
    elif algorithm == "monte_carlo_integration":
        f = kwargs.get("f")
        if isinstance(f, str):
            f = parse_function_string(f)
        return func(
            f,
            kwargs["a"],
            kwargs["b"],
            kwargs.get("n_samples", 10000),
            kwargs.get("seed"),
        )
    else:
        raise ValueError(f"Unhandled algorithm: {algorithm}")
