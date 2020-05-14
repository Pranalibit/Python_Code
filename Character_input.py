import datetime
name = input("Enter your name: ")
age = int(input("Enter your age: "))
hundred = (100 - age) + (datetime.datetime.now()).year
msg = "Hey {}, you will be 100 year old in year {}".format(name, hundred)
print(msg)
num = int(input("Give me a number: "))
i = 1
while i - 1!=num:
    print(msg)
    i += 1
#Another short method
msg += "\n"
print(msg * num)
