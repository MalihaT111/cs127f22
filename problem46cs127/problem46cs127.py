#Maliha Tasnim
#MALIHA.TASNIM64@myhunter.cuny.edu
#Date: October 24, 2022
#This program does stuff
def isPerfect(num):
    factors= []
    total = 0 
    if num <= 0 :
        return False
    else:
        for i in range(1,int((num/2)+1)):
            if num%i == 0:
                factors.append(i)             
    total = sum(factors)
    if total == num :
        return True
    else: 
        return False


        
def main():
    num = int(input("Enter a perfect number: "))
    while isPerfect(num) == False:
        num = int(input((f"{num} is not a perfect number. Re-enter: ")))
    else:
        print(f"Congratulations! {num} is a perfect number.")
        
main()
    