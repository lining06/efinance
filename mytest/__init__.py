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


data = {
            "msgtype": "text",
            "text": {
                "content": df,
                "mentioned_mobile_list": ["18516288649"]
            }
        }
r = requests.post(url='https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=80367921-d43c-4b87-bb6a-1628b9bb7e6f',
                  data=json.dumps(data))


print(df)