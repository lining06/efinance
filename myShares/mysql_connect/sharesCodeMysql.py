import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="ln6@Asiain",
    autocommit=True,
    database="lining",
    pool_size=10  # 设置连接池的大小为10
)


def saveSharesCode(shares_name,
                   shares_code,
                   shares_type):
    values = select(shares_code, shares_name)
    if len(values) > 0:
        print("ignore shares_name:" + shares_name + " shares_code:" + shares_code)
        # update(shares_name,
        #        shares_code,
        #        shares_type)
    else:
        insertSharesDay(shares_name,
                        shares_code,
                        shares_type)


def insertSharesDay(shares_name,
                    shares_code,
                    shares_type):
    mycursor = mydb.cursor()
    sql = "INSERT INTO shares_code (" \
          "shares_name, shares_code, shares_type) " \
          "VALUES (%s, %s, %s)"
    val = (shares_name, shares_code, shares_type)
    mycursor.execute(sql, val)
    mydb.commit()
    print("insert success " + shares_name + " " + shares_code)


def update(shares_name,
           shares_code,
           shares_type):
    mycursor = mydb.cursor()
    sql = "UPDATE shares_code SET shares_name=%s where shares_code=%s and shares_type=%s"
    val = (shares_name, shares_code, shares_type)
    mycursor.execute(sql, val)
    mydb.commit()
    print("udpate success " + shares_name + " " + shares_code)


def select(shares_code, shares_name):
    mycursor = mydb.cursor()
    sql = "select shares_name, shares_code from shares_code where shares_code = %s and shares_name = %s"
    val = (shares_code, shares_name)
    mycursor.execute(sql, val)
    rows = mycursor.fetchall()
    for row in rows:
        print("select result: ")
        print(row)
    return rows


def selectAll(offset, limit):
    mycursor = mydb.cursor()
    sql = "select shares_name, shares_code, shares_type from shares_code order by id asc limit %s,%s "
    val = (offset, limit)
    mycursor.execute(sql, val)
    rows = mycursor.fetchall()
    for row in rows:
        print("select result: ")
        print(row)
    return rows


def selectCount(shares_type):
    mycursor = mydb.cursor()
    sql = "select count(1) from shares_code where shares_type = %s "
    val = (shares_type,)
    mycursor.execute(sql, val)
    count = mycursor.fetchall()
    return count[0]
