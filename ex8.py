"""
ex8
"""

myname = input("Wtat is your name?")
myplace = input("Where are your from?")

if (myplace == "kp"):
    newfunc = open ('file2', 'w')
    newfunc.write("I am also from kp))")
    newfunc.close()
    print(myplace)

print(myname)
print(myplace)





