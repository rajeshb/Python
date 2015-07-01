print "Hello,World!"
print "I like 6.00.1x!"

num = 0
while num <= 5:
    print num
    num += 1
print "Outside of loop"
print num

#x = raw_input("Enter value:")
#print x
#print type(x)

myStr = '6.00x'

for char in myStr:
    print char
print 'done'

greeting = 'Hello!'
count = 0
for letter in greeting:
    count += 1
    if count % 2 == 0:
        print letter
    print letter
print 'done'

school = 'Massachusetts Institute of Technology'
numVowels = 0
numCons = 0

for char in school:
    if char == 'a' or char == 'e' or char == 'i' \
    or char == 'o' or char == 'u':
        numVowels += 1
    elif char == 'o' or char == 'M':
        print char
    else:
        numCons -= 1
print 'numVowels is: ' + str(numVowels)
print 'numCons is: ' + str(numCons)

print '---------'

num = 10
for num in range(5):
    print num
print num

print '---------'

divisor = 2
for num in range(0, 10, 2):
    print num/divisor

print '---------'

for variable in range(20):
    if variable % 4 == 0:
        print variable
    if variable %16 == 0:
        print 'Foo!'

print '---------'

for letter in 'hola':
    print letter

print '---------'

iteration = 0
count = 0
while iteration < 5:
    for letter in "hello, world":
        count += 1
    print "Iteration " + str(iteration) + "; count is: " + str(count)
    iteration += 1

print '---------'

iteration = 0
while iteration < 5:
    count = 0
    for letter in "hello, world":
        count += 1
    print "Iteration " + str(iteration) + "; count is: " + str(count)
    iteration += 1

print '---------'

iteration = 0
while iteration < 5:
    count = 0
    for letter in "hello, world":
        count += 1
        if iteration % 2 == 0:
            break
    print "Iteration " + str(iteration) + "; count is: " + str(count)
    iteration += 1

print '---------'
