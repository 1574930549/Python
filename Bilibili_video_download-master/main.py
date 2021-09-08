import BiliUtil
if __name__ == '__main__':
    cookie = input('请提供登录后的cookie信息，以升级下载画质:')
    # 创建频道对象
    ch = BiliUtil.Channel()
    # 设置频道参数
    ch.set_by_url('https://space.bilibili.com/4282930/channel/detail?cid=48758')
    # 传入cookie参数
    ch.set_cookie(cookie)
    # 开始批量下载视频
    ch.get_channel_data(base_path='Download', name_path=False, max_length=None)
