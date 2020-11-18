def Heap(arrays, x):

    for j in range(int((x - 2) / 2) + 1):

        if arrays[2 * j + 1] > arrays[j]:

            return False

        if (2 * j + 2 < x and

                arrays[2 * j + 2] > arrays[j]):

            return False

    return True


def mainfunction():
    value = input("Input an array: ")

    value = value.split(" ")

    arrays = [int(j) for j in value]

    s = int(input("Input an heap size: "))

    print(Heap(arrays, s))


mainfunction()
