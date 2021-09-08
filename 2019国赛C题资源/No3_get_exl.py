#！/usr/bin/env python
# -*- coding：utf-8 -*-
# author: haotian time:2019/9/15
import pandas as pd
def getTable(base_url,start=-1,end=1):
    for idx in range(start,end+1):
        for page in range(1,51):
            now_url=base_url %(idx,page)
            print(now_url)
            tb=pd.read_html(now_url)[0]
            tb.to_csv(r'flight_info.csv',mode='a',encoding='utf_8_sig',header=1,index=0)
            print(str(idx)+'页抓取完成')

getTable('http://www.cdairport.com/flightInfor.aspx?t=4&attribute=A&time=%d&page=%d')
