"""
Exercise 7
"""
# Create a file with name: file0 and write a text inside to the file1
som = open('file1', 'w')
som.write("One is {0} and two is {1}")
som.write("\n")
som.write("some text")
som.close()

# read file and close file1
read_som = open('file1', 'r')
content = read_som.readlines()
read_som.close()

# Print content of file1
print(content)
