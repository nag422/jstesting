import numpy as np
import time
import sys
a = np.array([1,2,3])
print(a[2])

l =  range(1000)
print(sys.getsizeof(5) * len(l))
array = np.arange(1000)
print(array.size*array.itemsize)

import datetime
current_date = datetime.date.today()
print((current_date))
# .timetuple()
# create datetime
personal_date = datetime.date(2022, 12,30)
# print(dir(personal_date))

timestamp = datetime.date.fromtimestamp(1326244364)
print(timestamp)

timevalue = datetime.time() # default all are 0
print(timevalue)

b = datetime.time(11, 34, 56)
print(b)

dt_time_value = datetime.datetime(2022, 12, 28, 23, 55, 59, 342380)
print(dt_time_value)

#  using date()

t1 = datetime.date(year = 2018, month = 7, day = 12)
print(t1)

t2 = datetime.date(year = 2017, month = 12, day = 23) # mostly 3 args.

print(t2)

t3 = t1 - t2
print(t3)

t4 = datetime.datetime(2018, 7, 12,7, 9, 33)
print(t4)

t1 = datetime.timedelta(weeks = 2, days = 5, hours = 1, seconds = 33)
t2 = datetime.timedelta(weeks = 4, days = 11, hours = 4, seconds = 54)

t3 = t1 - t2
print(t3)

t = datetime.timedelta(days = 5, hours = 1, seconds = 33, microseconds = 233423)
print("Total seconds =", t.total_seconds())

# current date and time
now = datetime.datetime.now()
print("Time:", t)

t = now.strftime("%m/%d/%Y, %H:%M:%S")
print(t)

date_string = "25 December, 2022"
#use strptime() to create date object
date_object = datetime.datetime.strptime(date_string, "%d %B, %Y")
print("date_string=", date_object)

import pytz

local = datetime.datetime.now()

print("Local", local.strftime("%m/%d/%Y, %H:%M:%S"))

tz_NY = pytz.timezone("America/New_York")
datetime_NY = datetime.datetime.now(tz_NY)
print(datetime_NY.strftime("%m/%d/%Y, %H:%M:%S"))

import time
size = 100
l1 = range(size)
l2 = range(size)

a1 = np.arange(size)
a2 = np.arange(size)

start = time.time()
result = [(x+y) for x,y in zip(l1,l2)]

print("python list took ", (time.time() - start) * 1000)

# numpy array

start = time.time()
result = a1 + a2

print("numpy took ", (time.time() - start) * 1000 )

a1 = np.array([1,2,3])
a2 = np.array([4,5,6])
print(a1*2)
print(a1*a2)

# dimensions

a = np.array([5,6,9])
print(a[::2])
print(a.ndim)

b = np.array([[1,2], [3,4], [5,6]])

print(b.ndim)
print(b.itemsize)

print(b.dtype)

a = np.array([[1,3], [4,6], [5,8]], dtype=np.float64)
print(a.dtype)

print(a.itemsize) # according space of occupy 8

print(a.size) # How many elements

print(a)

print(a.shape)

a = np.array([[1,2], [3,4], [5,6]], dtype=complex)
print(a)

z = np.zeros( (3,4) )
print(z)

z = np.ones( (3,4) )
print(z)

l =  range(5)
print(l) #create array object with shape
arnp = np.arange(1,5)
print(arnp.ravel());

s = arnp.min()
print(s)

k = arnp.max()
print(k)

a = arnp.sum()
print(a)

a = np.array([[2,3,5], [1,2,3], [9,3,2]])
print(a)

print(a[0,2])

