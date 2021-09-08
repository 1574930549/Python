# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re
header = {  # 伪造浏览器头部，不然获取不到网易云音乐的页面源代码。
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
    'Referer': 'http://93.174.95.27',
}
# link = 'http://music.163.com/playlist?id=2884035'  # 网易原创歌曲榜
# link ='http://music.163.com/playlist?id=19723756' # 云音乐飙升榜
# link ='http://music.163.com/playlist?id=3778678'  # 云音乐热歌榜
# link ='http://music.163.com/playlist?id=3779629'    # 云音乐新歌榜
link = "https://music.163.com/discover/toplist?id=3778678"
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
# 限制数量为 100，即歌单的前 100 首歌
file = "music/"  # 保存音乐的文件路径,最后加斜杠
# i = 1
for s in songs:

    song_id = s['href'][9:]
    print(song_id)
    song_name = s.text
    wurl = "https://link.hhtjim.com/163/"  # 外链生成地址
    wang_url = "https://music.163.com/song?id=" + song_id
    song_url = wurl + song_id + ".mp3"
    # 获取歌曲16进制编码
    song = requests.get(song_url).content
    # 获取歌曲名称
    song_names = requests.get(wang_url).text
    song_name = re.findall('<em class="f-ff2">.*</em>', song_names)[0].lstrip('<em class="f-ff2">').rstrip('</em>')
    # 保存文件
    # with open(file + song_name + '.mp3', 'wb') as f:
    #     f.write(song)
    #     print(song_url + ' 歌名：' + song_name)
    # i = i + 1
