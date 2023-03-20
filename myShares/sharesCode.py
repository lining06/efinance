# 导入 efinance 库

from myShares.mysql import sharesCodeMysql as mysqlConnect

# 股票代码
stock_code = '600519'
# 股票代码
stock_name = '贵州茅台'
mysqlConnect.saveSharesCode(stock_name, stock_code, 1)
