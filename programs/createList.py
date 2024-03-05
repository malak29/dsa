def createList ():
    list = []
    listLength = int(input("Enter length of list: "))
    while(listLength != 0 ):
        list.append(int(input("Enter a number: ")))
        listLength -= 1

    print(list, len(list))
    return list, len(list)
