# 导入 efinance 库

import efinance as ef
from myShares.mysql import sharesDayMysql as mysqlConnect

# 股票代码
stock_code = '600519'
# 开始日期
beg = '20000101'
# 结束日期
end = '20230313'
# 获取股票日 K 数据
rows = ef.stock.get_quote_history(stock_code, beg=beg, end=end)
for row in rows.values:
    mysqlConnect.saveSharesDay(row[0],
                               row[1],
                               row[2],
                               row[3],
                               row[4],
                               row[5],
                               row[6],
                               row[7],
                               row[8],
                               row[9],
                               row[10],
                               row[11],
                               row[12],
                               1)
