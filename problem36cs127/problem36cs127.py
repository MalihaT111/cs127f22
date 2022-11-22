#Maliha Tasnim
#MALIHA.TASNIM64@myhunter.cuny.edu
#Date: October 15, 2022
#This program does stuff
def computePrice(liquid,size):
    if liquid == 'coffee':
        if size == 'small':
            print("small size coffee: 2.5")
            return 2.5
        if size == 'medium':
            print("medium size coffee: 2.75")
            return 2.75
        if size == 'large':
            print('large size coffee' + '3.0')
            return 3.0
        if size != 'small' and size != 'medium' and size != 'large':
            return -1
    if liquid == 'misto':
        if size == 'small':
            print("small size misto: 3.15")
            return 3.15
        if size == 'medium':
            print("medium size misto: 3.35")
            return 3.35
        if size == 'large':
            print("large size misto: 3.7")
            return 3.7
        if size != 'small' and size != 'medium' and size != 'large':
            return -1
    if liquid == 'mocha':
        if size == 'small':
            print("small size mocha: 3.5")
            return 3.5
        if size == 'medium':
            print("medium size mocha: 3.8")
            return 3.8
        if size == 'large':
            print("large size mocha: 4.25")
            return 4.25
        if size != 'small' and size != 'medium' and size != 'large':
            return -1
    if liquid == 'tea':
        if size == 'small':
            print("small size tea: 2.35")
            return 2.35
        if size =='medium':
            print("medium size tea: 2.45")
            return 2.45
        if size == 'large':
            print("large size tea: 2.9")
            return 2.9
        if size != 'small' and size != 'medium' and size != 'large':
            return -1
    if liquid != 'coffee' and liquid != 'misto' and liquid != 'mocha' and liquid != 'tea':
        return -1
    #computePrice("coffee","small")