def lcs(a,b):
    prev = [0]*len(a)
    for i,r in enumerate(a):
        current = []
        for j,c in enumerate(b):
            if r==c:
                e = prev[j-1]+1 if i*j > 0 else 1
            else:
                e = max(prev[j] if i > 0 else 0, current[-1] if j > 0 else 0)
            current.append(e)
        prev = current
    return current[-1]
def compare(filename):
    A = []
    B = []
    with open(filename+".keylog","r",encoding='utf-8') as f:
        A = f.readlines()
    with open("correct.keylog","r",encoding='utf-8') as f:
        B = f.readlines()
    result = lcs(A,B)
    error = len(A) - result
    return error