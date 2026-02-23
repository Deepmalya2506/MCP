from server.weather import mcp
def main():
    print("Hello from weather-demo-mcp!")
    mcp.run(transport="stdio")


if __name__ == "__main__":
    print("Weather MCP server started, waiting for host connection...")
    mcp.run()

