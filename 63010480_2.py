change = False
def bubbleSortInside(index = 0):
    global List
    global change
    n = index+1
    while List[n] < 0:
        n += 1
        if n == len(List):
            break
    if n < len(List):
        if List[index] > List[n]:
            y = List[index]
            List.pop(index)
            List.insert(n,y)
            x = List[n-1]
            List.pop(n-1)
            List.insert(index,x)
            change = True
    if n < len(List)-1:
        bubbleSortInside(n)
    return change

def bubbleSortOutside():
    global change
    while bubbleSortInside():
        change = False
        bubbleSortInside()

List = [int(i) for i in input('Enter Input : ').split()]
bubbleSortOutside()
print(*List)