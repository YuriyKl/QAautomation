#!/usr/bin/python3
import time
from datetime import *

lecture_time = datetime.strptime("19:15 27 march 2023", "%H:%M %d %B %Y")
day_off = datetime.strptime("19:15 1 may 2023", "%H:%M %d %B %Y")
lecture_after_day_off = datetime.strptime("19:15 4 may 2023", "%H:%M %d %B %Y")

delta1 = timedelta(days=3)
delta2 = timedelta(days=4)

for lecture in range(1, 33):
    if lecture_time != day_off:
        if lecture % 2 == 0:
            print("Lecture {0:>2} :{1:>%Y-%m-%d %H:%M}".format(lecture, lecture_time))
            lecture_time += delta2
        else:
            print("Lecture {0:>2} :""{1:>%Y-%m-%d %H:%M}".format(lecture, lecture_time))
            lecture_time += delta1
    else:
        lecture_time = lecture_after_day_off
