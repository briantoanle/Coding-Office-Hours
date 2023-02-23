a=[-1,150,190,180,-1,-1,160,170]

def findPeople(a):
    temp = []
    for i in range(len(a)):
        if a[i] != -1:
            temp.append(a[i])
    temp = sorted(temp)
    print(temp)

    final = []
    count = 0
    for i in range(len(a)):
        if a[i] == -1:
            final.append(-1)
            count+=1
        else:
            final.append(temp[i-count])

    print(final)

findPeople(a)