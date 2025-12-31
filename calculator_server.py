from fastmcp import FastMCP

mcp = FastMCP("Calculator")

@mcp.tool()
def add(a: float, b: float) -> float:
    """
    Takes two numbers as input and returns their sum
    """
    print(f"Adding {a} + {b}")
    return a + b

@mcp.tool()
def subtract(a: float, b: float) -> float:
    """Takes two numbers as input and returns their difference"""
    print(f"Subtracting {a} - {b}")
    return a - b

@mcp.tool()
def multiply(a: float, b: float) -> float:
    """Takes two numbers as input and returns their product"""
    print(f"Multiplying {a} * {b}")
    return a * b

@mcp.tool()
def divide(a: float, b: float) -> float:
    """Takes two numbers as input and returns their quotient"""
    print(f"Dividing {a} / {b}")
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
