num = input("Enter a number: ")
if int(num) %2 == 0:
    print('{} is even number'.format(num))
    var = num[len(num) - 1:len(num) + 1]
    if int(var) % 4==0 :
        print("{} is divisible by 4".format(num))
else:
    print('{} is odd number'.format(num))
p = int(input('Give me one more number: '))
check = int(input("Give one more number please: "))
if p % check == 0:
    print('{} divides {} completely'.format(check, p))
else:
    print('{} don\'t divide {} completely'.format (check, p))
