import os
import sys

def TimeToSeconds(Times):
    RealTimes = 0
    times = Times.split(":")
    hh = times[0]; mm = times[1]; ss = times[2]
    RealTimes += int(ss)
    RealTimes += int(mm) * 60
    RealTimes += int(hh) * 60 * 60
    return RealTimes

def TtoSeconds(t):
    RealTime = 0
    t = t[:-1]
    if t.find('.') == -1:
        RealTime += int(t)
    else:
        times = t.split('.')
        second = times[0]; MicroSecond = times[1]
        RealTime += int(second)
        RealTime += (int(MicroSecond) * (10**(3 - len(MicroSecond))))/1000
    return RealTime

def ParsingJob(line, Jobs):
    # job-start, job-end, job-index: []
    infos = line.split(" ")
    complete_time = infos[1]; t = infos[2];
    Times, MicroSecond = complete_time.split('.')
    MicroSecond = int(MicroSecond) / 1000

    Real_CompleteTime = TimeToSeconds(Times) + MicroSecond
    Real_T = TtoSeconds(t)
    Real_StartTime = Real_CompleteTime - Real_T + 0.001

    Jobs.append((Real_CompleteTime, Real_StartTime))

def solution(lines):
    Jobs = []
    for line in lines:
        ParsingJob(line, Jobs)

    Max = 0
    Queries = [x[0] for x in Jobs] + [x[1] for x in Jobs]
    Queries.sort()
    Jobs.sort()
    # print("Queries: ", Queries)

    for Query in Queries:
        i = delete_count = count = 0;
        Start_point = Query; End_point = Query + 1
        while i < len(Jobs):
            if Start_point <= Jobs[i][0] < End_point:
                count += 1
            elif Start_point <= Jobs[i][1] < End_point:
                count += 1
            elif Jobs[i][1] < Start_point:
                delete_count += 1
            else:
                pass
            i += 1
        for iter_d in range(delete_count):
            Jobs.pop(0)
        Max = max(Max, count)
    return Max

if __name__ == '__main__':
    lines = []
    for lineIn in sys.stdin:
        line = lineIn.rstrip('\n')[1:-1]
        lines.append(line)
    result = solution(lines)
    print(result)
