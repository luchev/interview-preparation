# Complexity (n = length of input string)
# Time complexity: O(n)
# Space complexity: O(n)

digits = [str(x) for x in range(10)]
signs = ['-', '+']
es = ['e', 'E']

class Solution:
    def isNumber(self, s: str) -> bool:
        s1, ok = ingestDecimal(s)
        if not ok:
            s1, ok = ingestInteger(s)
        if len(s1) == 0: # exponent is optional
            return ok

        s1, ok_exp = ingestExponent(s1)
        return len(s1) == 0 and ok_exp and ok

def ingestExponent(s: str):
    if len(s) < 2:
        return s, False
    
    if s[0] not in es:
        return s, False
    return ingestInteger(s[1:])
    
def ingestDecimal(s: str):
    if len(s) == 0:
        return "", False
    
    s, ok_int1 = ingestInteger(s)
    s, ok = ingestDot(s)
    if not ok:
        return s, False
    s, ok_int2 = ingestUnsigned(s)
    
    return s, ok_int1 or ok_int2

def ingestSign(s: str):
    if len(s) == 0:
        return "", False
    
    if s[0] in signs:
        return s[1:], True
    return s, False
    
def ingestDot(s: str):
    if len(s) == 0:
        return "", False
    
    if s[0] == '.':
        return s[1:], True
    return s, False

def ingestUnsigned(s: str):
    if len(s) == 0:
        return "", False
    
    for i in range(len(s)):
        if s[i] not in digits:
            return s[i:], i > 0
    
    return "", True

def ingestInteger(s: str):
    s, _ = ingestSign(s)
    return ingestUnsigned(s)
