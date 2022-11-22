#Maliha Tasnim
#MALIHA.TASNIM64@myhunter.cuny.edu
#Date: September 26, 2022
#This program does stuff, hw25

string = input("Enter a string with 0 or 1 only: ")
num = 0
base = 2
weight = 1
length = len(string)
#ch = " "
for i in string[::-1]:
    ch = i 
    if ch == '1':
         num +=weight
    elif ch != '0':
        print("Letter",ch, "is not allowed in binary string.")
        exit()
    weight *= base
print("num ", num)

# input a string, put in variable string
# set num to be 0
# set base to be the base of binary number
# initialize weight to be 1, for the least significant digit
# set length to be the number of letters of string

# Move i from the rightmost index downto the leftmost index
#     put ith letter of string to variable ch 
#     if ch is '1'
#          increase num by weight 
#     otherwise, if ch is not '0'
#          print that Letter ch is not allowed in a binary string
#          call exit method to exit current program
#     #num is not updated when ch is '0'

#     update weight by multiplying it with base 

# print out num followed by prompt "num ="