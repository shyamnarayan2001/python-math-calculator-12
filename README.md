# Python Math Calculator

A simple Python calculator application for basic math operations.

## Features

- Addition of two numbers
- Subtraction of two numbers
- Support for both integers and floating-point numbers
- Clean and well-documented code

## Project Structure

```
python-math-calculator-12/
├── calculator.py          # Main calculator module
├── tests/                 # Test directory
│   ├── __init__.py
│   └── test_calculator.py # Unit tests
├── requirements.txt       # Project dependencies
├── .gitignore            # Git ignore file
└── README.md             # This file
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

### As a standalone script:

```bash
python calculator.py
```

### As a module:

```python
from calculator import Calculator

# Create calculator instance
calc = Calculator()

# Perform addition
result = calc.add(10, 5)
print(f"Result: {result}")  # Output: Result: 15

# Perform subtraction
result = calc.subtract(20, 8)
print(f"Result: {result}")  # Output: Result: 12
```

## Running Tests

```bash
python -m pytest tests/
```

## API Reference

### Calculator Class

#### `add(num1, num2)`
Add two numbers together.

- **Parameters:**
  - `num1` (float): First number
  - `num2` (float): Second number
- **Returns:** float - Sum of the two numbers

#### `subtract(num1, num2)`
Subtract the second number from the first.

- **Parameters:**
  - `num1` (float): First number (minuend)
  - `num2` (float): Second number (subtrahend)
- **Returns:** float - Difference of the two numbers

#### `get_result()`
Get the result of the last calculation.

- **Returns:** float - Last calculation result

## Examples

```python
from calculator import Calculator

calc = Calculator()

# Addition examples
print(calc.add(10, 5))      # Output: 15
print(calc.add(25.5, 14.5)) # Output: 40.0
print(calc.add(-10, 15))    # Output: 5

# Subtraction examples
print(calc.subtract(20, 8))     # Output: 12
print(calc.subtract(50.5, 25.3)) # Output: 25.2
print(calc.subtract(10, 30))    # Output: -20
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is open source and available under the MIT License.

## Author

Shyam Narayan - [shyamnarayan2001](https://github.com/shyamnarayan2001)

## Acknowledgments

- Built with Python 3.x
- Follows PEP 8 style guidelines
