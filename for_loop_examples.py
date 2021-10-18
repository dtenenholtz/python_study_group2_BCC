# for loop example 1
for num in [0,1,2,3,4,5,6,7,8,9]:
    print(num)

# for loop example 1a
for num1a in range(1,10):
    print(num1a)

# for loop example 2
start = int(input('Enter a starting number: '))
end = int(intput('Enter an ending number: '))

total = 0
for mynum in range(start, end + 1):
    total = total + mynum

print('Total=', total)
