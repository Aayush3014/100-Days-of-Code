# Average Heights of students
heights = input("Enter Heights of Students: ").split()
sum = 0
for n in range(0,len(heights)):
    heights[n] = int(heights[n])
    sum += int(heights[n])
avg = sum//len(heights)
print(sum)
print(avg)