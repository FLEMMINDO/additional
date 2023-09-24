def nextGreatestLetter(letters, target):
    starttarget = target
    toprint = letters[0]
    letters.sort()
    counter = 0
    while starttarget==target and counter!= len(letters):
        if letters[counter]>target:
            target = letters[counter]
        counter+=1
    if target!=starttarget:
        return target
    else:
        return toprint


print(nextGreatestLetter(letters = ["c","f","j"], target = "a"))