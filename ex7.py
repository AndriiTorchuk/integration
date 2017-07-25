"""
ex7
"""

print ("how old are you?"),
age = raw_input()
print ("You are {0}".format(age))
text = "some {0} text {1}".format(1, 2)

som = open('file1', 'w')
som.write(text ="some {0} text {1}".format(1, 2)) 
som.write("\n")
som.write(print(text))
som.close()

read_som = open('file1', 'r')
content = read_som.readlines()
read_som.close()

print(content)

