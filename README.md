# Fraction Class in Python

This repository contains a Python implementation of a Fraction class, which represents a mathematical fraction and provides functionality for performing various operations on fractions.

## Features

The `Fraction` class supports the following operations:

- Creation of fractions with a numerator and a denominator.
- Addition, subtraction, multiplication, and division of fractions.
- Reduction of fractions to their simplest form.
- Comparison of fractions.
- String representation of fractions.

## Usage

Here's a basic example of how to use the `Fraction` class:

```python
from fraction import Fraction

# Create two fractions
frac1 = Fraction(1, 2)
frac2 = Fraction(3, 4)

# Perform arithmetic operations
result = frac1 + frac2
print(result)  # Prints: 5/4

# Compare fractions
print(frac1 > frac2)  # Prints: False
