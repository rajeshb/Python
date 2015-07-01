s = 'azcbobobegghakl'
#s = 'abcbcd'

maxStartPos = 0
maxEndPos = 0

startPos = 0
endPos = 0

currentPos = 1

maxLength= len(s)

while currentPos < maxLength:
    if s[currentPos-1] <= s[currentPos]:
        currentPos += 1
        endPos += 1
    else:
        if (endPos - startPos) > (maxEndPos - maxStartPos):
            maxStartPos = startPos
            maxEndPos = endPos
        startPos = currentPos
        endPos = currentPos
        currentPos +=1
if (endPos - startPos) > (maxEndPos - maxStartPos):
    maxStartPos = startPos
    maxEndPos = endPos
    
print("Longest substring in alphabetical order is: " + s[maxStartPos:maxEndPos+1])