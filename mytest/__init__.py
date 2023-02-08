# 导入 efinance 库
import json

import efinance as ef
import requests

import jsonpath

# 股票代码
stock_code = '600519'
# 开始日期
beg = '20210101'
# 结束日期
end = '20210708'
# 获取股票日 K 数据
df = ef.stock.get_quote_history(stock_code, beg=beg, end=end)

print(df)
