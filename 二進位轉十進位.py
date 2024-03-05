print("請輸入二進位的數字", end = "")
num = input() 
numlist=[]
numout=0
integer_part, decimal_part = num.split(".") # 用小數點分開整數和小數
numlist = [int(a) for a in str(integer_part)]
power=len(numlist)-1
for digit in numlist:
    numout += digit * (2 ** power)
    power -= 1
if decimal_part:
    numlist = [int(a) for a in str(decimal_part)]
    power=-1
    for digit in numlist:
        numout += digit * (2 ** power)
        power -= 1
print(numout)