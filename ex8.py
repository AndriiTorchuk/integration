"""
Exercise 8
"""
# Some question
myname = input("Wtat is your name?")
myplace = input("Where are your from?")

# if statemant is true create a file file2 and write some information
if (myplace == "kp"):
    newfunc = open ('file2', 'w')
    newfunc.write("I am also from kp))")
    newfunc.close()
    print(myplace)

print(myname)
print(myplace)
