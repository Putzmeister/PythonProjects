n1 = int(input())
n2 = int(input())
operator = input().lower()

if 0 <= n1 <= 40000 and 0 <= n2 <= 40000:
    if operator == '+':
        result = n1 + n2
        even = result % 2
        if even == 0:
            print(str(n1) + ' + ' + str(n2) + ' = ' + str(result) + ' - ' + 'even')
        elif even != 0:
            print(str(n1) + ' + ' + str(n2) + ' = ' + str(result) + ' - ' + 'odd')
    elif operator == '-':
        result = n1 - n2
        even = result % 2
        if even == 0:
            print(str(n1) + ' - ' + str(n2) + ' = ' + str(result) + ' - ' + 'even')
        elif even != 0:
            print(str(n1) + ' - ' + str(n2) + ' = ' + str(result) + ' - ' + 'odd')
    elif operator == '*':
        result = n1 * n2
        even = result % 2
        if even == 0:
            print(str(n1) + ' * ' + str(n2) + ' = ' + str(result) + ' - ' + 'even')
        elif even != 0:
            print(str(n1) + ' * ' + str(n2) + ' = ' + str(result) + ' - ' + 'odd')
    elif operator == '/':
        if n2 != 0:
            result = n1 / n2
            print(str(n1) + ' / ' + str(n2) + ' = ' + str('%.2f' % result))
        elif n2 == 0:
            print('Cannot divide ' + str(n1) + ' by zero')
    elif operator == '%':
        if n2 != 0:
            result = n1 % n2
            print(str(n1) + ' % ' + str(n2) + ' = ' + str(result))
        elif n2 == 0:
            print('Cannot divide ' + str(n1) + ' by zero')



