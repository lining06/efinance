import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="ln6@Asiain",
    database="lining"
)


def saveSharesCode(shares_name,
                   shares_code,
                   shares_type):
    values = select(shares_code, shares_name)
    if len(values) > 0:
        update(shares_name,
               shares_code,
               shares_type)
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
