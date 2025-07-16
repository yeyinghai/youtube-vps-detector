# YouTube VPS Detector

[![GitHub license](https://img.shields.io/github/license/yeyinghai/youtube-vps-detector)](https://github.com/yeyinghai/youtube-vps-detector/blob/main/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/yeyinghai/youtube-vps-detector)](https://github.com/yeyinghai/youtube-vps-detector/stargazers)

一个简单的Python工具，用于检测YouTube上过去6天内发布的与“免费VPS”或“免费服务器”相关的视频，并将结果推送至自建Bark通知服务器。

## 功能
- 搜索关键词：`"免费VPS" OR "免费服务器"`。
- 时间范围：以运行时间为基准，往前6天。
- 结果：以列表形式推送（Markdown格式），包括标题、链接和发布时间。
- 如果无新视频，推送“无新视频”通知。
## 安装
1. 克隆仓库：
git clone https://github.com/yeyinghai/youtube-vps-detector.git cd youtube-vps-detector
2. 安装依赖（Python 3.8+）：
   pip install -r requirements.txt
3. 配置：创建config.json，并填写您的值（详见下文）。
  ## 配置 (config.json)
  ```json
  {
   "youtube_api_key": "YOUR_YOUTUBE_API_KEY_HERE",
   "bark_server_url": "https://your-bark-server.com/push",
   "bark_key": "YOUR_BARK_KEY_HERE",  // 可选，如果Bark需要密钥
   "max_results": 10  // 最大返回视频数量
  }
```
## 注意事项
YouTube API Key：从Google Cloud Console获取，启用YouTube Data API v3。

Bark服务器：您的自建Bark URL。
## 用法
运行脚本：
python youtube_vps_detector.py

它会自动搜索并推送通知。

自动化：使用cron（例如，每天运行）：0 9 * * * /usr/bin/python3 /path/to/youtube_vps_detector.py。

示例通知
标题: YouTube VPS检测 - 新视频
内容:
检测到过去6天内的免费VPS/服务器视频：

- **标题**: 2025最新免费VPS教程 (链接: https://www.youtube.com/watch?v=abc123)
  发布时间: 2025-07-15T12:00:00

# 使用GitHub Actions运行
自动化：可以设置定时任务（e.g., 每天运行一次），无需手动执行。

免费：GitHub提供免费的Actions分钟（public仓库无限，private有限）。

集成：无缝集成到您的GitHub仓库中。

安全：使用GitHub Secrets存储敏感信息（如API密钥），避免泄露。

示例：这个workflow会每天UTC时间9:00运行脚本（可调整）。 

##设置GitHub Secrets：

去您的GitHub仓库页面：Settings > Secrets and variables > Actions > New repository secret。

添加以下Secrets（这些值来自您的config.json，但不要上传真实config.json）：

YOUTUBE_API_KEY：您的YouTube API密钥。

BARK_SERVER_URL：您的Bark服务器URL（e.g., https://your-bark-server.com/push）。

BARK_KEY：您的Bark密钥（如果需要，否则留空）。

MAX_RESULTS：最大结果数量（e.g., 10，可选，如果想动态调整）。

Workflow文件：`.github/workflows/auto-detect.yml` 已配置为每天UTC 9:00自动运行。您可以调整cron表达式（详见YAML文件）

欢迎PR！请fork仓库，创建分支，提交更改。
