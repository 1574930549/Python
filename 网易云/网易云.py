# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup

header = {  # 伪造浏览器头部，不然获取不到网易云音乐的页面源代码。
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
    'Referer': 'http://93.174.95.27',
}
# link = 'http://music.163.com/playlist?id=2884035'  # 网易原创歌曲榜
# link ='http://music.163.com/playlist?id=19723756' # 云音乐飙升榜
# link ='http://music.163.com/playlist?id=3778678'  # 云音乐热歌榜
# link ='http://music.163.com/playlist?id=3779629'    # 云音乐新歌榜
link = "https://music.163.com/album?id=1770439"
# print(link)
# 这是网易云音乐歌单的链接,注意删除链接中的'#'
# （其实是嵌套在网页里面含有歌曲数据的页面框架的真实链接）
r = requests.get(link, headers=header)
html = r.content
# print(html)
soup = BeautifulSoup(html, "html.parser")
songs = soup.find("ul", class_="f-hide").select("a", limit=100)
# 通过分析网页源代码发现排行榜中的歌曲信息全部放在类名称为 f-hide 的 ul 中
# 于是根据特殊的类名称查找相应 ul，然后找到里面的全部 a 标签
# 限制数量为 10，即歌单的前 10 首歌

i = 1
for s in songs:
    song_id = s['href'][9:]
    song_name = s.text
    song_down_link = "http://music.163.com/song/media/outer/url?id=" + song_id + ".mp3"
    print("第 " + str(i) + " 首歌曲：" + song_name)
    print("正在下载...")

    response = requests.get(song_down_link, headers=header).content
    f = open('music\\'+song_name + ".mp3", 'wb')
    # music\\  路径
    f.write(response)
    f.close()
    print("下载完成！\n\r")
    i = i + 1
