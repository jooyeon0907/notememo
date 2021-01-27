from crontab import CronTab

cron = CronTab(user='jooyeon')
job = cron.new(command='echo hello_world')
job.minute.every(1)
cron.write()

job_standard_output = job.run()