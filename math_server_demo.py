from mcp.server.fastmcp import FastMCP

# 初始化MCP服务
mcp = FastMCP("Math")


@mcp.tool()
def add(a: int, b: int) -> int:
    """
    Add two numbers

    Args:
        a: First number
        b: Second number

    Returns:
        Sum of a and b
    """
    return a + b


@mcp.tool()
def multiply(a: int, b: int) -> int:
    """
    Multiply two numbers

    Args:
        a: First number
        b: Second number

    Returns:
        Product of a and b
    """
    return a * b


@mcp.tool()
def subtract(a: int, b: int) -> int:
    """
    Subtract two numbers

    Args:
        a: Minuend
        b: Subtrahend

    Returns:
        Difference of a and b
    """
    return a - b


if __name__ == "__main__":
    # 运行MCP服务（stdio传输）
    mcp.run(transport="stdio")