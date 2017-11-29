n = int(input('Еnter a number in the range [1...100]: '))

while n < 1 or n > 100:
    print('Invalid number!')
    n = int(input('Еnter a number in the range [1...100]: '))

print('The number is: ' + str(n))