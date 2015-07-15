#PS1
s="abc123"

# Count number of vowels in a string
totalVowels = s.count('a') + s.count('e') + s.count('i') + s.count('o') + s.count('u')
print("Number of vowels: " + str(totalVowels))

#Find the number of patterns in a string
start=0
cnt=0
pos=s.find('bob',start)
while pos >= 0:
    cnt += 1
    start = pos + 1
    pos=s.find('bob',start)
print("Number of times bob occurs is: " + str(cnt))

# Longest substring in alphabetical order
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