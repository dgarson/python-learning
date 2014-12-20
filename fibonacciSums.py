def eulerFib(maxValue = 4000000):
    sumEven, sumOdd, a, b = 0, 1, 1, 2;

    while (b < maxValue):
        if (b % 2 == 0):
            sumEven += b;
        elif (b % 2 == 1):
            sumOdd += b;
        a, b = b, a + b;


    print('sum of even numbers is',sumEven);
    print('sum of odd numbers is',sumOdd);

eulerFib();