# MCP (Model Context Protocol) Demo

一个简单的MCP示例项目，展示如何使用MultiServerMCPClient连接多个MCP服务（数学计算和天气查询）。

## 功能说明
- **数学服务**：通过stdio传输协议提供加减乘除计算
- **天气服务**：通过HTTP流式传输协议提供天气查询
- **客户端**：使用LangGraph创建ReAct Agent，调用多个MCP服务

## 环境要求
- Python 3.8+
- 依赖包见requirements.txt

## 安装依赖
```bash
pip install -r requirements.txt