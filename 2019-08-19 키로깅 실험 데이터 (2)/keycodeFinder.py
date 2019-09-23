ENGKEY = {}
KORKEY = {}
KSHKEY = {}
    
def initENG():
    ENGKEY["113"]='q';
    ENGKEY["119"]='w';
    ENGKEY["101"]='e';
    ENGKEY["114"]='r';
    ENGKEY["116"]='t';
    ENGKEY["121"]='y';
    ENGKEY["117"]='u';
    ENGKEY["105"]='i';
    ENGKEY["111"]='o';
    ENGKEY["112"]='p';
    
    ENGKEY["-9"]='LOG';
    ENGKEY["97"]='a';
    ENGKEY["115"]='s';
    ENGKEY["100"]='d';
    ENGKEY["102"]='f';
    ENGKEY["103"]='g';
    ENGKEY["104"]='h';
    ENGKEY["106"]='j';
    ENGKEY["107"]='k';
    ENGKEY["108"]='l';
    
    ENGKEY["-1"]='SHIFT';
    ENGKEY["122"]='z';
    ENGKEY["120"]='x';
    ENGKEY["99"]='c';
    ENGKEY["118"]='v';
    ENGKEY["98"]='b';
    ENGKEY["110"]='n';
    ENGKEY["109"]='m';
    ENGKEY["-5"]='DEL';
    
    ENGKEY["-6"]='TOKOR';
    ENGKEY["-2"]='TONUM';
    ENGKEY["32"]='SPACE';
    ENGKEY["46"]='.';
    ENGKEY["44"]=',';
    ENGKEY["10"]='Return';
    
def initKOR():
    KORKEY["113"]='ㅂ';
    KORKEY["119"]='ㅈ';
    KORKEY["101"]='ㄷ';
    KORKEY["114"]='ㄱ';
    KORKEY["116"]='ㅅ';
    KORKEY["121"]='ㅛ';
    KORKEY["117"]='ㅕ';
    KORKEY["105"]='ㅑ';
    KORKEY["111"]='ㅐ';
    KORKEY["112"]='ㅔ';
    
    KORKEY["-9"]='LOG';
    KORKEY["97"]='ㅁ';
    KORKEY["115"]='ㄴ';
    KORKEY["100"]='ㅇ';
    KORKEY["102"]='ㄹ'
    KORKEY["103"]='ㅎ';
    KORKEY["104"]='ㅗ';
    KORKEY["106"]='ㅓ';
    KORKEY["107"]='ㅏ';
    KORKEY["108"]='ㅣ';
    
    KORKEY["-1"]='SHIFT';
    KORKEY["122"]='ㅋ';
    KORKEY["120"]='ㅌ';
    KORKEY["99"]='ㅊ';
    KORKEY["118"]='ㅍ';
    KORKEY["98"]='ㅠ';
    KORKEY["110"]='ㅜ';
    KORKEY["109"]='ㅡ';
    KORKEY["-5"]='DEL';
    
    KORKEY["-6"]='TOENG';
    KORKEY["-2"]='TONUM';
    KORKEY["32"]='SPACE';
    KORKEY["46"]='.';
    KORKEY["44"]=',';
    KORKEY["10"]='Return';
    
def initKSH():
    KSHKEY["113"]='ㅃ';
    KSHKEY["119"]='ㅉ';
    KSHKEY["101"]='ㄸ';
    KSHKEY["114"]='ㄲ';
    KSHKEY["116"]='ㅅ';
    KSHKEY["121"]='ㅛ';
    KSHKEY["117"]='ㅕ';
    KSHKEY["105"]='ㅑ';
    KSHKEY["111"]='ㅒ';
    KSHKEY["112"]='ㅖ';
    
    KSHKEY["-9"]='LOG';
    KSHKEY["97"]='ㅁ';
    KSHKEY["115"]='ㄴ';
    KSHKEY["100"]='ㅇ';
    KSHKEY["102"]='ㄹ'
    KSHKEY["103"]='ㅎ';
    KSHKEY["104"]='ㅗ';
    KSHKEY["106"]='ㅓ';
    KSHKEY["107"]='ㅏ';
    KSHKEY["108"]='ㅣ';
    
    KSHKEY["-1"]='SHIFT';
    KSHKEY["122"]='ㅋ';
    KSHKEY["120"]='ㅌ';
    KSHKEY["99"]='ㅊ';
    KSHKEY["118"]='ㅍ';
    KSHKEY["98"]='ㅠ';
    KSHKEY["110"]='ㅜ';
    KSHKEY["109"]='ㅡ';
    KSHKEY["-5"]='DEL';
    
    KSHKEY["-6"]='TOENG';
    KSHKEY["-2"]='TONUM';
    KSHKEY["32"]='SPACE';
    KSHKEY["46"]='.';
    KSHKEY["44"]=',';
    KSHKEY["10"]='Return';
    
def findCode(keyboard, keycode):
    result = None
    if keyboard == "ENG":
        result = ENGKEY[keycode];
    elif keyboard == "KOR":
        result = KORKEY[keycode];
    else:
        result = KSHKEY[keycode];
    return result;