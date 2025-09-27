import time

from datetime import datetime

# print(dir(time))
# print(time.time())
methods = [
    "altzone",
    "asctime",
    "ctime",
    "daylight",
    "get_clock_info",
    "gmtime",
    "localtime",
    "mktime",
    "monotonic",
    "monotonic_ns",
    "perf_counter",
    "perf_counter_ns",
    "process_time",
    "process_time_ns",
    "sleep",
    "strftime",
    "strptime",
    "struct_time",
    "thread_time",
    "thread_time_ns",
    "time",
    "time_ns",
    "timezone",
    "tzname",
]
print(time.altzone)

print(time.time())
print(time.ctime())
print(time.localtime())
# print(time.localtime(30))
# print(time.asctime(time.localtime(3000000000)))

# print(time.asctime((2022, 11, 4, 12, 30, 0, 0, 0, 0)))

# print(time.mktime((2022, 11, 4, 12, 30, 0, 0, 0, 0)))

# print(time.get_clock_info("time"))

# for x in range(5):
#     print(x)
#     time.sleep(1)

# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# log_file_name = "Log_" + time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime()) + ".txt"

# print(log_file_name)


print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print(datetime.now())
print(datetime.now().date())
print(datetime.now().time())
print(datetime.now().year)
print(datetime.now().month)
print(datetime.now().day)
print(datetime.now().hour)
print(datetime.now().minute)
print(datetime.now().second)
print(datetime.now().microsecond)
