"""
ex7
"""

som = open('file1', 'w')
som.write("One is {0} and two is {1}") 
som.write("\n")
som.write("some text")
som.close()

read_som = open('file1', 'r')
content = read_som.readlines()
read_som.close()

print(content)

