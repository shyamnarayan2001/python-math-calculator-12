"""
Python Math Calculator
A simple calculator for basic math operations (addition and subtraction)
"""

class Calculator:
    """A simple calculator class for basic math operations"""
    
    def __init__(self):
        """Initialize the calculator"""
        self.result = 0
    
    def add(self, num1, num2):
        """
        Add two numbers
        
        Args:
            num1 (float): First number
            num2 (float): Second number
            
        Returns:
            float: Sum of num1 and num2
        """
        self.result = num1 + num2
        return self.result
    
    def subtract(self, num1, num2):
        """
        Subtract num2 from num1
        
        Args:
            num1 (float): First number (minuend)
            num2 (float): Second number (subtrahend)
            
        Returns:
            float: Difference of num1 and num2
        """
        self.result = num1 - num2
        return self.result
    
    def get_result(self):
        """
        Get the last calculation result
        
        Returns:
            float: Last calculation result
        """
        return self.result


def main():
    """Main function to demonstrate calculator usage"""
    calc = Calculator()
    
    print("Python Math Calculator")
    print("=" * 30)
    
    # Addition examples
    print("\nAddition Examples:")
    result1 = calc.add(10, 5)
    print(f"10 + 5 = {result1}")
    
    result2 = calc.add(25.5, 14.5)
    print(f"25.5 + 14.5 = {result2}")
    
    result3 = calc.add(-10, 15)
    print(f"-10 + 15 = {result3}")
    
    # Subtraction examples
    print("\nSubtraction Examples:")
    result4 = calc.subtract(20, 8)
    print(f"20 - 8 = {result4}")
    
    result5 = calc.subtract(50.5, 25.3)
    print(f"50.5 - 25.3 = {result5}")
    
    result6 = calc.subtract(10, 30)
    print(f"10 - 30 = {result6}")
    
    print(f"\nLast result: {calc.get_result()}")


if __name__ == "__main__":
    main()
