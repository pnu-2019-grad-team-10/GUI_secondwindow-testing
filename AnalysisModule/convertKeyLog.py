import sys
import keycodeFinder as kf

def convertLog(pathheader,target):
    result = ""
    kf.initENG();
    kf.initKOR();
    kf.initKSH();
    f = open(pathheader + target,"r",encoding="utf-8")
    lines = f.readlines()
    prevkeyboard = 'KOR'
    for line in lines:
        argument = line.split(" ")
        if(len(argument) < 2):  
            continue
        time = argument[0]
        keycode = argument[1]
        keyboard = argument[2]
        action = argument[3]
        if action == "P\n":
            prevkeyboard = keyboard
        elif action == "R\n" and prevkeyboard != keyboard:
            keyboard = prevkeyboard
        output = kf.findCode(keyboard,keycode)
        result += time + " " + output + " " + action + "\n"
    with open(pathheader + "converted-" + target, "w", encoding = "utf-8") as f:
        f.write(result)
        
if __name__=="__main__":
    target = sys.argv[1]
    convertLog(target)
    