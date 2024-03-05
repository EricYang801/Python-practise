print("請輸入十進位的數字", end="")
num = input()

num = float(num)  
if num.is_integer():  
    num = int(num)  
else:
    integer_part, decimal_part = str(num).split(".")  
    integer_part = int(integer_part)  
    decimal_part = float("0." + decimal_part)  

# 將整數部分轉換為二進位
integer_num_list = []
while integer_part > 0:
    remainder = integer_part % 2
    integer_num_list.insert(0, remainder)
    integer_part //= 2

# 將小數部分轉換為二進位
decimal_num_list = []
while decimal_part > 0:
    decimal_part *= 2
    integer_part = int(decimal_part)
    decimal_num_list.append(integer_part)
    decimal_part -= integer_part

# 將二進位數字組合為一個字串
binary_num = ''.join(map(str, integer_num_list))
if decimal_num_list:
    binary_num += "."
    binary_num += ''.join(map(str, decimal_num_list))

print("二進位表示為：", binary_num)