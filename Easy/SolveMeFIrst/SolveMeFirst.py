
def solveMeFirst(a: int, b: int) -> int:
    """
    Does the sum of two integers
    
    Args:
        a (int): The first integer
        b (int): The second integer
        
    Returns: The sum of a and b
    """
    return a + b
   
if __name__ == "__main__":
    num1 = int(input("Enter first number: ")) # 2
    num2 = int(input("Enter second number: ")) # 3
    res = solveMeFirst(num1, num2)
    print("Result is", res) # 5

