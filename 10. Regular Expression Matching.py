import re

def isMatch(s: str, p: str) -> bool:
        p = p.replace('***', '*')
        if re.fullmatch(p, s):
            return True
        else:
            return False

print(isMatch(s = 'aa', p = 'a*'))
