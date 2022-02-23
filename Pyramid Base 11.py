#Pyramid Base

x = 1
def funct(z):
    for x in range(1,z+1,2):
        n = (z-x)/2
        for y in range(int(n)):
            print(" ", end = "")
        for y in range(x):
            print("*", end = "" )
        print("")

funct(77)






