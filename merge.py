def merge_insertion_sort(X, y):

    h = 0

    i = 0

    j = 0

    c = 0

    if(len(X) > 1):

        middle = len(X) // 2

        a1 = X[:middle]

        a2 = X[middle:]

        c = merge_insertion_sort(a1, y) + 1

        c = merge_insertion_sort(a2, y) + 1

        while(h < len(a1) and i < len(a2)):
            if(a1[h] < a2[i]):

                X[j] = a1[h]
                h += 1
            else:
                X[j] = a2[i]
                i += 1
            j += 1

        while(h < len(a1)):

            X[j] = a1[h]

            j += 1

            h += 1

        while(i < len(a2)):

            X[j] = a2[j]

            j += 1

            i += 1

        if(c == y - 1):
            print("Sort on: ")

            print(a1)
            a1 = insertion_sort(a1)

            print("  Sort on: ")

            print(a2)
            a2 = insertion_sort(a2)

    return c


def insertion_sort(z):
    for a in range(0, len(z)):

        if(a != len(z) - 1):

            part = a + 1

            if(z[a] > z[part]):

                for b in range(0, part):

                    if(z[b] > z[part]):

                        z[b], z[part] = z[part], z[j]

    return z

# online code


def mergeSort(arr):

    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array

        L = arr[:mid]  # Dividing the array elements

        R = arr[mid:]  # into 2 halves
        mergeSort(L)  # Sorting the first half
        mergeSort(R)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1

            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


def insertionSort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
