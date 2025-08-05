# 🔍 MCP-WebSearch

[![Docker](https://img.shields.io/badge/Docker-Ready-blue?logo=docker)](https://www.docker.com/)
[![Python](https://img.shields.io/badge/Python-3.10+-green?logo=python)](https://www.python.org/)
[![MCP](https://img.shields.io/badge/MCP-Compatible-orange?logo=microsoft)](https://github.com/modelcontextprotocol/servers)
[![License](https://img.shields.io/badge/License-Apache2.0-yellow)](LICENSE)

> 為 AI Agent 提供強大的網頁搜尋 MCP 工具  
> 整合多種搜尋引擎，支援內容爬取與即時搜尋

## ✨ 特色功能

### 🌐 多重搜尋引擎整合
- **SearXNG**: 聚合多種搜尋引擎 (Google, Bing, Yahoo, DuckDuckGo...)
- **FireCrawl**: 強大的網頁內容爬取與搜尋功能

### 🚀 主要功能
- 📰 **網頁搜尋**: 快速搜尋網路資訊
- 📋 **新聞搜尋**: 獲取最新新聞資訊  
- 🔬 **學術搜尋**: 搜尋科學文獻與研究
- 📱 **社交媒體**: 搜尋社交平台內容
- 📄 **內容提取**: 將網頁內容轉換為 Markdown 格式

## 🚀 快速開始

### 1. 克隆專案
```bash
git clone https://github.com/TsukiSama9292/mcp_searxng.git
cd mcp_websearch
```

### 2. 配置環境變數
創建 `.env` 文件：
```bash
cp .env.example .env
```

### 3. 啟動服務
```bash
docker compose up -d
```

### 4. 驗證服務
```bash
curl http://localhost:8000/health
```

## ⚙️ 環境配置

### 必要環境變數

| 變數名稱 | 描述 | 預設值 | 範例 |
|---------|------|--------|------|
| `SEARXNG_HOST` | SearXNG 服務主機位址 | `http://localhost` | `http://192.168.1.100` |
| `SEARXNG_PORT` | SearXNG 服務端口 | `8080` | `8080` |
| `FIRECRAWL_CLOUD` | 是否使用 FireCrawl 雲端服務 | `false` | `true/false` |
| `FIRECRAWL_HOST` | FireCrawl 服務主機位址 | `http://localhost` | `http://192.168.1.100` |
| `FIRECRAWL_PORT` | FireCrawl 服務端口 | `3002` | `3002` |
| `FIRECRAWL_API_KEY` | FireCrawl API 金鑰 | `firecrawl_api_key` | `your_api_key_here` |

### 配置範例

```env
# SearXNG 配置
SEARXNG_HOST=http://192.168.200.102
SEARXNG_PORT=8080

# FireCrawl 配置
FIRECRAWL_CLOUD=false
FIRECRAWL_HOST=http://192.168.200.102
FIRECRAWL_PORT=3002
FIRECRAWL_API_KEY=your_firecrawl_api_key
```

## 🛠️ 本地開發

### 安裝依賴
```bash
# 使用 uv (推薦)
uv sync
```

### 運行開發服務器
```bash
python main.py
```

### 運行測試
```bash
pytest tests/
```

## 📖 API 使用

### 可用工具

#### 🌐 search_web
```python
# 網頁搜尋
search_web(query="Python 教學", num_results=5)
```

#### 📰 search_news  
```python
# 新聞搜尋
search_news(query="AI 最新發展", num_results=3)
```

#### 🔬 search_science
```python
# 學術搜尋
search_science(query="機器學習研究")
```

#### 📱 search_social
```python
# 社交媒體搜尋
search_social(query="開源專案討論")
```

#### 🔥 firecrawl_web
```python
# FireCrawl 搜尋
firecrawl_web(query="技術文檔", limit=5)
```

#### 📄 firecrawl_get_web_content
```python
# 獲取網頁內容
firecrawl_get_web_content(url="https://example.com")
```

## 🐳 Docker 部署

### 基本部署
```bash
docker compose up -d
```

### 自定義配置
```bash
# 修改 docker-compose.yml 中的環境變數
# 或使用 .env 文件
docker compose --env-file .env.production up -d
```

### 查看日誌
```bash
docker compose logs -f mcp_websearch
```

## 📁 專案結構

```
mcp_websearch/
├── 📁 src/
│   └── 📁 mcp_websearch/
│       ├── 📁 searxng/          # SearXNG 搜尋模組
│       ├── 📁 firecrawl/        # FireCrawl 搜尋模組
│       └── 📄 runner.py         # MCP 服務運行器
├── 📁 tests/                    # 測試文件
├── 📄 main.py                   # 主程式入口
├── 📄 docker-compose.yml        # Docker 配置
├── 📄 pyproject.toml           # Python 專案配置
└── 📄 README.md                # 專案說明
```


---

<div align="center">

**⭐ 如果這個專案對你有幫助，請給這個專案一個星星吧！**

Made with ❤️ by [TsukiSama9292](https://github.com/TsukiSama9292)

</div>