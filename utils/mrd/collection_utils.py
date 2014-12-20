__author__ = 'dgarson'

def eulerFib(maxValue = 4000000):

    sumEven = 0;
    sumOdd = 1;
    a, b = 1, 2;
    while (b < maxValue):
        if (b % 2 == 0):
            sumEven += b;
        elif (b % 2 == 1):
            sumOdd += b;
        a, b = b, a+b;
    print('even sum is ', sumEven)
    print('odd sum is ', sumOdd)

eulerFib();

def eulerFib()