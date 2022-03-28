import random

lives = 5
user_choice = "y"
word_list = ["mouse","monitor"]
word = random.choice(word_list)
print(word)
spaces = len(word)
print(spaces)
while user_choice == "y":
    
    
    while spaces>0 and lives>0:
        alphabet = input("Guess the alphabet : ")

        if alphabet in word :
        
            print(alphabet)
            word = word.replace(alphabet,'')
            spaces-=1
            user_choice = input("choose more or not?  y/n  ")
            #print("spaces",spaces)
        else:
            lives -= 1
            user_choice = input("choose more or not?  y/n")
            #print("Lives",lives)
    