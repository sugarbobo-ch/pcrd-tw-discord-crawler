# PCRD-TW-webhook-crawler
> PCRD-TW-webhook-crawler 將從[超異域公主連結RE:DIVE 台灣官方網站](http://www.princessconnect.so-net.tw/news)進行爬蟲解析，抓取最新的公告並透過webhook發佈到Discord上

# 開始使用
## 環境需求
- Python 3.8.0+ (https://www.python.org/)
- 需要安裝在requirements.txt中額外的套件

## 安裝方式
若要執行PCRD-TW-webhook-crawler，需要安裝額外的套件，使用終端機至此專案的資料夾中下此指令：

```
pip install -r requirements.txt
```

## 設定
用任意的文字編輯器開啟 "pcrd_news.py"，在
```py
webhook_links = []
```
插入Discord的webhook連結，如下：
```py
webhook_links = [ 'https://discordapp.com/api/webhooks/.../...']
```
如果您有超過一個連結需要加入，請使用逗號分隔：
```py
webhook_links = [ 'https://discordapp.com/api/webhooks/.../...',
                  'https://discordapp.com/api/webhooks/.../...'
                ]
```
## 使用方式
使用終端機至專案資料夾執行此指令：
```
python pcrd_news.py
```
或
```
python3 pcrd_news.py
```

您也可以透過已經寫好的腳本來每天執行爬蟲

首先，在`pcrd_news_crawler.bat`中, 將　`YOUR_PROJECT_FOLDER_PATH` 文字用此專案資料夾的絕對路徑取代掉
```
cd /d YOUR_PROJECT_FOLDER_PATH
python pcrd_news.py
REM pause
```
接著，在`launch_bat.vbs`中，同樣把 `YOUR_PROJECT_FOLDER_PATH\pcrd_news_crawler.bat`的 `YOUR_PROJECT_FOLDER_PATH` 也取代掉

`\pcrd_news_crawler.bat`要留著

按下`開始 + R`, 輸入“taskschd.msc“ 開啟 **工作排程器**　或是Windows搜尋工作排程器

新增一個工作，在"觸發程序"中設定排程，公主連結的公告通常都在工作日的中午12點以及下午5點做更新，切記不要過於頻繁執行此程式

在"動作"的分頁，新增包含 launch_bat.vbs 的絕對路徑在程式或指令碼欄位內，按下確定即可

設定完後，只要電腦不關閉，此排程應會正常執行並推送通知到您設定的連結
