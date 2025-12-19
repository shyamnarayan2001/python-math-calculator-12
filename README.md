# Python Math Calculator

A simple, well-documented Python calculator library for performing basic mathematical operations.

## Features

- ✅ **Addition**: Add two numbers (integers or floats)
- ✅ **Subtraction**: Subtract one number from another
- ✅ **Operation History**: Track all performed operations
- ✅ **Comprehensive Tests**: Full unit test coverage
- ✅ **Type Support**: Works with both integers and floating-point numbers

## Installation

Clone the repository:

```bash
git clone https://github.com/shyamnarayan2001/python-math-calculator-12.git
cd python-math-calculator-12
```

Install the package:

```bash
pip install -e .
```

## Usage

### Basic Usage

```python
from calculator import Calculator

# Create a calculator instance
calc = Calculator()

# Perform addition
result = calc.add(5, 3)
print(f"5 + 3 = {result}")  # Output: 5 + 3 = 8

# Perform subtraction
result = calc.subtract(10, 4)
print(f"10 - 4 = {result}")  # Output: 10 - 4 = 6
```

### Working with Decimals

```python
calc = Calculator()

# Float addition
result = calc.add(10.5, 2.3)
print(result)  # Output: 12.8

# Float subtraction
result = calc.subtract(50.8, 20.3)
print(result)  # Output: 30.5
```

### Operation History

```python
calc = Calculator()

calc.add(5, 3)
calc.subtract(10, 2)
calc.add(100, 50)

# Get operation history
history = calc.get_history()
for operation in history:
    print(operation)

# Output:
# 5 + 3 = 8
# 10 - 2 = 8
# 100 + 50 = 150

# Clear history
calc.clear_history()
```

### Running the Demo

Run the built-in demonstration:

```bash
python calculator.py
```

## API Reference

### Calculator Class

#### `__init__()`
Initialize a new Calculator instance with empty history.

#### `add(num1, num2)`
Add two numbers together.

**Parameters:**
- `num1` (int/float): The first number
- `num2` (int/float): The second number

**Returns:** (int/float) The sum of num1 and num2

#### `subtract(num1, num2)`
Subtract the second number from the first number.

**Parameters:**
- `num1` (int/float): The number to subtract from
- `num2` (int/float): The number to subtract

**Returns:** (int/float) The difference of num1 and num2

#### `get_history()`
Get the history of all operations performed.

**Returns:** (list) A list of all operations as strings

#### `clear_history()`
Clear the operation history.

## Running Tests

Run the test suite:

```bash
# Run all tests
python -m pytest tests/

# Run with verbose output
python -m pytest tests/ -v

# Run specific test file
python tests/test_calculator.py
```

## Test Coverage

The project includes comprehensive unit tests covering:

- ✅ Addition with positive numbers
- ✅ Addition with negative numbers
- ✅ Addition with mixed signs
- ✅ Addition with floating-point numbers
- ✅ Addition with zero
- ✅ Addition with large numbers
- ✅ Subtraction with positive numbers
- ✅ Subtraction with negative numbers
- ✅ Subtraction with mixed signs
- ✅ Subtraction with floating-point numbers
- ✅ Subtraction with zero
- ✅ Subtraction resulting in negative
- ✅ Operation history tracking
- ✅ History clearing

## Project Structure

```
python-math-calculator-12/
├── calculator.py           # Main calculator module
├── tests/
│   ├── __init__.py
│   └── test_calculator.py  # Unit tests
├── README.md               # This file
├── requirements.txt        # Project dependencies
├── setup.py               # Package setup configuration
└── .gitignore            # Git ignore patterns
```

## Requirements

- Python 3.7+
- pytest (for running tests)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Author

**Narayan Krishnamurthy Shyam**
- GitHub: [@shyamnarayan2001](https://github.com/shyamnarayan2001)
- Email: shyamnarayan2001@gmail.com

## Version History

- **v1.0.0** (2025-12-19)
  - Initial release
  - Addition and subtraction operations
  - Operation history tracking
  - Comprehensive unit tests
