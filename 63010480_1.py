change = False
def bubbleSortInside(index = 0):
    global List
    global change
    if List[index] > List[index+1]:
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
print(List)