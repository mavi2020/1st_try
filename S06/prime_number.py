n = 1001  # int(input("Enter an integer number: "))

is_prime = True
for i in range(2, n):
    if n % i == 0:
        is_prime = False

if is_prime:
    print("Number ", n, " is prime")
else:
    print("Number ", n, " is not a prime number ")

prime_lst = [2]

for i in range(3, n):
    j = 1
    count = 0
    while j <= i:
        if i % j == 0:
            count += 1
            j += 1
        else:
            j += 1

    if count == 2:
        is_prime = True
        prime_lst.append(i)

print(prime_lst)
