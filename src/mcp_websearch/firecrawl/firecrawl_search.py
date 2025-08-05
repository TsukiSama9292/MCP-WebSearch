import httpx

def firecrawl_get_url_content(url: str, cloud: bool = False, host: str = "http://localhost", port: str = "3002", api_key: str = "firecrawl_api_key") -> str:
    """
    Get the content of a URL using Firecrawl.

    Args:
        url (str): The URL to fetch content from.
    
    Returns:
        str: The content of the URL in markdown format.
    """
    if cloud:
        api_url = f"https://api.firecrawl.dev/v1/scrape"
    else:
        api_url = f"{host}:{port}/v1/scrape"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }
    payload = {
        "url": url,
        "formats": ["markdown"],
    }
    response = httpx.post(api_url, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()["data"].get("markdown","")

def firecrawl_search(query: str, limit: int = 3, cloud: bool = False, host: str = "http://localhost", port: str = "3002", api_key: str = "firecrawl_api_key") -> list:
    """
    Perform a web search using the Firecrawl search engine.

    Args:
        query (str): The search query.
        limit (int): The maximum number of results to return.
    
    Returns:
        list: A list of search results, each containing a title and content.
    """
    if cloud:
        url = "https://api.firecrawl.dev/v1/search"
    else:
        url = f"{host}:{port}/v1/search"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }
    payload = {
        "query": query,
        "limit": limit,
    }
    try:
        response = httpx.post(url, headers=headers, json=payload)
        response.raise_for_status()
        results = response.json()
        result = []
        if results["success"] is True:
            for data in results["data"]:
                title = data.get("title", "No title")
                content = firecrawl_get_url_content(data["url"], cloud=cloud, host=host, port=port, api_key=api_key)
                if content:
                    result.append({
                        "title": title,
                        "content": content
                    })  
            return result
        else:
            print("No results found or search failed.")
            return []
    except httpx.HTTPStatusError as e:
        print(f"HTTP error occurred: {e.response.status_code} - {e.response.text}")
        return []

if __name__ == "__main__":
    query = "what is firecrawl?"
    results = firecrawl_search(query)
    for result in results:
        print(f"Title: {result['title']}")
        print(f"Content: {result['content'][:100]}...")  # Print first 100 characters of content
        print()