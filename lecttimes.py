#!/usr/bin/python3
import time
from datetime import *

lecture_time = datetime.strptime("19:15 27 march 2023","%H:%M %d %B %Y")
print(lecture_time)
delta1 = timedelta(days=3)
delta2 = timedelta(days=4)

for lecture in range(1,32):
    if lecture_time!= datetime.strptime("19:15 1 may 2023","%H:%M %d %B %Y"):
        if lecture%2==0:
            lecture_time+=delta2
            print("Lecture {0} :{1:>%Y-%m-%d %H:%M}".format(lecture,lecture_time))
        else:
            lecture_time+=delta1
            print("Lecture {0} :""{1:>%Y-%m-%d %H:%M}".format(lecture, lecture_time))
    else:
        lecture_time = datetime.strptime("19:15 4 may 2023","%H:%M %d %B %Y")
