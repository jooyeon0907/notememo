from crontab import CronTab
from common import *
import schedule
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler

config = load_config()
AUTO_BACKUP_SCHEDULE_POLICY = config['AUTO_BACKUP_SCHEDULE_POLICY']

cron = CronTab(user=True)
job = cron.new()
job.setall('2 06 2 1 5')
# cron.write()


# print(job.minutes)
# print(job.hours)
# print(job.day)
# print(job.months)
# print(job.dow)

print("--------------------")
'''
    minute(0-59)
    hour(0-23)
    day of month(1-31)
    month(1-12)
    day of week(0-6)
'''

def test():
    print("test")
    # time.sleep(1)

# sched = BlockingScheduler()
# sched.add_job(test, 'cron', second="*/1", minute="*", hour="*", month="*", day="*", week="*")
# sched.start()


def backup_schedule():
    schedule = BackgroundScheduler()
    schedule.start()
    schedule.add_job(test, 'cron', second="*/2", minute="*", hour="*", month="*", day="*", week="*")
    while True:
        pass

backup_schedule_thread = threading.Thread(target=backup_schedule, daemon= True)
backup_schedule_thread.start()

# cnt =0
while True:
    # cnt += 1
    # print(f"cnt : {cnt}")
    time.sleep(10)






# schedule.every(2).minutes.do(test)
# schedule.every(4).seconds.do(test)
# print(schedule.jobs)
# while True:
#     schedule.run_all()


