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

from mcp.server.fastmcp import FastMCP
from mcp_websearch.searxng.searxng_search import searxng_search
from mcp_websearch.firecrawl.firecrawl_search import firecrawl_search, firecrawl_get_url_content

class mcp_runner():
    def __init__(self, name, host, port, settings):
        self.name = name
        self.host = host
        self.port = port
        self.settings = settings
        self.mcp = FastMCP(self.name, host=self.host, port=self.port)
        @self.mcp.tool()
        def search_web_searxng(query: str, num_results: int = 3):
            """Search web using SearXNG."""
            results = searxng_search("web", query, num_results=num_results, host=self.settings.searxng_host, port=self.settings.searxng_port)
            return results

        @self.mcp.tool()
        def search_news_searxng(query: str, num_results: int = 3):
            """Search news using SearXNG."""
            results = searxng_search("news", query, num_results=num_results, host=self.settings.searxng_host, port=self.settings.searxng_port)
            return results

        @self.mcp.tool()
        def search_science_searxng(query: str):
            """Search science articles using SearXNG."""
            results = searxng_search("science", query, num_results=3, host=self.settings.searxng_host, port=self.settings.searxng_port)
            return results

        @self.mcp.tool()
        def search_social_searxng(query: str):
            """Search social media using SearXNG."""
            results = searxng_search("social", query, num_results=3, host=self.settings.searxng_host, port=self.settings.searxng_port)
            return results

        @self.mcp.tool()
        def search_web_firecrawl(query: str, limit: int = 3):
            """
            Perform a web search using the Firecrawl search engine.

            Args:
                query (str): The search query.
                limit (int): The maximum number of results to return.
            
            Returns:
                list: A list of search results, each containing a title and content.
            """
            results = firecrawl_search(query, limit, cloud=self.settings.firecrawl_cloud, host=self.settings.firecrawl_host, port=self.settings.firecrawl_port, api_key=self.settings.firecrawl_api_key)
            return results

        @self.mcp.tool()
        def get_a_url_web_content_firecrawl(url: str):
            """
            Get the content of a URL using Firecrawl.

            Args:
                url (str): The URL to fetch content from.
            
            Returns:
                str: The content of the URL in markdown format.
            """
            content = firecrawl_get_url_content(url, cloud=self.settings.firecrawl_cloud, host=self.settings.firecrawl_host, port=self.settings.firecrawl_port, api_key=self.settings.firecrawl_api_key)
            return content
    
    def run(self, transport="streamable-http"):
        """Run the MCP server"""
        self.mcp.run(transport=transport)

    def async_run(self, transport="streamable-http"):
        self.mcp.run_async(transport=transport)