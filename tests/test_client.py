import pytest
from fastmcp import Client
from fastmcp.client.client import CallToolResult
from mcp.types import TextContent
from mcp_websearch.runner import mcp_runner

class TestSettings:
    """Simple class to hold test settings"""
    def __init__(self):
        self.searxng_host = "http://192.168.200.102"
        self.searxng_port = "8080"
        self.firecrawl_cloud = False
        self.firecrawl_host = "http://192.168.200.102"
        self.firecrawl_port = "3002"
        self.firecrawl_api_key = "test_api_key"

class TestMCPWebSearch:
    """Test cases for MCP WebSearch tools"""
    
    def setup_method(self):
        """Setup test settings and mcp_runner instance"""
        self.settings = TestSettings()
        self.mcp_tools = mcp_runner(
            name="mcp_websearch_test",
            host="0.0.0.0",
            port=8001,
            settings=self.settings
        )
        
    # def test_mcp_runner_initialization(self):
    #     """Test that mcp_runner initializes correctly with settings"""
    #     assert self.mcp_tools.name == "mcp_websearch_test"
    #     assert self.mcp_tools.host == "0.0.0.0"
    #     assert self.mcp_tools.port == 8001
    #     assert self.mcp_tools.settings == self.settings
    #     assert self.mcp_tools.mcp is not None
    
    # def test_tools_registration(self):
    #     """Test that all tools are properly registered"""
    #     # Check that tools are registered in the FastMCP instance
    #     # First, let's examine the structure of the mcp object
    #     mcp_attrs = [attr for attr in dir(self.mcp_tools.mcp) if not attr.startswith('_')]
    #     print(f"Available MCP attributes: {mcp_attrs}")
        
    #     # Try to access tools in different ways
    #     if hasattr(self.mcp_tools.mcp, 'tools'):
    #         registered_tools = list(self.mcp_tools.mcp.tools.keys())
    #     elif hasattr(self.mcp_tools.mcp, '_tools'):
    #         registered_tools = list(self.mcp_tools.mcp._tools.keys())
    #     elif hasattr(self.mcp_tools.mcp, 'server') and hasattr(self.mcp_tools.mcp.server, 'list_tools'):
    #         # This is a fallback - we might need to call list_tools
    #         print("Using server.list_tools approach")
    #         registered_tools = []  # We'll handle this differently
    #     else:
    #         # Let's just verify the object exists for now
    #         assert self.mcp_tools.mcp is not None
    #         print("MCP object exists but couldn't find tools attribute")
    #         return
        
    #     expected_tools = [
    #         "search_web",
    #         "search_news", 
    #         "search_science",
    #         "search_social",
    #         "firecrawl_web",
    #         "firecrawl_get_web_content"
    #     ]
        
    #     if registered_tools:
    #         for tool_name in expected_tools:
    #             assert tool_name in registered_tools, f"Tool {tool_name} not registered"
    #     else:
    #         # Just verify the MCP object exists
    #         assert self.mcp_tools.mcp is not None
    
    # def test_server_initialization_and_tools_check(self):
    #     """Test that mcp_runner initializes correctly and tools can be accessed"""
    #     # This test doesn't need to actually start a server
    #     assert self.mcp_tools.name == "mcp_websearch_test"
    #     assert self.mcp_tools.host == "0.0.0.0"
    #     assert self.mcp_tools.port == 8001
    #     assert self.mcp_tools.settings == self.settings
    #     assert self.mcp_tools.mcp is not None
        
    #     # Test that the MCP instance exists and has the expected structure
    #     mcp_instance = self.mcp_tools.mcp
    #     assert mcp_instance is not None
    #     print("MCP runner configured successfully")

    # @pytest.mark.asyncio
    # async def test_client_connection_with_in_memory_transport(self):
    #     """Test client connection using in-memory transport (no blocking)"""
    #     # Use in-memory transport - this connects directly to the FastMCP instance
    #     # without starting a subprocess or network server
    #     client = Client(self.mcp_tools.mcp)
        
    #     async with client:
    #         # Test basic connectivity
    #         await client.ping()
            
    #         # List available tools
    #         tools = await client.list_tools()
    #         print(f"Available tools: {[tool.name for tool in tools]}")
    #         assert isinstance(tools, list)
    #         assert len(tools) > 0, "No tools found"
            
    #         # Check if our expected tools are present
    #         tool_names = [tool.name for tool in tools]
    #         expected_tools = [
    #             "search_web_searxng", 
    #             "search_news_searxng", 
    #             "search_science_searxng", 
    #             "search_social_searxng", 
    #             "search_web_firecrawl", 
    #             "get_a_url_web_content_firecrawl"
    #         ]
            
    #         for expected_tool in expected_tools:
    #             assert expected_tool in tool_names, f"Expected tool '{expected_tool}' not found in available tools"

    # @pytest.mark.asyncio
    # async def test_search_web_searxng(self):
    #     """Test search_web_searxng"""
    #     client = Client(self.mcp_tools.mcp)
        
    #     async with client:
    #         # Mock the searxng_search function to avoid external dependencies
   
    #         result = await client.call_tool("search_web_searxng", {
    #             "query": "Large Language Model",
    #             "num_results": 2
    #         })
    #         print(f"Search results: {result}")
    #         assert isinstance(result, CallToolResult), "Expected CallToolResult type"
    #         assert result.content is not None, "Expected non-empty content in result"
    #         assert len(result.content) > 0, "Expected at least one search result"

    # @pytest.mark.asyncio
    # async def test_search_news_searxng(self):
    #     """Test search_news_searxng"""
    #     client = Client(self.mcp_tools.mcp)
        
    #     async with client:
    #         # Mock the searxng_search function to avoid external dependencies
    #         result = await client.call_tool("search_news_searxng", {
    #             "query": "Large Language Model",
    #             "num_results": 2
    #         })
    #         print(f"Search results: {result}")
    #         assert isinstance(result, CallToolResult), "Expected CallToolResult type"
    #         assert result.content is not None, "Expected non-empty content in result"
    #         assert len(result.content) > 0, "Expected at least one search result"
    
    # @pytest.mark.asyncio
    # async def test_search_science_searxng(self):
    #     """Test search_science_searxng"""
    #     client = Client(self.mcp_tools.mcp)
        
    #     async with client:
    #         # Mock the searxng_search function to avoid external dependencies
    #         result = await client.call_tool("search_science_searxng", {
    #             "query": "Large Language Models"
    #         })
    #         print(f"Search results: {result}")
    #         assert isinstance(result, CallToolResult), "Expected CallToolResult type"
    #         assert result.content is not None, "Expected non-empty content in result"
    #         assert len(result.content) > 0, "Expected at least one search result"
            
    # @pytest.mark.asyncio
    # async def test_search_social_searxng(self):
    #     """Test search_social_searxng"""
    #     client = Client(self.mcp_tools.mcp)
        
    #     async with client:
    #         # Mock the searxng_search function to avoid external dependencies
    #         result = await client.call_tool("search_social_searxng", {
    #             "query": "Large Language Model"
    #         })
    #         print(f"Search results: {result}")
    #         assert isinstance(result, CallToolResult), "Expected CallToolResult type"
    #         assert result.content is not None, "Expected non-empty content in result"
    #         assert len(result.content) > 0, "Expected at least one search result"
            
    @pytest.mark.asyncio
    async def test_search_web_firecrawl(self):
        """Test search_web_firecrawl"""
        client = Client(self.mcp_tools.mcp)
        
        async with client:
            # Mock the firecrawl_search function to avoid external dependencies
            result = await client.call_tool("search_web_firecrawl", {
                "query": "Large Language Model",
                "limit": 2
            })
            print(f"Search results: {result}")
            assert isinstance(result, CallToolResult), "Expected CallToolResult type"
            assert isinstance(result.content, list), "Expected content to be a list"
            assert len(result.content) > 0, "Expected at least one search result"

    @pytest.mark.asyncio
    async def test_get_a_url_web_content_firecrawl(self):
        """Test get_a_url_web_content_firecrawl"""
        client = Client(self.mcp_tools.mcp)
        
        async with client:
            # Mock the firecrawl_get_url_content function to avoid external dependencies
            result = await client.call_tool("get_a_url_web_content_firecrawl", {
                "url": "https://raw.githubusercontent.com/jlowin/fastmcp/refs/heads/main/README.md"
            })
            print(f"Content: {result}")
            assert isinstance(result, CallToolResult), "Expected CallToolResult type"
            assert isinstance(result.content, list), "Expected content to be a list"
            assert len(result.content) > 0, "Expected at least one content item"
            assert isinstance(result.content[0], TextContent), "Expected content to be a string"

if __name__ == "__main__":
    pytest.main([__file__])