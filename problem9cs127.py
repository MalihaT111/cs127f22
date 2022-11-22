#Maliha Tasnim
#MALIHA.TASNIM64@myhunter.cuny.edu
#Date: September 17, 2022
#This program encryptes a message based on given input + character shifts. 

inputstring = input("input: ")
shift = int(input("shift: "))
cipher = ""

for i in range (len(inputstring)):
    p = inputstring[i]
    if ord(p)+shift<123:
        cipher+= chr(ord(p)+shift)    
    else:
        #literally j visualize the cipher man... like if you rotate it u then add the remainder from a (97)
        cipher+=chr(97+((ord(p)+shift)-123))

print("ciphered string: "+ cipher)

