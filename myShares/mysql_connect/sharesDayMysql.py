import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="ln6@Asiain",
    database="lining"
)


def saveSharesDay(shares_name,
                  shares_code,
                  date,
                  begin_price,
                  end_price,
                  max_price,
                  min_price,
                  deal_count,
                  deal_money,
                  range_percent,
                  change_price_percent,
                  change_price,
                  change_count_percent,
                  shares_type):
    values = select(shares_code, date, shares_type)
    if len(values) > 0:
        print("ignore shares_name:" + shares_name + " shares_code:" + shares_code + " date:" + date)
        return
        # update(shares_name,
        #        shares_code,
        #        date,
        #        begin_price,
        #        end_price,
        #        max_price,
        #        min_price,
        #        deal_count,
        #        deal_money,
        #        range_percent,
        #        change_price_percent,
        #        change_price,
        #        change_count_percent,
        #        shares_type)
    else:
        insertSharesDay(shares_name,
                        shares_code,
                        date,
                        begin_price,
                        end_price,
                        max_price,
                        min_price,
                        deal_count,
                        deal_money,
                        range_percent,
                        change_price_percent,
                        change_price,
                        change_count_percent,
                        shares_type)


def insertSharesDay(shares_name,
                    shares_code,
                    date,
                    begin_price,
                    end_price,
                    max_price,
                    min_price,
                    deal_count,
                    deal_money,
                    range_percent,
                    change_price_percent,
                    change_price,
                    change_count_percent,
                    shares_type):
    mycursor = mydb.cursor()
    sql = "INSERT INTO shares_day (" \
          "shares_name, shares_code, date, begin_price, end_price, max_price, " \
          "min_price, deal_count, deal_money, range_percent, change_price_percent," \
          " change_price, change_count_percent, shares_type) " \
          "VALUES (%s, %s, %s, %s, %s, %s, %s," \
          " %s, %s, %s, %s, %s, %s, %s)"
    val = (shares_name, shares_code, date, begin_price, end_price, max_price, min_price,
           deal_count, deal_money, range_percent, change_price_percent, change_price, change_count_percent, shares_type)
    mycursor.execute(sql, val)
    mydb.commit()
    print("insert success " + shares_name + " " + shares_code + " " + date)


def update(shares_name,
           shares_code,
           date,
           begin_price,
           end_price,
           max_price,
           min_price,
           deal_count,
           deal_money,
           range_percent,
           change_price_percent,
           change_price,
           change_count_percent,
           shares_type):
    mycursor = mydb.cursor()
    sql = "UPDATE shares_day SET shares_name=%s,shares_code=%s,date=%s,begin_price=%s,end_price=%s," \
          "max_price=%s,min_price=%s,deal_count=%s,deal_money=%s,range_percent=%s,change_price_percent=%s," \
          "change_price=%s,change_count_percent=%s where shares_code=%s and date=%s and shares_type=%s"
    val = (shares_name, shares_code, date, begin_price, end_price, max_price, min_price,
           deal_count, deal_money, range_percent, change_price_percent, change_price,
           change_count_percent, shares_code, date, shares_type)
    mycursor.execute(sql, val)
    mydb.commit()
    print("udpate success " + shares_name + " " + shares_code + " " + date)


def select(shares_code, date, shares_type):
    mycursor = mydb.cursor()
    sql = "select shares_name, shares_code, date, begin_price, end_price, max_price, " \
          "min_price, deal_count, deal_money, range_percent, change_price_percent," \
          " change_price, change_count_percent, shares_type from shares_day " \
          "where shares_code = %s and date = %s and shares_type = %s"
    val = (shares_code, date, shares_type)
    mycursor.execute(sql, val)
    rows = mycursor.fetchall()
    return rows


def select_by_shares_code(shares_code):
    mycursor = mydb.cursor()
    sql = "select shares_name, shares_code, date, begin_price, end_price, max_price, " \
          "min_price, deal_count, deal_money, range_percent, change_price_percent," \
          " change_price, change_count_percent, shares_type from shares_day " \
          "where shares_code = %s"
    val = [shares_code]
    mycursor.execute(sql, val)
    rows = mycursor.fetchall()
    return rows
