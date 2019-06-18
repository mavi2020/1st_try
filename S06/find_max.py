lst = [4, 2, 59, 32]
mx=lst[0]
index_max=0
mn=lst[0]
index_min=0

for i in range(len(lst)):
    if mx < lst[i]:
        mx = lst[i]
        index_max=i
    elif mn > lst[i]:
        mn = lst[i]
        index_min=i

print("max member is: ",mx, index_max)
print("min member is: ", mn, index_min)