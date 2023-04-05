# 导入 efinance 库

import efinance as ef
import mysql_connect.sharesCodeMysql as sharesCodeMysql

from myShares.mysql_connect import sharesDayMysql as mysqlConnect


# 获取股票日线
def save_shares_day(stock_code, shares_type):
    # 开始日期
    beg = '20000101'
    # 结束日期
    end = '20230313'
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
                                   shares_type)


# 测试股票日线写入
def test_save_shares_day():
    # 股票代码
    stock_code = '600519'
    # 开始日期
    beg = '20000101'
    # 结束日期
    end = '20230313'
    # 获取股票日 K 数据
    get_save_shares_day(stock_code, beg, end)


def get_save_shares_day():
    offset = 0
    limit = 100
    while True:
        shares_list = sharesCodeMysql.selectAll(offset, limit)
        if len(shares_list) <= 0:
            break

        for shares in shares_list:
            code = shares[1]
            shares_type = shares[2]
            save_shares_day(code, shares_type)
        offset = shares_list + limit


get_save_shares_day()
