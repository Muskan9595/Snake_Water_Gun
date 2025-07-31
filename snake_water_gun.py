
import random

def check(comp_choice, user_choice):
    if user_choice==0 and comp_choice==1:
        return 1
    
    elif user_choice==1 and comp_choice==2:
        return 1
    
    elif user_choice==2 and comp_choice==0:
        return 1
    
    elif  user_choice==0 and comp_choice==2:
        return -1
    
    elif user_choice==1 and comp_choice==0:
        return -1
    
    elif user_choice==2 and comp_choice==1:
        return -1
    
    else:
        return 0

comp_choice=random.randint(0,2)
choices=['Snake', 'Water', 'Gun']
print("\nEnter 0 for Snake, 1 for Water & 2 for Gun.\n")
user_choice=int(input("Enter your input: "))
print(f"\nUser choose: {user_choice}, which is for {choices[user_choice]} ")
print(f"Computer choose: {comp_choice}, which is for {choices[comp_choice]}\n")
result=check(comp_choice, user_choice)

if (result==-1):
    print("..........Computer Won!..........\n")

elif(result==1):
    print("----------Congratulations! You Won!----------\n")

else:
    print("__________It's a draw__________\n")




