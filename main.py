# CLI 參數解析器
import argparse
import os
from dotenv import load_dotenv

# 載入 .env 文件
load_dotenv()

def parse_args():
    parser = argparse.ArgumentParser(description="MCP WebSearch Settings")
    parser.add_argument("--searxng-host", type=str, default=os.getenv("SEARXNG_HOST", "http://localhost"), help="SearxNG host URL")
    parser.add_argument("--searxng-port", type=str, default=os.getenv("SEARXNG_PORT", "8080"), help="SearxNG port")
    parser.add_argument("--firecrawl-cloud", action="store_true", help="Use Firecrawl cloud service")
    parser.add_argument("--firecrawl-host", type=str, default=os.getenv("FIRECRAWL_HOST", "http://localhost"), help="Firecrawl host URL")
    parser.add_argument("--firecrawl-port", type=str, default=os.getenv("FIRECRAWL_PORT", "3002"), help="Firecrawl port")
    parser.add_argument("--firecrawl-api-key", type=str, default=os.getenv("FIRECRAWL_API_KEY", "firecrawl_api_key"), help="Firecrawl API key")
    return parser.parse_args()
settings = parse_args()
print(settings)
# from mcp.server.fastmcp import FastMCP
# from mcp_websearch.searxng.searxng_search import searxng_search
# from mcp_websearch.firecrawl.firecrawl_search import firecrawl_search, firecrawl_get_url_content

# mcp = FastMCP("mcp_searxng", host="0.0.0.0", port=8000)

# @mcp.tool()
# def search_web(query: str, num_results: int = 3):
#     """Search web using SearxNG."""
#     results = searxng_search("web", query, num_results=num_results, host=settings.searxng_host, port=settings.searxng_port)
#     return results

# @mcp.tool()
# def search_news(query: str, num_results: int = 3):
#     """Search news using SearxNG."""
#     results = searxng_search("news", query, num_results=num_results, host=settings.searxng_host, port=settings.searxng_port)
#     return results

# @mcp.tool()
# def search_science(query: str):
#     """Search science articles using SearxNG."""
#     results = searxng_search("science", query, num_results=3, host=settings.searxng_host, port=settings.searxng_port)
#     return results

# @mcp.tool()
# def search_social(query: str):
#     """Search social media using SearxNG."""
#     results = searxng_search("social", query, num_results=3, host=settings.searxng_host, port=settings.searxng_port)
#     return results

# @mcp.tool()
# def firecrawl_web(query: str, limit: int = 3):
#     """
#     Perform a web search using the Firecrawl search engine.

#     Args:
#         query (str): The search query.
#         limit (int): The maximum number of results to return.
    
#     Returns:
#         list: A list of search results, each containing a title and content.
#     """
#     results = firecrawl_search(query, limit, cloud=settings.firecrawl_cloud, host=settings.firecrawl_host, port=settings.firecrawl_port, api_key=settings.firecrawl_api_key)
#     return results

# @mcp.tool()
# def firecrawl_get_web_content(url: str):
#     """
#     Get the content of a URL using Firecrawl.

#     Args:
#         url (str): The URL to fetch content from.
    
#     Returns:
#         str: The content of the URL in markdown format.
#     """
#     content = firecrawl_get_url_content(url, cloud=settings.firecrawl_cloud, host=settings.firecrawl_host, port=settings.firecrawl_port, api_key=settings.firecrawl_api_key)
#     return content

# def main():
#     """Run the MCP server"""
#     mcp.run(transport="streamable-http")

# if __name__ == "__main__":
#     main()

from mcp_websearch.runner import mcp_runner

mcp_tools = mcp_runner(
    name="mcp_websearch",
    host="0.0.0.0",
    port=8000,
    settings=settings
)

mcp_tools.run(transport="streamable-http")