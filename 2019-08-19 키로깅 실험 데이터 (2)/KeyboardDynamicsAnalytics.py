import convertKeyLog
import keyLogStatics
import keyPressConverter
import lcs

SLOPE_PTP = -0.000019149808847818817
INTERCEPT_PTP = 0.056337597321837574
SLOPE_PTR = -0.0005577978229345415
INTERCEPT_PTR = 0.09315867688652194

def getFunctionValue(slope, intercept, target):
    return slope*target + intercept
    
    
def analyzeKeystrokeData(realpath):
    pathheader = "\\".join(realpath.split("\\")[:-1]) + "\\"
    filepath = realpath.split("\\")[-1]
    print(filepath)
    filename = filepath.split(".")[0]
    convertKeyLog.convertLog(pathheader,filepath)
    convertedFilepath = 'converted-' + filepath
    PTP, PTR, BSP = keyLogStatics.acquireData(pathheader + convertedFilepath)
    keyPressConverter.acquireData(pathheader + convertedFilepath)
    LCS = lcs.compare(pathheader + 'converted-'+filename)
    print(getFunctionValue(SLOPE_PTP,INTERCEPT_PTP,PTP),getFunctionValue(SLOPE_PTR,INTERCEPT_PTR,PTR), BSP, LCS)
    return (getFunctionValue(SLOPE_PTP,INTERCEPT_PTP,PTP),getFunctionValue(SLOPE_PTR,INTERCEPT_PTR,PTR), BSP, LCS)
    
if __name__ == '__main__':
    import sys
    filepath = sys.argv[1]
    analyzeKeystrokeData(filepath)