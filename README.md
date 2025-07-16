# YouTube VPS Detector

[![GitHub license](https://img.shields.io/github/license/yeyinghai/youtube-vps-detector)](https://github.com/yeyinghai/youtube-vps-detector/blob/main/LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/yeyinghai/youtube-vps-detector)](https://github.com/yeyinghai/youtube-vps-detector/stargazers)

一个简单的Python工具，用于检测YouTube上过去6天内发布的与“免费VPS”或“免费服务器”相关的视频，并将结果推送至自建Bark通知服务器。

## 功能
- 搜索关键词：`"免费VPS" OR "免费服务器"`。
- 时间范围：以运行时间为基准，往前6天。
- 结果：以列表形式推送（Markdown格式），包括标题、链接和发布时间。
- 如果无新视频，推送“无新视频”通知。
