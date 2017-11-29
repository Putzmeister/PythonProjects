
amount=float(input())
inputCurrency=str(input())
outputCurrency=str(input())


if inputCurrency == 'BGN' and outputCurrency == 'USD':
    result=amount / 1.79549
    print('%.2f' % result + ' USD')
elif inputCurrency == 'BGN' and outputCurrency == 'EUR':
    result=amount / 1.95583
    print('%.2f' % result + ' EUR')
elif inputCurrency == 'BGN' and outputCurrency == 'GBP':
    result = amount / 2.53405
    print('%.2f' % result + ' GBP')


if inputCurrency == 'USD' and outputCurrency == 'BGN':
    result=amount * 1.79549
    print('%.2f' % result + ' BGN')
elif inputCurrency == 'USD' and outputCurrency == 'EUR':
    result=amount * 1.79549 / 1.95583
    print('%.2f' % result + ' EUR')
elif inputCurrency == 'USD' and outputCurrency == 'GBP':
    result = amount * 1.79549 / 2.53405
    print('%.2f' % result + ' GBP')


if inputCurrency == 'EUR' and outputCurrency == 'BGN':
        result = amount * 1.95583
        print('%.2f' % result + ' BGN')
elif inputCurrency == 'EUR' and outputCurrency == 'USD':
        result = amount * 1.95583 / 1.79549
        print('%.2f' % result + ' USD')
elif inputCurrency == 'EUR' and outputCurrency == 'GBP':
        result = amount * 1.95583 / 2.53405
        print('%.2f' % result + ' GBP')


if inputCurrency == 'GBP' and outputCurrency == 'BGN':
        result = amount * 2.53405
        print('%.2f' % result + ' BGN')
elif inputCurrency == 'GBP' and outputCurrency == 'USD':
        result = amount * 2.53405 / 1.79549
        print('%.2f' % result + ' USD')
elif inputCurrency == 'GBP' and outputCurrency == 'EUR':
        result = amount * 2.53405 / 1.95583
        print('%.2f' % result + ' EUR')