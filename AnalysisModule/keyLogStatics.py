import re
import sys

query = r"(?P<date>\d+:\d+:\d+):(?P<hour>\d+):(?P<minute>\d+):(?P<second>\d+):(?P<ms>\d+) (?P<content>.+) (?P<type>[PR])"

ATTRIBUTES = ["date", "hour", "minute", "second", "ms", "content", "type"]

def timeCalc(timeKey):
    total = timeKey
    hour = 0
    minute = 0
    second = 0
    if total > 3600000:
        hour = total / 3600000
        total %= 3600000
    if total > 60000:
        minute = total / 60000
        total %= 60000
    if total > 1000:
        second = total / 1000
        total %= 1000
    return (hour,minute,second,total)
    
def patToTime(timeDict):
    result = 0
    result += int(timeDict["hour"])*3600000 + int(timeDict["minute"]) * 60000 + int(timeDict["second"]) * 1000 + int(timeDict["ms"])
    return result

def acquireData(filename):
    lines = None
    with open(filename,"r",encoding="utf-8") as f:
        lines = f.readlines()
    avePressToPressTime = 0
    avePressToReleaseTime = 0
    countBackspace = 0
    lineq = re.compile(query)
    prevKeyPressTime = -1
    actionCount = 0
    count = 1

    for line in lines:
        lineVal = lineq.search(line)
        print(count)
        count += 1
        if lineVal is None:
            continue
        tempVal = {}
        for category in ATTRIBUTES:
            tempVal[category] = lineVal.group(category)
        currentTime = patToTime(tempVal)
        if prevKeyPressTime > 0:
            if tempVal["type"] == 'P':
                avePressToPressTime += currentTime - prevKeyPressTime
            else:
                print(tempVal["content"] + ": " + str(currentTime)  + "/" + str(prevKeyPressTime) + "/" + str(currentTime - prevKeyPressTime))
                avePressToReleaseTime += currentTime - prevKeyPressTime
        
        if tempVal["type"] == 'P':
            actionCount += 1
            prevKeyPressTime = currentTime
            if tempVal["content"] == 'DEL':
                countBackspace += 1
            
    avePressToPressTime /= actionCount
    avePressToReleaseTime /= actionCount

    return (avePressToPressTime, avePressToReleaseTime, countBackspace)
    
if __name__ == "__main__":
    fname = sys.argv[1]
    acquireData(fname)