fr = open('data.txt')
data = fr.read()
data = data.split(',')
# print(data)
lst = []
duration = []
t1 = 200
t2 = 201

for t in range(len(data)):
    lst.append(float(data[t]))

# print(lst)
for d in range(len(lst) - 1):
    duration.append(lst[d + 1] - lst[d])

# print(duration)

check_duration = []
for i in range(len(duration)):
    if duration[i] <= t1:
        check_duration.append('S')
    elif duration[i] >= t2:
        check_duration.append('L')
    elif t1 < duration[i] < t2:
        check_duration.append('M')
# print(check_duration)

count = [0, 0, 0, 0]
for c in range(len(check_duration) - 2):
    if check_duration[c] == 'L':
        if c <= len(check_duration) - 2 and check_duration[c + 1] == 'S' and check_duration[c + 2] == 'L':
            count[0] += 1
            print("LSL ","start index: ", c, "stop index: ", c + 3)
            print("data: ", float(data[c + 2]) - float(data[c]))
            print("duration: ", duration[c + 2] - duration[c])
        if c <= len(check_duration) - 3 and check_duration[c + 1] == "S" and check_duration[c + 2] == 'S' and \
                check_duration[c + 3] == 'L':
            count[1] += 1
            print("LSSL ","start index: ", c, "stop index: ", c + 4)
            print("data: ", float(data[c + 3]) - float(data[c]))
            print("duration: ", duration[c + 3] - duration[c])

        if c <= len(check_duration) - 4 and check_duration[c + 1] == "S" and check_duration[c + 2] == 'S' and \
                check_duration[c + 3] == 'S' and check_duration[c + 4] == 'L':
            count[2] += 1
            print("LSSSL ", "start index: ", c, "stop index: ", c + 5)
            print("data: ", float(data[c + 4]) - float(data[c]))
            print("duration: ", duration[c + 4] - duration[c])

        if c <= len(check_duration) - 5 and check_duration[c + 1] == "S" and check_duration[c + 2] == 'S' and \
                check_duration[c + 3] == 'S' and check_duration[c + 4] == 'S' and check_duration[c + 5] == 'L':
            count[3] += 1
            print("LSSSSL ", "start index: ", c, "stop index: ", c + 6)
            print("data: ", float(data[c + 5]) - float(data[c]))
            print("duration: ", duration[c + 5] - duration[c])

print("LSL_ count: ", count[0])
print("LSSL_ count: ", count[1])
print("LSSSL_ count: ", count[2])
print("LSSSSL_ count: ", count[3])
