import datetime
import requests
import threading
import urllib.parse
from bs4 import BeautifulSoup
from discord_webhook import DiscordWebhook, DiscordEmbed

base_Url = 'http://www.princessconnect.so-net.tw'
current_title = None
timer_interval = 600
webhook_links = []

def remove_new_line_symbol(lines):
    removedLines = []
    for line in lines:
        removedLines.append(line.rstrip('\r\n'))
    return removedLines

def get_pcrd_news():
    global current_title
    global timer_interval
    
    # File Input
    f = open('pcrd_titles.txt','r+', encoding="utf-8")
    readTitles = f.readlines()
    writeTitles = readTitles

    # Crawler
    r = requests.get("http://www.princessconnect.so-net.tw/news")
    soup = BeautifulSoup(r.text, 'html.parser')
    divObjects = soup.find_all("dd")
    dtObjects = soup.find_all("dt")

    isUpdated = False
    count = 9
    for div in reversed(divObjects):
        title = div.findAll("a", recursive=False)[0]
        event_type = dtObjects[count].findAll("span", recursive=False)[0].get_text()

        # tag color
        tag_color = 16077457
        if event_type == '活動':
            tag_color = 3775462
        elif event_type == '系統':
            tag_color = 10512325

        current_title = title['title']
        find_news = False
        for line in readTitles:
            if current_title in line:
                find_news = True
                break

        if find_news == False:
            writeTitles.insert(0, current_title + '\n')
            current_link = title['href']
            r = requests.get(base_Url + current_link)
            soup = BeautifulSoup(r.text, 'html.parser')

            section = soup.select('body > main > article > article > section > p')
            content = ''
            for e in section:
                content += e.get_text('\n', '<br/>')
            content = content.replace('【', '\n**【')
            content = content.replace('】', '】**')
            content = (content[:1850] + ' ......') if len(content) > 1850 else content

            news_link = urllib.parse.urljoin(base_Url, current_link)

            embed = DiscordEmbed()
            embed.set_author(name='超異域公主連結☆Re：Dive', url='https://www.facebook.com/SonetPCR/',
                            icon_url='http://www.princessconnect.so-net.tw/images/pc-icon.png')
            embed.title = event_type + '：' + current_title
            embed.description = content
            embed.add_embed_field(name='官網連結', value=news_link)
            embed.color = tag_color
            
            for link in webhook_links:
                new_embed = embed
                webhook = DiscordWebhook(url=link)
                webhook.add_embed(new_embed)
                if "外掛停權" in current_title:
                    break
                webhook.execute()
                #print("已發布：" + current_title)
            # print(embed.title)
            # print(embed.description)
            print("已更新：" + current_title)
            isUpdated = True
        else:
            print("未更新：" + current_title)
        
        count -= 1
    
    while len(writeTitles) > 20:
        writeTitles.pop()

    if isUpdated:
        print("已儲存檔案")
        f.seek(0)
        f.truncate(0)
        f.writelines(writeTitles)
    f.close()
    # threading.Timer(timer_interval, get_pcrd_news).start()


if __name__ == '__main__':
    get_pcrd_news()
