# 导入 efinance 库

import efinance as ef
import myShares.mysql_connect.sharesCodeMysql as sharesCodeMysql
import wechat as wechat

from myShares.mysql_connect import sharesDayMysql as mysqlConnect
from myShares.mysql_connect import sharesCodeMysql as mysqlCodeConnect


# 获取股票日线
def save_shares_day(stock_code, shares_type, shares_name):
    # 开始日期
    beg = '20230629'
    # 结束日期
    end = '20230704'
    try:
        rows = ef.stock.get_quote_history(stock_code, beg=beg, end=end)
    except Exception as e:
        wechat.send_message("股票：" + shares_name + "查询详情失败, code: " + stock_code + "Exception:" + str(e))
        return 0

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
    return len(rows.values)


# 同步所有股票数据
def sync_shares_day():
    offset = 0
    limit = 100
    count = 0
    while True:
        shares_list = sharesCodeMysql.selectAll(offset, limit)
        if len(shares_list) <= 0:
            break
        for shares in shares_list:
            shares_name = shares[0]
            code = shares[1]
            shares_type = shares[2]
            size = save_shares_day(code, shares_type, shares_name)
            count = count + size
        offset = offset + limit
    wechat.send_message("本次成功同步股票：" + str(offset) + "个,数据：" + str(count) + "条")


# 获取单只股票日线
def getShareInfoSingle():
    # 开始日期
    beg = '20230511'
    # 结束日期
    end = '20230524'
    stock_code = 'BK0456'

    rows = ef.stock.get_quote_history(stock_code, beg=beg, end=end)
    print(rows)


# 发汇总消息
def statistic_base_info():
    wechat.send_message("股票代码数据汇总。指数共：" + str(mysqlCodeConnect.selectCount(0))
                        + "支，深圳共: " + str(mysqlCodeConnect.selectCount(1))
                        + "支，上海共: " + str(mysqlCodeConnect.selectCount(2))
                        + "支，北京共: " + str(mysqlCodeConnect.selectCount(3))
                        + "支，板块代码共: " + str(mysqlCodeConnect.selectCount(10)))

    wechat.send_message("股票日数据汇总。指数共：" + str(mysqlConnect.selectCount(0))
                        + "条，深圳共: " + str(mysqlConnect.selectCount(1))
                        + "条，上海共: " + str(mysqlConnect.selectCount(2))
                        + "条，北京共: " + str(mysqlConnect.selectCount(3))
                        + "条，板块代码共: " + str(mysqlConnect.selectCount(10)))

sync_shares_day()

# getShareInfoSingle()

# get_board()

# statistic_base_info()