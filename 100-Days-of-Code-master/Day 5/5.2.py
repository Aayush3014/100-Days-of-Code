# For finding Max Number.

n = int(input("Number of elements you want to enter : "))
l = []
max = 0
for i in range(n):
    ele = int(input("Enter the element you want to enter : "))
    l.append(ele)
for j in l:
    if j > max:
        max = j
else:
    print(max)
