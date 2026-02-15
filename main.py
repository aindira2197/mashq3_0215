# 1
n = int(input())
s = 0
for i in range(1, n + 1):
    if i % 4 == 0:
        s += i
print(s)

# 2
n = int(input())
for i in range(1, n + 1):
    print(i, i ** 4)

# 3
n = int(input())
count = 0
for i in range(1, n + 1):
    if i % 6 == 0:
        count += 1
print(count)

# 4
n = int(input())
for i in range(1, n + 1):
    if str(i).endswith("3"):
        print(i)

# 5
n = int(input())
s = 0
for i in range(1, n + 1):
    if i % 2 == 1:
        s += i ** 2
print(s)
