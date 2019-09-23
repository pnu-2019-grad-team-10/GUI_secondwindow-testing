import convertKeyLog
import keyLogStatics
import keyPressConverter
import lcs

SLOPE_PTP = -0.000318542350205459
INTERCEPT_PTP = 0.170274
SLOPE_PTR = -0.00129836406128278369
INTERCEPT_PTR = 0.1640483

def getFunctionValue(slope, intercept, target):
    return slope*target + intercept
    
    
def analyzeKeystrokeData(realpath):
    pathheader = "/".join(realpath.split("/")[:-1]) + "/"
    filepath = realpath.split("/")[-1]
    print(filepath)
    filename = filepath.split(".")[0]
    convertKeyLog.convertLog(pathheader,filepath)
    convertedFilepath = 'converted-' + filepath
    PTP, PTR, BSP = keyLogStatics.acquireData(pathheader + convertedFilepath)
    keyPressConverter.acquireData(pathheader + convertedFilepath)
    LCS = lcs.compare(pathheader + 'converted-'+filename)
    AVE = (getFunctionValue(SLOPE_PTP,INTERCEPT_PTP,PTP) + getFunctionValue(SLOPE_PTR,INTERCEPT_PTR,PTR)) / 2
    print(AVE, getFunctionValue(SLOPE_PTP,INTERCEPT_PTP,PTP),getFunctionValue(SLOPE_PTR,INTERCEPT_PTR,PTR), PTP, PTR, BSP, LCS)
    return (getFunctionValue(SLOPE_PTP,INTERCEPT_PTP,PTP),getFunctionValue(SLOPE_PTR,INTERCEPT_PTR,PTR), PTP, PTR, BSP, LCS)
    
if __name__ == '__main__':
    import sys
    filepath = sys.argv[1]
    analyzeKeystrokeData(filepath)
