
#Maliha Tasnim
#MALIHA.TASNIM64@myhunter.cuny.edu
#Date: November 1, 2022
#This program does stuff

print("Pick an integer in [0, 100] in your mind.")
def guess (l,r,num):
    resp = (l+r)//2
    print("Guess " + str(num) + ": is it " + str(resp) + "?")  
    print("1. too small   2. too big  3. just right")

    feedback = int(input("Enter choice 1-3: "))

    while feedback != 1 and feedback != 3 and feedback != 2: 
        feedback = int(input("Enter choice 1-3: "))
    
    if feedback == 1:
        guess(resp+1,r,num+1)

    if feedback == 2: 
        guess(l,resp-1,num+1)

    if feedback == 3:
        print(f"Congratulations! The answer is {resp}")
def main ():
    guess(0,100,1)

main() 