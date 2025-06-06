# DiffPy

**DiffPy** is a Python library designed to solve mathematical problems related to differential equations. It provides simple and efficient tools for solving ordinary and partial differential equations, computing derivatives and integrals, and more. The library is written entirely in Python and is continuously evolving into a full-featured computer algebra system (CAS).

### Key Features:
- **Solving Differential Equations**: Supports solving ordinary and partial differential equations, including homogeneous and non-homogeneous cases.
- **Derivatives and Integrals**: Easily compute derivatives and integrals for various mathematical functions.
- **Extensible**: Built with simplicity in mind, making it easy to understand, extend, and contribute to.
- **Open Source**: Feel free to contribute and help improve the library.

### Usage:

To use **DiffPy** in your project, you can import the necessary components and start solving mathematical problems. Below are some examples to help you get started.

#### Example 1: Solving a First-Order Homogeneous Differential Equation

```python
from diffpy import Variable, first_order_homogeneous

x = Variable()

# Solve a first-order homogeneous differential equation
solution = first_order_homogeneous(1, -1 / x)
print(solution)  # Expected Output: y = C * x
```

#### Example 2: Calculating the Integral of a Function

```python
from diffpy import integrate, Variable, Sin, Cos

x = Variable()

# Compute the integral of sin(x)
integral = integrate(Sin(x))
print(integral) # Expected Output: -1.0*cosx
print(integral.to_dictionary())  # Expected Output: {'const': -1.0, 'func': ['cos', {'const': 1, 'func': 'x', 'pow': 1}], 'pow': 1}

# Compute the integral of 3*x + 5
integral = integrate(3*x + 5)
print(integral)  # Expected Output: (1.5*x^2 + 5*x)
print(integral.to_dictionary())  # Expected Output: {'const': 1, 'func': ['sum', {'const': 1.5, 'func': 'x', 'pow': 2}, {'const': 5, 'func': 'x', 'pow': 1}], 'pow': 1}

# Continue computations after integration
result = integral + 2*x**2 + 10 - 4*x
print(result) # Expected Output: (3.5*x^2 + x + 10.0)
```

#### Example 3: Solving an Equation Using Undetermined Coefficients

```python
from diffpy import undetermined_coefficient, Variable, Sin, Cos

x = Variable()

# Example equation with Cos and Sin terms
eq = 5*Cos(2*x) + 10*Sin(2*x)
solution = undetermined_coefficient(1, -2, 1, eq)
print(solution)  # Expected Output: y = C₁e^(1.0x) + C₂e^(1.0x) * x - 2.0sin(2x) + 1.0cos(2x)
```

### Contact Information:
For more details, questions, or contributions, feel free to reach out to the developers:

- **Tangatarov Nurzhan**: [Telegram](https://t.me/Tngtarov)
- **Syzdykova Meyirim**: [Telegram](https://t.me/meyirimq)
- **Tuleugalieva Bibi**: [Telegram](https://t.me/bbshkaaq)
