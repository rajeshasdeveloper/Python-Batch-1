lst = [1, 2, 3]
tup = (1, 2, 3)
set = {1, 2, 3}
dic = {"a": 1, 2: "b"}
r = range(10)
string = "good morning"

# Generators

import random


def random_numbers(count: int, length: int):
    d = 10 ** (length)
    res = [int(random.random() * d) for _ in range(count)]
    filtered_res = list(filter(lambda x: len(str(x)) == length, res))
    if len(filtered_res) != count:
        return random_numbers(count, length)
    return filtered_res


def gen(count, length):
    yield random_numbers(count, length)
    yield random_numbers(count + 1, length)
    yield random_numbers(count + 2, length)


# a = gen(3, 5)

# print(next(a))
# print(next(a))
# print(next(a))


import datetime, pytz, time

# print(time.time())

timez = pytz.timezone("America/Los_Angeles")

pst_time = datetime.datetime.now(timez)
# print(pst_time)
ist_time = datetime.datetime.now()
utc_time = datetime.datetime.utcnow()
# print(datetime.datetime.utcoffset(pst_time))

str_time = datetime.datetime.strftime(pst_time, "%Y-%m-%d %H:%M:%S")
# print(str_time, type(str_time))
parsed_time = datetime.datetime.strptime(str_time, "%Y-%m-%d %H:%M:%S")
# print(parsed_time, type(parsed_time))


# import os, platform

# # print(os.getcwd())
# # os.chdir('C:/Users/Rajesh/Documents/xortican/Python-Batch-1/session_5/source')

# print(os.getcwd())
# # print(os.listdir())
# os.environ["ABCD"] = "ABCD"
# os.getenv("ABCD")
# print(os.cpu_count())
# print(os.getlogin())
# print(os.getpid())
# # os.mkdir(os.getcwd()+'/sample')
# print(platform.uname())
