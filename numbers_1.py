# add two numbers entered by user and print the result

num1 = input('Enter first number: ')
num2 = input('Enter second number: ')

sum = float(num1) + float(num2)

print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))

# show the series of prime numbers starting in 1 and ending in the sum obtained in the previous code
# Python program to display all the prime numbers within an interval
# change the values of lower and upper for a different result

lower = 1
upper = int(sum)

print('Prime numbers between', lower, 'and', upper, 'are:')

for num in range(lower, upper + 1):
    # all prime numbers are greater than 1
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
