import datetime

#time difference
t = datetime.timedelta(days=1000)
# dates
b = datetime.date(2006,5,22)

#the calculation of the dates
print('future day :',(t + b).strftime("%d:%m:%y"))