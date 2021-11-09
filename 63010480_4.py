change = False
def bubbleSortInside(index = 0):
    global List
    global change
    Str1 = List[index]
    Str2 = List[index+1]
    for i in range(0,len(Str1)):
        if Str1[i].isalpha():
            key1 = Str1[i]
            break
    for i in range(0, len(Str2)):
        if Str2[i].isalpha():
            key2 = Str2[i]
            break
    if key1 > key2:
        y = List[index]
        List.pop(index)
        List.insert(index+1,y)
        change = True
    if index+1 < len(List)-1:
        bubbleSortInside(index+1)
    return change

def bubbleSortOutside():
    global change
    while bubbleSortInside():
        change = False
        bubbleSortInside()

List = input('Enter Input : ').split()
bubbleSortOutside()
print(*List)