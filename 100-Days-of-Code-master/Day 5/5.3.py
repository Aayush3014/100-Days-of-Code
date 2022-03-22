# For finding Min Number.

n = int(input("Number of elements you want to enter : "))
l = []

for i in range(n):
    ele = int(input("Enter the element you want to enter : "))
    l.append(ele)
mini = l[0]
for j in l:
    if j < mini:
        mini = j
else:
    print(mini)
