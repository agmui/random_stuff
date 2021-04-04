#/usr/bin/env python3

from datetime import datetime


def calcutate(next_class_ampm, next_class_hour, next_class_minute):
    now = datetime.now()
    current_hour, current_min, current_sec, next_class_hour, next_class_minute = int(now.strftime("%H")), int(now.strftime("%M")), int(now.strftime("%S")), int(next_class_hour), int(next_class_minute)

    # now time given in military

    current = current_hour * 60 + current_min
    next_class = next_class_hour * 60 + next_class_minute

    if next_class_ampm == 2:  # convert both now and next time's to military
        current = current + 12 * 60

    # if ampm = 1 then it is AM and 2 for PM

    if current_sec == 0:
        diff = next_class - current
    else:
        diff = next_class - current - 1  # -1 due to seconds

    if diff < 0:
        if current_sec == 0:
            diff = (next_class + 24 * 60) - current
        else:
            diff = (next_class + 24 * 60) - current - 1
        if diff < 0:
            if current_sec == 0:
                diff = (next_class + 24 * 60 * 2) - current
            else:
                diff = (next_class + 24 * 60 * 2) - current - 1


    H = diff // 60
    M = diff % 60
    if current_sec != 0:
        current_sec = 60 - current_sec

    return H, M, current_sec
