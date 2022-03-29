choice = "yes"
while choice == "yes":

    process = input("Type 'Encode' to Encode a Message or \nType 'Decode' to Decode a Message : ")
    word = input("Enter the Word : ")
    shift = int(input("Enter the number of shifts : "))

    if process == "Encode":
        print("Encrypted Cipher is : ",end=' : ')
        for i in word:
            encrypted = chr(ord(i)+shift)
            print(encrypted,end='')
        print()
    elif process == "Decode":
        print("Decrypted Cipher is : ",end=' : ')
        for i in word:
            decrypted = chr(ord(i)-shift)
            print(decrypted,end='')
        print()
    user_choice = input("Type 'yes' if you want to continue the process else Type no  yes/no  ")
else:
    exit()