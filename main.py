import httpx
from mcp.server.fastmcp import FastMCP
from mcp_searxng.searxng.search import get_search

mcp = FastMCP("mcp_searxng", host="0.0.0.0", port=8000)

@mcp.tool()
def search_web(query: str):
    """Search the web using SearxNG."""
    results = get_search("web", query)
    return results

@mcp.tool()
def search_news(query: str):
    """Search news using SearxNG."""
    results = get_search("news", query)
    return results

@mcp.tool()
def search_science(query: str):
    """Search science articles using SearxNG."""
    results = get_search("science", query)
    return results

@mcp.tool()
def search_social(query: str):
    """Search social media using SearxNG."""
    results = get_search("social", query)
    return results

def main():
    """Run the MCP server"""
    mcp.run(transport="streamable-http")

if __name__ == "__main__":
    main()