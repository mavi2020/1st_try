lst = [4, 2, 59, 32]
mx=lst[0]
mn=lst[0]

for i in lst:
    if mx < i:
        mx = i
    elif mn > i:
        mn = i

print("max member is: ",mx)
print("min member is: ", mn)