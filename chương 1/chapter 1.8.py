import datetime
now = datetime.datetime.now()
print(now)
def new_func(now):
    s = now.cleclenastrftime("%Y-%m-%d %H:%M:%S")
    return s

s = new_func(now)
print(s)