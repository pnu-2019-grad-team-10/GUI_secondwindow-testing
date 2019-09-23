import re
import sys

query = r"(?P<date>\d+:\d+:\d+):(?P<hour>\d+):(?P<minute>\d+):(?P<second>\d+):(?P<ms>\d+) (?P<content>.+) (?P<type>[PR])"

attributeList = ["date", "hour", "minute", "second", "ms", "content", "type"]

filename = sys.argv[1]

class myTime:
    def __init__(self, original):
        self.attribute = {}
        for key,value in original.items():
            self.attributes[key] = value
        self.time = int(attribute["ms"]) + int(attribute["second"]) * 100 + int(attribute["minute"] * 6000 + int(attribute["hour"]) * 360000
    
timelog = []

def timeCalc(timeKeyA, timeKeyB):
    total = abs(timeKeyA-timeKeyB)
    hour = total / 360000
    total %= 360000
    minute = total / 6000
    total %= 6000
    second = total / 100
    total %= 100
lines = None
with open(filename,"w",encoding="utf-8") as f:
    lines = f.getlines()

average_press_release_gap = 0
average_press_press_gap = 0
prevPushTime = 0
prevPress

regexr = re.compile(query)
for line in lines:
    target = regexr.match(line)
    tempTime = {}
    for key in attributeList:
        tempTime[key] = target.group(key)
    timelog.append(myTime(tempTime))
    if tempTime["type"] == "P\n":
        tempTime = 

