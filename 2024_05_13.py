
def maxProduct(list):

    if len(list)==3:
        return list[0]*list[1]*list[2]
    
    list.sort()
    print(list)

    candidates = list[-3:]
    if list[0]<0 and list[1]<0 and list[0]*list[1] > candidates[0]*candidates[1]:
        candidates[0] = list[0]
        candidates[1] = list[1]
    
    print(candidates)

    return candidates[0]*candidates[1]*candidates[2]



list = [2, 4, 1, 3, -5, 6]
print(maxProduct(list))

list = [-2, 4, 1, 3, -5, 6]
print(maxProduct(list))

list = [-1, 3, 1, 2, -5, 6]
print(maxProduct(list))