def romanToInt(s):
    romanDict = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
    }
    total = 0
    letters = list(s)
    i=0
    semiTotal = 0
    while i < len(list(s)):
        #check if i < i+1
        semiTotal += romanDict[letters[i]]

        if i == len(letters)-1:
            total += semiTotal
            semiTotal = 0
            i+=1
            continue
        elif romanDict[letters[i]] < romanDict[letters[i+1]]:
            #here we have a reset 
            # need to dump semittoal
            total+= semiTotal -romanDict[letters[i]]
            semiTotal = romanDict[letters[i]]
            semiTotal = romanDict[letters[i+1]] - semiTotal
            total += semiTotal
            semiTotal = 0
            i+=2
            continue
        i+=1
    return total



        

print(romanToInt('MCXCIV'))