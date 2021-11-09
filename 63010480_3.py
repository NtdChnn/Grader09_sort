change = False
def bubbleSortInsideMinToMax(index = 0):
    global List
    global change
    if List[index] > List[index+1]:
        y = List[index]
        List.pop(index)
        List.insert(index+1,y)
        change = True
    if index+1 < len(List)-1:
        bubbleSortInsideMinToMax(index + 1)
    return change

def bubbleSortOutsideMinToMax():
    global change
    while bubbleSortInsideMinToMax():
        change = False
        bubbleSortInsideMinToMax()
    return List

def bubbleSortInsideMaxToMin(index = 0):
    global List
    global change
    if List[index] < List[index+1]:
        y = List[index]
        List.pop(index)
        List.insert(index+1,y)
        change = True
    if index+1 < len(List)-1:
        bubbleSortInsideMaxToMin(index + 1)
    return change

def bubbleSortOutsideMaxToMin():
    global change
    while bubbleSortInsideMaxToMin():
        change = False
        bubbleSortInsideMaxToMin()
    return List

ip = [int(i) for i in input('Enter Input : ')]
List = ip.copy()
ListMinToMax = bubbleSortOutsideMinToMax().copy()
ListMaxToMin = bubbleSortOutsideMaxToMin().copy()
duplicate = False
Repdrome = True
for i in range(0,len(ip)):
    if ip[i] in ip[i+1:]:
        duplicate = True
for i in range(0,len(ip)-1):
    if ip[i] != ip[i+1]:
        Repdrome = False
        break
if Repdrome:
    print("Repdrome")
elif ip == ListMinToMax and not duplicate:
    print("Metadrome")
elif ip == ListMinToMax and duplicate:
    print("Plaindrome")
elif ip == ListMaxToMin and not duplicate:
    print("Katadrome")
elif ip == ListMaxToMin and duplicate:
    print("Nialpdrome")
else: print("Nondrome")

