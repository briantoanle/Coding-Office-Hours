arr = [[0,0,0,0,0],
       [0,0,0,9,0],
       [0,9,0,0,0],
       [0,0,0,9,0],
       [0,0,0,0,0]]

# Coding problem with Meta Engineer in Residence
# return livable spaces
def livable(arr):
    ghosts=[]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if (arr[i][j] == 9):
                if(arr[i][j] not in ghosts):
                    ghosts.append([i,j])

        """for i in range(len(ghosts)):
            for j in range(-1,2,2):
                if (ghosts[i][1] + j) >= 0 and ghosts[i][1] + j <=(len(arr[i])-1):
                    ghosts.append([i,(ghosts[i][1]+j)])"""
    ghost1 = ghosts.copy()

    # add adjacent plots to the sides of the ghost coordinates
    for i in range(len(ghosts)):
        for k in range(ghosts[i]):
            print('he')
        for j in [-1, 1]:
            if 0 <= ghosts[i][1] + j < len(arr[i]):
                new_ghost = [ghosts[i][0], ghosts[i][1] + j]
                ghosts.append(new_ghost)



    print(ghosts)
livable(arr)

def recur(n):
    if n==0 or n==1:
        return 1
    else:
        return(recur(n-1)) +(recur(n-2))


#print(recur(5))