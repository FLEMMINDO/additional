def longestValidParentheses(s):
    counter = 0
    while '()' in s:
        s = s.replace('()', '',1)
        counter+=2
    return counter

print(longestValidParentheses(")()())"))