import datetime

date1=datetime.datetime.now()
date2=date1-datetime.timedelta(days=1)

print((date1-date2).total_seconds())