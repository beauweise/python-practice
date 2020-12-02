print ("hello world")



if 5 > 2:
    print("Five is greater than two!")

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

for x in "beau":
    print (x)

x = 5
y = "John"
print(type(x))
print(type(y))

def fizzBuzz(num):
    if num % 15 == 0:
        return 'FizzBuzz'
    elif num % 5 == 0:
        return 'Fizz'
    elif num % 3 == 0:
        return 'Buzz'

print(fizzBuzz(15))
print(fizzBuzz(5))
print(fizzBuzz(3))

x-5
print(x)

teststring = "abcdefg"

def reverse(string):
    return string[::-1]

print(reverse(teststring))