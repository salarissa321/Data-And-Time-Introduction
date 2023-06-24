


#---------------------------------------------------
#----- Data And Time => Introduction--------------
#-----------------------------------------------------

import datetime

# print(dir(datetime)) # ['MAXYEAR', 'MINYEAR', 'UTC', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'date', 'datetime', 'datetime_CAPI', 'sys', 'time', 'timedelta', 'timezone', 'tzinfo']
# print(dir(datetime.datetime)) # ['__add__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__radd__', '__reduce__', '__reduce_ex__', '__repr__', '__rsub__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', 'astimezone', 'combine', 'ctime', 'date', 'day', 'dst', 'fold', 'fromisocalendar', 'fromisoformat', 'fromordinal', 'fromtimestamp', 'hour', 'isocalendar', 'isoformat', 'isoweekday', 'max', 'microsecond', 'min', 'minute', 'month', 'now', 'replace', 'resolution', 'second', 'strftime', 'strptime', 'time', 'timestamp', 'timetuple', 'timetz', 'today', 'toordinal', 'tzinfo', 'tzname', 'utcfromtimestamp', 'utcnow', 'utcoffset', 'utctimetuple', 'weekday', 'year']


# Print The Current Date and Time 

print(datetime.datetime.now()) # 2023-05-20 15:28:52.273052

# print("#" * 50) # ##################################################




# Print The Year

print(datetime.datetime.now().year) # 2023

print("#" * 50) # ##################################################


# Print The month

print(datetime.datetime.now().month) # 5

print("#" * 50) # ##################################################

# Print The Day

print(datetime.datetime.now().day) # 20


print("#" * 50) # ##################################################


# Print Start and End of Date

print(datetime.datetime.min) # 0001-01-01 00:00:00
print(datetime.datetime.max) # 9999-12-31 23:59:59.999999


print("#" * 50) # ##################################################


# Print The Current Time 

print(datetime.datetime.now().time()) # 15:37:33.616500

# print(dir(datetime.datetime.now())) # ['__add__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__radd__', '__reduce__', '__reduce_ex__', '__repr__', '__rsub__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', 'astimezone', 'combine', 'ctime', 'date', 'day', 'dst', 'fold', 'fromisocalendar', 'fromisoformat', 'fromordinal', 'fromtimestamp', 'hour', 'isocalendar', 'isoformat', 'isoweekday', 'max', 'microsecond', 'min', 'minute', 'month', 'now', 'replace', 'resolution', 'second', 'strftime', 'strptime', 'time', 'timestamp', 'timetuple', 'timetz', 'today', 'toordinal', 'tzinfo', 'tzname', 'utcfromtimestamp', 'utcnow', 'utcoffset', 'utctimetuple', 'weekday', 'year']





print("#" * 50) # ##################################################

# Print The Current Time Hour
print(datetime.datetime.now().time().hour) # 15

# Print The Current Time Minute
print(datetime.datetime.now().time().minute) # 41

# Print The Current Time Second
print(datetime.datetime.now().time().second) # 0

print("#" * 50) # ##################################################



#  Print Start and End of Time

print(datetime.time.min) # 00:00:00
print(datetime.time.max) # 23:59:59.9999

print("#" * 50) # ##################################################

# Printspecific Date

print(datetime.datetime(1995, 7 , 25)) # 1995-07-25 00:00:00
print(datetime.datetime(1995, 7 , 25 , 10 ,25 ,55 , 159826)) # 1995-07-25 10:25:55.159826

print("#" * 50) # ##################################################

myBirthDay = datetime.datetime(1995, 7 , 25)
dateNow = datetime.datetime.now()

print(f"my Birthday is {myBirthDay} And " , end ="")  # my Birthday is 1995-07-25 00:00:00 And Date Now  is 2023-05-20 15:52:15.815134
print(f"Date Now  is {dateNow} ") 

print(f"I Lived for {dateNow - myBirthDay}") # I Lived for 10161 days, 15:55:12.958200
print(f"I Lived for {(dateNow - myBirthDay).days} Days") # I Lived for 10161 Days