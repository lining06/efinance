# 导入 efinance 库

import efinance as ef
import myShares.mysql_connect.sharesCodeMysql as sharesCodeMysql
import wechat as wechat

from myShares.mysql_connect import sharesDayMysql as mysqlConnect


# 获取股票日线
def save_shares_day(stock_code, shares_type, shares_name):
    # 开始日期
    beg = '20000101'
    # 结束日期
    end = '20230313'
    try:
        rows = ef.stock.get_quote_history(stock_code, beg=beg, end=end)
    except Exception as e:
        wechat.send_message("股票：" + shares_name + "查询详情失败, code: " + stock_code + "Exception:" + str(e))

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
    # wechat.send_message("股票：" + shares_name + "历史数据写入成功, code: " + stock_code)


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

# 同步所有股票数据
def get_save_shares_day():
    offset = 0
    limit = 100
    while True:
        shares_list = sharesCodeMysql.selectAll(offset, limit)
        if len(shares_list) <= 0:
            break

        for shares in shares_list:
            shares_name = shares[0]
            code = shares[1]
            shares_type = shares[2]
            save_shares_day(code, shares_type, shares_name)
        offset = offset + limit


get_save_shares_day()
