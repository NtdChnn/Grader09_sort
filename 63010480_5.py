change = False
def bubbleSortInside(index = 0):
    global List
    global change
    if int(List[index][1]) == int(List[index+1][1]):
        key1 = int(List[index][2])
        key2 = int(List[index+1][2])
    else:
        key1 = int(List[index][1])
        key2 = int(List[index+1][1])
    if key1 < key2:
        y = List[index].copy()
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

def CalculateScore(ListOC):
    for i in ListOC:
        i.append((3*int(i[1]))+int(i[3]))
        i.append(int(i[4])-int(i[5]))
        for n in range(0,5):
            i.pop(1)

    return ListOC


ip = input('Enter Input : ').split('/')
listOfClubUnScore = []
for i in ip:
    listOfClubUnScore.append(i.split(',').copy())
listOfClubScored = CalculateScore(listOfClubUnScore).copy()
List = listOfClubScored.copy()
bubbleSortOutside()
print('== results ==')
for i in List:
    print(f'[\'{i[0]}\', {{\'points\': {i[1]}}}, {{\'gd\': {i[2]}}}]')