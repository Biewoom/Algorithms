import os
import sys
from heapq import heappush, heappop

def timeToSecond(time):
    hh, mm, ss = time.split(':')
    return float(hh)*3600 + float(mm)*60 + float(ss)

def completeTimeParsing(time):
    return float( time[:-1] )

def solution(lines):
    loadingTime = 0.001
    Max = 0
    hq = []; jobQ = []

    for line in lines:
        date, Endtime, completeTime = line.split(" ")
        Endtime = timeToSecond(Endtime)
        completeTime = completeTimeParsing(completeTime)
        jobQ.append( (Endtime-completeTime+loadingTime, Endtime) )

    jobQ.sort()
    timeZones = [x[0] for x in jobQ]

    for timeZone in timeZones:

        while jobQ and jobQ[0][0] <= timeZone:
            startTime, endtime = jobQ.pop(0)
            heappush(hq, endtime)

        while hq and hq[0] <= timeZone - 1:
            heappop(hq)

        Max = max(Max, len(hq))

    return Max

if __name__ == '__main__':
    lines = []
    for line in sys.stdin:
         line = line.rstrip()[1:-1]
         lines.append(line)

    result = solution(lines)
    print(result)
