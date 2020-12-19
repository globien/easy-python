year = int(input("Year: "))
month = int(input("Month: "))
day = int(input("Day: "))

days = [31,28,31,30,31,30,31,31,30,31,30]  # 前11月的，12月的没用
for i in range(month-1):
    day = day + days[i]
if (year%400 == 0 or (year%4 == 0 and year%100 != 0)) and month > 2:
    day = day +1
print("它是第", day, "天")
