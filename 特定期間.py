import twstock as t
import pandas as p
import plotly.express as e

#最近一個月資料
stock=t.Stock("0056")
period=stock.fetch_31()
data=p.DataFrame(period)
data.columns=["日期", "成交股數" , "成交量", "開盤價", "最高價", "最低價", "收盤價", "漲跌價差", "成交筆數"]
data

#特定時間資料
period=stock.fetch(2023, 6)
data=p.DataFrame(period)
data.columns=["日期", "成交股數" , "成交量", "開盤價", "最高價", "最低價", "收盤價", "漲跌價差", "成交筆數"]
data

#特定時間到今日資料
period=stock.fetch_from(2023, 6)
data=p.DataFrame(period)
data.columns=["日期", "成交股數" , "成交量", "開盤價", "最高價", "最低價", "收盤價", "漲跌價差", "成交筆數"]

result=e.line(data, x="日期", y="收盤價", title="0056 元大寶來收盤價")
result.show()

result=e.bar(data, x="日期", y="成交量", title="0056 元大寶來成交量")
result.show()