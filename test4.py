from crontab import CronTab

cron = CronTab()
job = cron.new()
job.setall('1 * * * *')

print(cron)
print(job.minute)