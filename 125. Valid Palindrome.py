import string


def isPalindrome(s):
        propstring = ''.join(i for i in s if i not in string.punctuation)
        propstring = propstring.replace(' ','')
        l = 0
        r = len(propstring)-1
        while l<len(propstring)/2:
                if str.lower(propstring[l]) == str.lower(propstring[r]):
                        l+=1
                        r-=1
                else:
                        return False
        return True


print(isPalindrome(' '))

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.