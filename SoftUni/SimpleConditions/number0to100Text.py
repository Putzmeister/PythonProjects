num = int(input())

numbers = {1:'one' , 2:'two' , 3:'three' , 4:'four' , 5:'five' , 6:'six' , 7:'seven' , 8:'eight' , 9:'nine'}
special = {10:'ten' , 11:'eleven', 12:'twelve', 13:'thirteen' , 14:'fourteen' , 15:'fifteen' , 16:'sixteen' , 17:'seventeen' , 18:'eighteen', 19:'nineteen'}
decimals = {20:'twenty' , 30:'thirty' , 40:'forty' , 50:'fifty' , 60:'sixty' , 70:'seventy' , 80:'eighty' , 90:'ninety'}

if num == 0:
    print('zero')
elif num == 100:
    print('one hundred')
elif 0 < num < 10:
    print(numbers[num])
elif 10 <= num <= 19:
    print(special[num])
elif num % 10 == 0 and 0 < num < 100:
    print(decimals[num])
elif num % 10 != 0 and 0 < num < 100:
    wholedecimal = (num // 10) * 10
    wholenumber = num % 10
    print(decimals[wholedecimal] + ' ' + numbers[wholenumber])
else:
    print('invalid number')



