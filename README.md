# MCP-WebSearch

為 AI Agent 提供網頁搜尋 MCP 工具  
通過 `.env` 或 `.env.local` 的環境參數使用本 MCP 工具  

## 支援工具

- SearXNG: 集成多種搜尋引擎，如: google, bing, yahoo...
- FireCrawl: 具備強大的搜尋功能，如: 取得指定 URL 網頁的 Markdown 文字 

## 快速啟動

```bash
docker compose up -d
```

## 範例 `.env`

- `SEARXNG_HOST`: 部屬 SearXNG 的主機 IP 位置
- `SEARXNG_PORT`: 部屬 SearXNG 暴露的 Port
- `FIRECRAWL_CLOUD`: 選擇是否使用雲端 FireCrawl
- `FIRECRAWL_HOST`: 部屬 FireCrawl 的主機 IP 位置
- `FIRECRAWL_PORT`: 部屬 FireCrawl 暴露的 Port
- `FIRECRAWL_API_KEY`: FireCrawl 金鑰(自部屬，若 DB 許可沒有啟動就不需要修改)

```
SEARXNG_HOST=http://192.168.200.102
SEARXNG_PORT=8080
FIRECRAWL_CLOUD=false
FIRECRAWL_HOST=http://192.168.200.102
FIRECRAWL_PORT=3002
FIRECRAWL_API_KEY=firecrawl_api_key
```