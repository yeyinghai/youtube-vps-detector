import datetime
import json
import os
import requests
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# 加载配置
CONFIG_FILE = "config.json"
if not os.path.exists(CONFIG_FILE):
    raise FileNotFoundError("config.json 未找到。请复制 config.json.example 并配置。")

with open(CONFIG_FILE, "r") as f:
    config = json.load(f)

YOUTUBE_API_KEY = config["youtube_api_key"]
BARK_SERVER_URL = config["bark_server_url"]
BARK_KEY = config.get("bark_key", "")  # 可选
MAX_RESULTS = config.get("max_results", 10)

def search_youtube_videos():
    # 计算时间范围：当前时间往前6天
    now = datetime.datetime.utcnow()
    past_date = now - datetime.timedelta(days=6)
    published_after = past_date.isoformat("T") + "Z"  # ISO 8601格式

    # 构建YouTube API客户端
    youtube = build("youtube", "v3", developerKey=YOUTUBE_API_KEY)

    # 搜索请求
    try:
        search_response = youtube.search().list(
            q='"免费VPS" OR "免费服务器"',  # 查询关键词（支持OR）
            type="video",  # 只搜索视频
            part="id,snippet",
            publishedAfter=published_after,
            maxResults=MAX_RESULTS,
            order="relevance"  # 按相关性排序（可改为"date"按时间排序）
        ).execute()

        videos = []
        for item in search_response.get("items", []):
            video_id = item["id"]["videoId"]
            title = item["snippet"]["title"]
            published_at = item["snippet"]["publishedAt"]
            link = f"https://www.youtube.com/watch?v={video_id}"
            videos.append({
                "title": title,
                "link": link,
                "published_at": published_at
            })

        return videos

    except HttpError as e:
        print(f"API错误: {e}")
        return []

def send_bark_notification(videos):
    if not videos:
        title = "YouTube VPS检测"
        body = "过去6天内无新的免费VPS/服务器视频。"
    else:
        title = "YouTube VPS检测 - 新视频"
        body = "检测到过去6天内的免费VPS/服务器视频：\n\n"
        for video in videos:
            body += f"- **标题**: {video['title']} (链接: {video['link']})\n"
            body += f"  发布时间: {video['published_at']}\n\n"

    # Bark推送参数
    payload = {
        "title": title,
        "body": body,
        "group": "VPS检测",  # 可自定义分组
        "icon": "https://img.icons8.com/color/48/000000/youtube.png",  # 可选图标
        "sound": "minuet.caf"  # 可选声音（Bark支持）
    }
    if BARK_KEY:
        payload["key"] = BARK_KEY

    # 发送POST请求
    response = requests.post(BARK_SERVER_URL, json=payload)
    if response.status_code == 200:
        print("Bark通知发送成功！")
    else:
        print(f"Bark通知失败: {response.status_code} - {response.text}")

if __name__ == "__main__":
    videos = search_youtube_videos()
    send_bark_notification(videos)
