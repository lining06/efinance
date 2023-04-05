# 导入 efinance 库
import json
from myShares.mysql_connect import sharesCodeMysql as mysqlConnect

# stype（1：深圳、2：上海、3：北京）

with open('files/a_code.json', 'r') as f:
    json_object = json.load(f)
data_list = json_object['data']

for shares_object in data_list:
    name = shares_object['name']
    stype = shares_object['stype']
    code = shares_object['code']
    mysqlConnect.saveSharesCode(name, code, stype)


