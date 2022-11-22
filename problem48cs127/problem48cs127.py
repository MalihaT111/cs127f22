#Maliha Tasnim
#MALIHA.TASNIM64@myhunter.cuny.edu
#Date: October 24, 2022
#This program does stuff
import random 
def userinput () :
    ui = int(input("Enter only 1-6: "))
    while ui not in range(1,7):
        ui = int(input("Input needs to be in 1-6. Re-enter: "))
    return ui

def generate ():
    user = userinput()
    computer = random.randint(1,6)
    print(f"user: {user}")
    print(f"computer: {computer}")
    if user==computer:
        print("draw")
    else:
        if user+computer in [3,6,7,8]:
            print("user wins")
        else:
            print("computer wins")
def main():
    generate()
if __name__ == '__main__':
   main()
