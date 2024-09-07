day, hour, minute = map(int, input().split())
if day < 11 and hour < 11 and minute < 11:
    print(-1)
    exit(1)
else:
    dayGap = day - 11
    hourGap = hour - 11
    minuteGap = minute - 11
    print((dayGap * 24 * 60) + (hourGap * 60) + minuteGap)