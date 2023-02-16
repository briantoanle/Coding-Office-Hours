
l1 = [123, -17, -5, 1, 2, 3, 12, 43, 45] #true
l2 = [40, 50, 60, 10, 20, 30] #false
l3 = [1, 2, 3, 4, 5, 3, 5, 6] #false

def solution(sequence):
    count = 0
    index = -1
    for i in range(1,len(sequence)):
        if(sequence[i-1] >=sequence[i]):
            count +=1
            index = i

        if count >1:
            return False
        if count == 0:
            return True
        if index==len(sequence)-1 or index==1:
            return True
        if sequence[index-1] < sequence[index+1]:
            return True
        if sequence[index-2]<sequence[index]:
            return True
        return False

def solution1(sequence):
    #print(sequence)
    counter = 0
    for i in range(0,len(sequence)-2):
        print(sequence[i],sequence[i+1])
        if sequence[i] >= sequence[i+1]:
            print('here')
            counter+=1
        if sequence[i] >= sequence[i+2]:
            print('here')
            counter+=1
    if counter > 2:
        print('False')
print(solution(l1),solution(l2),solution(l3))

def solution(sequence):
    counter = 0
    for i in range(len(sequence)):
        temp = sequence.copy()
        temp.pop(i)
        if temp == sorted(temp):
            l = []
            for i in range(len(temp)):
                if temp[i] not in l:
                    l.append(temp[i])
            if temp == l:
                return True
    return False