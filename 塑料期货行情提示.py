#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import akshare as ak
from datetime import date
#import pandas as pd
import time
import os
#以塑料为例，获取代码、现价、手数及时间time_0节点
code = 'L2309' 
time_0 = time.asctime()
#获取当前时间点的期货价格
futures_zh_spot_df = ak.futures_zh_spot(symbol=code, market="CF", adjust='0')
#print(futures_zh_spot_df)
fp_0 = futures_zh_spot_df['current_price'].values.tolist()[0]
print('当前期货价格是', fp_0)


# In[ ]:


code = 'L2309' #大商所塑料代码
#code = 'PP2309' #大商所聚丙烯代码

hl = ['09:00', '11:30', '13:30', '15:00', '21:00', '23:00'] #聚乙烯、聚丙烯开盘收盘时间点

#播放音乐
def music():
    #当前文件的路径
    pwd = os.getcwd()  # 绝对路径
    print(pwd)
    pwd2=pwd+'\提示铃声.wav'
    os.system(pwd2)
    file=r"D:\提示铃声.wav"
    os.system(file)
    return

# 获得交易日期的start_date 和 end_date
def get_trade_date(N = 80):
    today = date.today()
    trade_date_df = ak.tool_trade_date_hist_sina() #获取所有交易日期
    trade_date_list = trade_date_df["trade_date"].astype(str).tolist()
    while str(today) not in trade_date_list:  # 如果当前日期不在交易日期列表内，则当前日期天数减一
        today = today - datetime.timedelta(days=1)

    end_date = str(today)[:4]+str(today)[5:7] + str(today)[8:10]

    start_date_index = trade_date_list.index(str(today))- N
    start_date = trade_date_list[start_date_index][:4] + trade_date_list[start_date_index][5:7] + trade_date_list[start_date_index][8:10]
    #print("结束时间",start_date)
    #print("开始时间",end_date)
    return trade_date_list[start_date_index:start_date_index+N+1]


#输入现价、手数
np_0 = int(input('请输入塑料现价：（eg:7680）'))
amount = input('请输入交易数量：（eg:300）')

time_0 = time.asctime()
#获取当前时间点的期货价格
futures_zh_spot_df = ak.futures_zh_spot(symbol=code, market="CF", adjust='0')
#print(futures_zh_spot_df)
fp_0 = futures_zh_spot_df['current_price'].values.tolist()[0]
print(fp_0)

check = 0
while check == 0:
    #获取当前时间
    time_now = time.localtime() #时间格式化
    day = time.strftime('%Y-%m-%d', time_now)
    last_day = get_trade_date(N = 0)[0]
    hour = time.strftime('%H:%M', time_now)
    #print(1) 
    #print(time.asctime())
    
    if day == last_day:
        #print(2)
        #print(time.asctime())
        
        if hl[0] <= hour <= hl[1] or hl[2] <= hour <= hl[3] or hl[4] <= hour <= hl[5]:
            #print(3)
            print(time.asctime()) #当前时间
            futures_zh_spot_df = ak.futures_zh_spot(symbol=code, market="CF", adjust='0')
            #print(futures_zh_spot_df)
            fp_1 = futures_zh_spot_df['current_price'].values.tolist()[0]
            #print(fp_1)
            
            #fin = run_main() #运行主函数
            #print(fin)

            if  fp_0 - fp_1 >= 30:
                print('满足触发条件')
                time_1 = time.asctime()  #输出期货满足条件的时间
                #print(time_1, fin[1])
                music()
                check = 1
                break
            else:
                time.sleep(15)
        else:
            time.sleep(1800)
    else:
        time.sleep(86400)
        
#输出
print('买入现货时间:', time_0, '买入期货价格:', fp_0, '买入现货价格:', np_0, '买入现货数量:', str(amount)+'吨')
print('条件触发时间:', time_1, '当前期货价格:', fp_1)




