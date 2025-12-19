"""
Python Math Calculator
A simple calculator module for basic math operations.
"""

class Calculator:
    """A calculator class for performing basic math operations."""
    
    def __init__(self):
        """Initialize the calculator."""
        self.history = []
    
    def add(self, a, b):
        """
        Add two numbers.
        
        Args:
            a (float): First number
            b (float): Second number
            
        Returns:
            float: Sum of a and b
        """
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a, b):
        """
        Subtract second number from first number.
        
        Args:
            a (float): First number
            b (float): Second number
            
        Returns:
            float: Difference of a and b
        """
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def get_history(self):
        """
        Get calculation history.
        
        Returns:
            list: List of previous calculations
        """
        return self.history
    
    def clear_history(self):
        """Clear calculation history."""
        self.history = []


def main():
    """Main function to demonstrate calculator usage."""
    calc = Calculator()
    
    print("Python Math Calculator")
    print("=" * 30)
    
    # Addition examples
    print(f"\nAddition:")
    print(f"10 + 5 = {calc.add(10, 5)}")
    print(f"25.5 + 14.3 = {calc.add(25.5, 14.3)}")
    print(f"-8 + 15 = {calc.add(-8, 15)}")
    
    # Subtraction examples
    print(f"\nSubtraction:")
    print(f"20 - 8 = {calc.subtract(20, 8)}")
    print(f"100 - 45.5 = {calc.subtract(100, 45.5)}")
    print(f"5 - 12 = {calc.subtract(5, 12)}")
    
    # Display history
    print(f"\nCalculation History:")
    for entry in calc.get_history():
        print(f"  {entry}")


if __name__ == "__main__":
    main()
