import datetime

today=datetime.datetime.now()

print ("Today: ", today)

print ("Yesterday: ", today-datetime.timedelta(days=1))

print ("Tomorrow: ", today+datetime.timedelta(days=1))