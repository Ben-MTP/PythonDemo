intNumber = [12, 23, 32, 12, 34, 34, 54, 65, 655, 44, 33, 55, 66, 77, 665, 98, 62, 52, 14, 98, 654, 52, 34]
intSumNumber = 0;
intMulti = 1;
intDev = 0;
intDiv = 0.0;
intIndex = 0;
for x in intNumber:
    # Sum value of array:
    intSumNumber = intSumNumber + intNumber[intIndex];

    #Multi value arr[1] and arr[3]:
    intMulti = intNumber[1] * intNumber[3];

    #Value of Div arr[1] and arr[3]:
    intDiv = intNumber[1] / intNumber[3];

print("Sum off array int: " + str(intSumNumber));
print("Multi value of arr[1] and arr[3]: " + str(intMulti));
print("Value of div between arr[1] and arr[3]: " + str(int(intDiv)))