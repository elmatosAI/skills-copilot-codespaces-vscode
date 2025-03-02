# given one number by the user, show the two prime numbers that were multiplied to obtain the number

# user introduces a number
num = int(input('Enter a number: '))
# initialize a list to store the prime numbers
prime_numbers = []
# loop through the range of the number
for i in range(2, num):
    # check if the number is prime
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        prime_numbers.append(i)
# loop through the prime numbers list
for i in prime_numbers:
    # check if the number is prime
    for j in prime_numbers:
        if i * j == num:
            print(f'{i} * {j} = {num}')
            break
    else:
        continue
    break
# if there are no prime numbers that multiply to obtain the number, print the following message
else:
    print('The number entered is not the result of multiplying two prime numbers')
# keep asking numbers in a loop until the user enters 0
while True:
    # ask the user to enter a number
    num = int(input('Enter a number (0 to exit): '))
    # check if the number is 0
    if num == 0:
        break
    # initialize a list to store the prime numbers
    prime_numbers = []
    # loop through the range of the number
    for i in range(2, num):
        # check if the number is prime
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            prime_numbers.append(i)
    # loop through the prime numbers list
    for i in prime_numbers:
        # check if the number is prime
        for j in prime_numbers:
            if i * j == num:
                print(f'{i} * {j} = {num}')
                break
        else:
            continue
        break
    # if there are no prime numbers that multiply to obtain the number, print the following message
    else:
        print('The number entered is not the result of multiplying two prime numbers')


# print a message to say goodbye
print('Goodbye!')