import os
import sys

from collections import defaultdict

def TimeToInt(Time):
    result = 0
    hh, mm = Time.split(":")
    result += int(hh)*60
    result += int(mm)
    return result

def IntToTime(num):
    result = 0
    hh = str(num//60).zfill(2)
    mm = str(num % 60).zfill(2)
    result = hh + ":" + mm
    return result

def CheckMyTime(lastBus, Queue, Crews, capacity):
    while Crews and Crews[0] <= lastBus:
        Queue.append(Crews.pop(0))

    if len(Queue) < capacity:
        return lastBus
    else:
        TimeMap = defaultdict(int)
        for time in Queue: TimeMap[time] += 1

        TimeCandidates = sorted(TimeMap.keys())

        count = i = 0
        while count + TimeMap[ TimeCandidates[i] ] < capacity:
            count += TimeMap[ TimeCandidates[i] ]
            i += 1
        MyTime = TimeCandidates[i] - 1
        return MyTime

def solution(n, t, m, timetable):
    Bus_Start = TimeToInt("09:00")
    BusTable = [Bus for Bus in range(Bus_Start, Bus_Start + (t*n), t) ]
    Crews = [TimeToInt(time) for time in timetable]
    Queue = []
    Crews.sort()

    for Bus in BusTable[:-1]:

        while Crews and Crews[0] <= Bus:
            Queue.append(Crews.pop(0))

        count = 0
        while Queue and count < m:
            Queue.pop(0)
            count += 1

    lastBus = BusTable[-1]
    MyTime = CheckMyTime(lastBus, Queue, Crews, m)
    answer = IntToTime(MyTime)
    return answer


if __name__ == '__main__':
    timetable = []
    n = int(input())
    t = int(input())
    m = int(input())
    lines = input().split(',')
    for line in lines:
        timetable.append(line[1:-1])
    result = solution(n, t, m, timetable)
    print(result)
