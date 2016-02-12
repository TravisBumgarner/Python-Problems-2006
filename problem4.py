def isPal(num):
    num = str(num)
    if(len(num) == 0) or (len(num) ==1 ):
        print(num)
        return True
        
    elif len(num) >= 2:
        print("length >=2")
        if num[0] == num [-0]:
            return isPal(num[1:-1])
        else:
            return False
largestVal = 0
val = 0

'''
for i in range(999,0,-1):
    for j in range(999,0,-1):
        val = i*j
        if isPal(val):
            if val > largestVal:
                largestVal = val
                print(val)
print(largestVal)
'''
"900099"
