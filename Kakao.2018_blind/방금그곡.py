import os
import sys

def timeToMinutes(time):
    hh, mm = time.split(":")
    return int(hh)*60 + int(mm)

def replaceTone(melody):
    melody = melody.replace('A#', 'K')
    melody = melody.replace('C#', 'H')
    melody = melody.replace('D#', 'I')
    melody = melody.replace('F#', 'J')
    melody = melody.replace('G#', 'M')
    return melody

def checkValid(time, m, melody):
    turns = time//len(melody); left = time% len(melody)
    song = melody*turns + melody[:left]
    return 0 if song.find(m) == -1 else 1

def parsing(musicinfo):
    t1, t2, title, melody = musicinfo.split(',')
    startTime = timeToMinutes(t1)
    endTime = timeToMinutes(t2)
    passTime = endTime - startTime
    return ((passTime, startTime, title), melody)

def solution(m, musicinfos):
    matched = []
    m = replaceTone(m)
    for musicinfo in musicinfos:
        info, melody = parsing(musicinfo)
        time = info[0]; melody = replaceTone(melody)
        if checkValid(time, m, melody): matched.append(info)

    print("mathced: ", matched)
    # x = (재생시간, 먼저 입력된 시간, 곡 이름)
    if matched:
        matched.sort(key = lambda x: (-x[0], x[1]))
        return matched[0][2]
    else:
        return '(None)'

if __name__ == '__main__':
    m = input()
    lines = input().split('","')
    musicinfos = []
    for line in lines:
        musicinfos.append(line[1:-1])

    print(solution(m, musicinfos))
