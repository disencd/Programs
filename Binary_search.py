def bin_search(list, no):
    first = 0
    length = len(list)
    last = length - 1

    for index in range(length):
        mid = (first + last) // 2

        if no == list[mid]:
            return True

        else:
            if no < list[mid]:
                last = mid - 1
            else:
                first = mid + 1

            

print (bin_search([12,23,34,45,56,67,78],12))
