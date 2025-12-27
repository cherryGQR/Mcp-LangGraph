from mcp.server.fastmcp import FastMCP
import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 配置服务参数（优先从环境变量读取）
HOST = os.getenv("FASTMCP_HOST", "0.0.0.0")
PORT = int(os.getenv("FASTMCP_PORT", "8009"))
PATH = os.getenv("FASTMCP_STREAMABLE_HTTP_PATH", "/mcp")

# 初始化MCP服务
mcp = FastMCP("Weather")


@mcp.tool()
async def get_weather(location: str) -> str:
    """
    Get weather information for a specific location

    Args:
        location: Location to get weather for (city name, zip code, etc.)

    Returns:
        Weather description for the location
    """
    # 模拟天气数据
    weather_data = {
        "nyc": "It's always sunny in New York (25°C)",
        "london": "Cloudy with a chance of rain (18°C)",
        "tokyo": "Sunny with light breeze (28°C)",
        "paris": "Mild and pleasant (20°C)"
    }

    # 转换为小写并提取主要城市名
    loc = location.lower()
    for city in weather_data:
        if city in loc:
            return weather_data[city]

    # 默认返回
    return f"Weather data not available for {location}. Default: Sunny (22°C)"


if __name__ == "__main__":
    print(f"启动天气MCP服务: http://{HOST}:{PORT}{PATH}")

    # 设置环境变量
    os.environ["FASTMCP_HOST"] = HOST
    os.environ["FASTMCP_PORT"] = str(PORT)
    os.environ["FASTMCP_STREAMABLE_HTTP_PATH"] = PATH

    # 运行MCP服务
    mcp.run(
        transport="streamable-http",
    )