import datetime
import pytz


dt = datetime.datetime(2020, 12, 1, 18, 27, 13, 5000, tzinfo=pytz.UTC)
# print(dt)

dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
# print(dt_utcnow)
dt_currz = dt_utcnow.astimezone(pytz.timezone("CST6CDT"))
# print(dt_currz)

# Naive dt now()
dt_test = datetime.datetime.now()
test_zone = pytz.timezone("America/Mexico_City")

print(dt_test)
dt_test = test_zone.localize(dt_test)
print(dt_test)
print(f"\n{dt_test.date()}")

dt_shift = dt_test.astimezone(pytz.timezone("America/Chihuahua"))
print(dt_shift)

date_str = "January 10, 1789 7:29"
dt = datetime.datetime.strptime(date_str, "%B %d, %Y %H:%M")
print(dt)

# for tz in pytz.all_timezones:
#     print(tz)


max_time = datetime.timedelta(hours=22)

check = datetime.datetime.now()

dt_left = max_time - datetime.timedelta(
    hours=check.hour,
    minutes=check.minute,
    seconds=check.second,
    microseconds=check.microsecond,
)
print(dt_left)

dt_zero = check - datetime.timedelta(
    hours=check.hour,
    minutes=check.minute,
    seconds=check.second,
    microseconds=check.microsecond,
)
print(check)
print(dt_zero)