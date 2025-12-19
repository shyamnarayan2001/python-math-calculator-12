"""
Python Math Calculator
======================
A simple calculator module for performing basic mathematical operations.

Author: Narayan
Date: 2025-12-19
"""


class Calculator:
    """
    A calculator class that provides basic mathematical operations.
    
    This class implements addition and subtraction operations for two numbers.
    All operations support both integer and floating-point numbers.
    """
    
    def __init__(self):
        """Initialize the Calculator instance."""
        self.history = []
    
    def add(self, num1, num2):
        """
        Add two numbers together.
        
        Args:
            num1 (int/float): The first number
            num2 (int/float): The second number
            
        Returns:
            int/float: The sum of num1 and num2
            
        Example:
            >>> calc = Calculator()
            >>> calc.add(5, 3)
            8
            >>> calc.add(10.5, 2.3)
            12.8
        """
        result = num1 + num2
        operation = f"{num1} + {num2} = {result}"
        self.history.append(operation)
        return result
    
    def subtract(self, num1, num2):
        """
        Subtract the second number from the first number.
        
        Args:
            num1 (int/float): The number to subtract from
            num2 (int/float): The number to subtract
            
        Returns:
            int/float: The difference of num1 and num2
            
        Example:
            >>> calc = Calculator()
            >>> calc.subtract(10, 3)
            7
            >>> calc.subtract(5.5, 2.2)
            3.3
        """
        result = num1 - num2
        operation = f"{num1} - {num2} = {result}"
        self.history.append(operation)
        return result
    
    def get_history(self):
        """
        Get the history of all operations performed.
        
        Returns:
            list: A list of all operations performed
        """
        return self.history
    
    def clear_history(self):
        """Clear the operation history."""
        self.history = []


def main():
    """Main function to demonstrate calculator usage."""
    print("=" * 50)
    print("Python Math Calculator")
    print("=" * 50)
    
    calc = Calculator()
    
    # Addition examples
    print("\n--- Addition Examples ---")
    print(f"5 + 3 = {calc.add(5, 3)}")
    print(f"10.5 + 2.5 = {calc.add(10.5, 2.5)}")
    print(f"100 + 250 = {calc.add(100, 250)}")
    
    # Subtraction examples
    print("\n--- Subtraction Examples ---")
    print(f"10 - 3 = {calc.subtract(10, 3)}")
    print(f"50.8 - 20.3 = {calc.subtract(50.8, 20.3)}")
    print(f"1000 - 450 = {calc.subtract(1000, 450)}")
    
    # Display history
    print("\n--- Operation History ---")
    for operation in calc.get_history():
        print(operation)


if __name__ == "__main__":
    main()
