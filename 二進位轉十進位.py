print("請輸入二進位的數字", end = "")
num = int(input())
numlist=[]
numout=0
numlist = [int(a) for a in str(num)]
power=len(numlist)-1
for digit in numlist:
    numout += digit * (2 ** power)
    power -= 1
    
print(numout)



