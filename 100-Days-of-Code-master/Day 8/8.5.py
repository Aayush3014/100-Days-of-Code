# Prime Number Checker.

n = int(input("Enter The Number : "))
def prime_number(n):
    for i in range(2,n):
        if n % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime Number")
prime_number(n)