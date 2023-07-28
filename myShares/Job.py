import schedule
import time
import sharesDay as sharesDay
import wechat as wechat


def job():
    # 在这里写你要执行的代码
    print("定时任务执行中...")
    try:
        sharesDay.sync_shares_day()
        wechat.send_message("今日定时任务执行成功")
    except Exception as e:
        try:
            wechat.send_message("今日定时任务执行失败" + str(e))
        except Exception as ex:
            print("微信发送失败")


# 每天的特定时间执行任务
schedule.every().day.at("15:30").do(job)
schedule.every().day.at("16:30").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
