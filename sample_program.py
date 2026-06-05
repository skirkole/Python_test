"""Sample Python program demonstrating basic functions, I/O, and NumPy array addition."""

import numpy as np


def greet(name: str) -> str:
    """Return a greeting message for the given name."""
    return f"Hello, {name}! Welcome to Python."


def add_numbers(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b


def add_numpy_arrays(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    """Return the element-wise sum of two NumPy arrays."""
    return a + b


def main() -> None:
    """Main entry point for the sample program."""
    print("Sample Python Program")
    print("---------------------")

    name = input("Enter your name: ")
    print(greet(name))

    try:
        x = int(input("Enter the first number: "))
        y = int(input("Enter the second number: "))
        print(f"{x} + {y} = {add_numbers(x, y)}")
    except ValueError:
        print("Please enter valid integers.")

    print("\nNumPy sample array addition:")
    array_a = np.array([1, 2, 3])
    array_b = np.array([4, 5, 6])
    result = add_numpy_arrays(array_a, array_b)
    print(f"Array A: {array_a}")
    print(f"Array B: {array_b}")
    print(f"A + B = {result}")


if __name__ == "__main__":
    main()
