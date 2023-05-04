# Problem Statement 
# You are given an array of integers 'ARR' of length 'N' and an integer Target. Your task is to return all pairs of elements such that they add up to Target.
# Note: We cannot use the element at a given index twice.
# Follow Up: Try to do this probelm in O(N) time complexity.


def twoSum(arr, target, n):
    # Write your code here.
    res = []
    unordered = {}
    for ele in arr:
        if target-ele in unordered and unordered[target-ele] >0:
            res.append([ele,target-ele])
            unordered[target-ele] -= 1
        else:
            if ele in unordered:
                unordered[ele] +=1
            else:
                unordered[ele] = 1
    if not res:
        res.append([-1,-1])
    return res

def takeInput() :

    n, tar = map(int, input().strip().split(" "))
    arr = list(map(int, input().strip().split(" ")))
    return n, tar, arr

def printAns(ans):
    for i in ans:
        if i[0] < i[1]:
            print('{} {}'.format(i[0], i[1]))
        else:
            print('{} {}'.format(i[1], i[0]))

t = int(input().strip())
for i in range(t) :

    n, target, arr = takeInput()

    ans = twoSum(arr, target, n)
    printAns(ans)