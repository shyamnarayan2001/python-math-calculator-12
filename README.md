# Python Math Calculator

A simple Python calculator application that performs basic math operations (addition and subtraction).

## Features

- **Addition**: Add two numbers together
- **Subtraction**: Subtract one number from another
- **Calculation History**: Track all calculations performed
- **Support for Multiple Number Types**: Works with integers, floats, and negative numbers

## Project Structure

```
python-math-calculator-12/
├── calculator.py           # Main calculator module
├── tests/
│   ├── __init__.py
│   └── test_calculator.py # Unit tests
├── README.md              # Project documentation
├── requirements.txt       # Python dependencies
├── .gitignore            # Git ignore file
└── setup.py              # Package setup file
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/shyamnarayan2001/python-math-calculator-12.git
cd python-math-calculator-12
```

2. Install dependencies (if any):
```bash
pip install -r requirements.txt
```

## Usage

### As a Module

```python
from calculator import Calculator

# Create calculator instance
calc = Calculator()

# Perform calculations
result1 = calc.add(10, 5)        # Returns: 15
result2 = calc.subtract(20, 8)   # Returns: 12

# View calculation history
history = calc.get_history()
print(history)

# Clear history
calc.clear_history()
```

### Run the Demo

```bash
python calculator.py
```

## Running Tests

Run the unit tests using unittest:

```bash
python -m unittest discover tests
```

Or run specific test file:

```bash
python tests/test_calculator.py
```

## API Reference

### Calculator Class

#### Methods

- `add(a, b)`: Add two numbers and return the result
  - Parameters: `a` (float), `b` (float)
  - Returns: float

- `subtract(a, b)`: Subtract b from a and return the result
  - Parameters: `a` (float), `b` (float)
  - Returns: float

- `get_history()`: Get list of all calculations performed
  - Returns: list of strings

- `clear_history()`: Clear the calculation history
  - Returns: None

## Examples

### Addition Examples

```python
calc = Calculator()

print(calc.add(10, 5))       # Output: 15
print(calc.add(25.5, 14.3))  # Output: 39.8
print(calc.add(-8, 15))      # Output: 7
```

### Subtraction Examples

```python
calc = Calculator()

print(calc.subtract(20, 8))      # Output: 12
print(calc.subtract(100, 45.5))  # Output: 54.5
print(calc.subtract(5, 12))      # Output: -7
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Author

Shyam Narayan

## Repository

GitHub: [python-math-calculator-12](https://github.com/shyamnarayan2001/python-math-calculator-12)
