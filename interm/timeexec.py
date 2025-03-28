import time
import datetime

start_time = time.perf_counter()

for i in range(100000):
    pass

fruits = ["apple", "orange", "grape", "banana"]
print(fruits.sort())
for fruit in fruits:
    print(f"This is a {fruit}")
    
fruit_cal = {"apple" : 300, "orange" : 200, "grape" : 150, "banana" : 20}
fruit_cal = sorted(fruit_cal.items(), key=lambda item: item[1])
print(fruit_cal)
end_time = time.perf_counter()

elapsed_time = end_time - start_time 
print(elapsed_time)

date = datetime.date(2025, 1, 2)
today = datetime.date.today()
time = datetime.time(12, 30, 0)
now = datetime.datetime.now()
print(date)
print(today)
print(time)
print(now)

target_date = datetime.datetime(2030, 5, 6, 5, 3, 30)


if target_date > now:
    print("Active")
else: 
    print("Expired!")