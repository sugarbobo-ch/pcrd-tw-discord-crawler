# PCRD-TW-webhook-crawler
> PCRD-TW-webhook-crawler 將從[超異域公主連結RE:DIVE 台灣官方網站](http://www.princessconnect.so-net.tw/news)進行爬蟲解析，抓取最新的公告並透過webhook發佈到Discord上

> A crawler for mobile game "Princess Connect Re:Dive" announcements in Taiwan server, which can post the latest annoucement in discord embed block to discord channels via webhook.

# README.md
- [繁體中文 (zh_TW)](https://github.com/jinan-tw/pcrd-tw-discord-crawler/blob/main/README_zh-TW.md)

# Getting Started
## Requirements
- Python 3.8.0+ (https://www.python.org/)
- Additional library listed in requirements.txt

## Installation
To run PCRD-TW-webhook-crawler, you need to install the packages in requirements.txt

```
pip install -r requirements.txt
```

## Configuration
Open the file "pcrd_news.py", in 
```py
webhook_links = []
```
Insert your discord webhook link in string, like:
```py
webhook_links = [ 'https://discordapp.com/api/webhooks/.../...']
```
If you have more than one link, use comma to separate them
```py
webhook_links = [ 'https://discordapp.com/api/webhooks/.../...',
                  'https://discordapp.com/api/webhooks/.../...'
                ]
```
## Usage
PCRD-TW-webhook-crawler can run with command:
```
python pcrd_news.py
```
or
```
python3 pcrd_news.py
```

You can also use the VBScript in this project to setup daily scheule in Windows.
First, in pcrd_news_crawler.bat, replace `YOUR_PROJECT_FOLDER_PATH` with your abosulte path of project folder
```
cd /d YOUR_PROJECT_FOLDER_PATH
python pcrd_news.py
REM pause
```
Second, in launch_bat.vbs, do the same action to `YOUR_PROJECT_FOLDER_PATH`
Third, Press `Windows + R`, and type “taskschd.msc“ to open **Task Scheduler**.
In **Triggers** tab, set when the task will start, the news usually updated at 12:00 and 17:00 (UTC+08:00) during the week.
In **Actions** tab, create a new action, start a program with your `launch_bat.vbs` path.

Done, keep the machine power on, wait the webhook notification.
