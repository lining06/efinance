# 导入 efinance 库
import json
from myShares.mysql_connect import sharesCodeMysql as mysqlConnect
import efinance as ef
import wechat as wechat


# stype（0：指数、1：深圳、2：上海、3：北京 、10：板块）

# 同步股票代码（从文件）
def sync_shares_code():
    with open('files/a_code.json', 'r') as f:
        json_object = json.load(f)
    data_list = json_object['data']

    for shares_object in data_list:
        name = shares_object['name']
        stype = shares_object['stype']
        code = shares_object['code']
        mysqlConnect.saveSharesCode(name, code, stype)


# 同步板块代码（从数据库）
def sync_shares_bk():
    offset = 0
    limit = 100
    while True:
        shares_list = mysqlConnect.selectAll(offset, limit)
        if len(shares_list) <= 0:
            break

        for shares in shares_list:
            code = shares[1]
            shares_name = shares[0]
            try:
                # 查股票所属板块
                boards = get_board(code)
                if len(boards) <= 0:
                    break
                for board in boards.values:
                    board_code = board[2]
                    board_name = board[3]
                    mysqlConnect.saveSharesCode(board_name, board_code, 10)
            except Exception as e:
                wechat.send_message("股票：" + shares_name + "查询所属板块失败, code: " + code + "Exception:" + str(e))
        offset = offset + limit


# 查询股票所在板块
def get_board(stock_code):
    boards = ef.stock.get_belong_board(stock_code)
    print(boards)
    return boards


# sync_shares_bk()
