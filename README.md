# MathDesk

MathDesk is a lightweight desktop mathematics application built with Python. It is designed to help users quickly perform mathematical calculations, verify functions, solve equations, and compute calculus problems without the need for a large computer algebra system.

The goal of MathDesk is to provide a simple and easy-to-use tool for students, educators, and anyone who needs to perform short mathematical tasks efficiently.

## Features

### Basic Calculator

Perform common mathematical calculations, including:

* Addition, subtraction, multiplication, and division
* Powers and roots
* Logarithmic functions
* Trigonometric functions
* Absolute value
* Most standard mathematical expressions

### Function Plotting

Plot mathematical functions by entering a function and its plotting range.

* Supports custom plotting ranges
* Variable name must be **`x`**
* Quick visualization for function verification

### Calculus

Perform common calculus operations, including:

* Indefinite integration
* Definite integration
* Differentiation
* Derivative evaluation at a specific point
* Variable name must be **`x`**

Simply enter the function and the required information to obtain the result.

### Equation Solver

Solve equations using either symbolic or numerical methods.

* Symbolic equation solving
* Numerical equation solving
* Variable name must be **`x`**

### Clear Function

Each module includes a **Clear** button that instantly clears all input fields within that section, allowing users to quickly perform another calculation.

## Technologies

MathDesk is built with the following libraries:

* **CustomTkinter (CTk)** – Graphical User Interface
* **math** – Standard mathematical functions
* **NumPy** – Numerical computation
* **SymPy** – Symbolic mathematics
* **Matplotlib** – Function plotting

## Installation

1. Clone this repository:

```bash
git clone https://github.com/veratic-labs/math-desk.git
cd math-desk
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Launch the application:

```bash
python main.py
```

> **Note:** The project consists of multiple Python files, but only `main.py` needs to be executed. All other modules are imported automatically.


## License

This project is licensed under the **Apache License 2.0**. See the `LICENSE` file for more information.

Copyright (c) 2026 Veratic Labs



