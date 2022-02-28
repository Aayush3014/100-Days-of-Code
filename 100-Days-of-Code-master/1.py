import random
names = "Ayush, Nikhil, Amit, Pawan"
l = names.split(",")
r = random.randint(0,3)
print(r)
if r == 0:
    print("Ayush")
elif r==1:
    print("Nikhil")
elif r==2:
    print("Amit")
else:
    print("Pawan")