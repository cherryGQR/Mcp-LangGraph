from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI
import asyncio
import os
from dotenv import load_dotenv

# 加载环境变量（可选）
load_dotenv()

# MCP服务配置
CLIENT_CONFIG = {
    "math": {
        "command": "python",
        # 建议使用相对路径，方便不同环境部署
        "args": [os.path.join(os.path.dirname(__file__), "math_server_demo.py")],
        "transport": "stdio",
    },
    "weather": {
        "url": "http://localhost:8009/mcp",
        "transport": "streamable_http",
    }
}

# 主LLM配置（可通过环境变量覆盖）
llm = ChatOpenAI(
    max_retries=2,
    model=os.getenv("LLM_MODEL", "QWQ-32B"),
    api_key=os.getenv("LLM_API_KEY", "QWQ_32B_RTAwMjI5NzEmUVdRXzMyQiYyMDI1LzUvOA=="),
    base_url=os.getenv("LLM_BASE_URL", "http://t-llmserver.ai.cdtp.com/v1/"),
    # temperature=0.7,
    # streaming=True
)

# 测试用LLM配置
llm_test = ChatOpenAI(
    max_retries=2,
    model=os.getenv("TEST_LLM_MODEL", "DeepSeek-R1-fp8"),
    api_key=os.getenv("TEST_LLM_API_KEY", "sglang_DeepSeek_R1_fp8_test"),
    base_url=os.getenv("TEST_LLM_BASE_URL", "http://llmserver.ai.cxmt.com/v1/"),
    # temperature=0.7,
    # streaming=True
)


async def main():
    """主函数：初始化MCP客户端并调用服务"""
    try:
        # 初始化MCP客户端
        client = MultiServerMCPClient(CLIENT_CONFIG)

        # 获取MCP工具
        tools = await client.get_tools()
        print(f"成功加载 {len(tools)} 个MCP工具")

        # 创建ReAct Agent
        agent = create_react_agent(
            model=llm_test,
            tools=tools
        )

        # 执行数学查询
        print("\n=== 执行数学计算 ===")
        math_response = await agent.ainvoke({
            "messages": [{"role": "user", "content": "请帮忙计算 (3 + 5) x 12"}]
        })
        print("数学计算结果:", math_response["messages"][-1]["content"])

        # 执行天气查询
        print("\n=== 执行天气查询 ===")
        weather_response = await agent.ainvoke({
            "messages": [{"role": "user", "content": "帮我查询nyc天气?"}]
        })
        print("天气查询结果:", weather_response["messages"][-1]["content"])

    except Exception as e:
        print(f"执行出错: {e}")
    finally:
        # 清理资源
        await client.close()


if __name__ == "__main__":
    # 启动异步事件循环
    asyncio.run(main())