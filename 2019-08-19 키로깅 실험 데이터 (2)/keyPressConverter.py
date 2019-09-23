import re
import sys

query = r"(?P<date>\d+:\d+:\d+):(?P<hour>\d+):(?P<minute>\d+):(?P<second>\d+):(?P<ms>\d+) (?P<content>.+) (?P<type>[PR])"

ATTRIBUTES = ["date", "hour", "minute", "second", "ms", "content", "type"]

def acquireData(filename):
    lines = None
    with open(filename,"r",encoding="utf-8") as f:
        lines = f.readlines()
        
    lineq = re.compile(query)
    
    result = ""
    targetName = filename[:-4] + ".keylog"
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
        if tempVal['type'] != 'P':
            continue
        result += tempVal['content'] + "\n"
    
    with open(targetName,"w",encoding="utf-8")as f:
        f.write(result)
    
if __name__ == "__main__":
    fname = sys.argv[1]
    acquireData(fname)