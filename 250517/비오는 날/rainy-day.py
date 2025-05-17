n = int(input())
date = []
day = []
weather = []

for _ in range(n):
    d, dy, w = input().split()
    date.append(d)
    day.append(dy)
    weather.append(w)

# Please write your code here.
class Weather:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather

    def print_info(self):
        print(f"{self.date} {self.day} {self.weather}")


data = []
for i in range(n):
    w = Weather(date[i], day[i], weather[i])
    data.append(w)


earliest_rain = None
for wea in data:
    if wea.weather == 'Rain':
        if earliest_rain is None or wea.date < earliest_rain.date:
            earliest_rain = wea

# 결과 출력
earliest_rain.print_info()