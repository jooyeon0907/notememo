from crontab import CronTab

cron = CronTab(user='jooyeon')
job = cron.new(command='python3 test.py')
job.setall("* * * * *")
cron.write()
# job_standard_output = job.run()

 