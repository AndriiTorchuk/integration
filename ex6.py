"""
Exercise 6
"""
# Some of exceptions
try:
    result = 1 / 0
except ZeroDivisionError:
    print ("wow, an error happened!")
except OSError:
    pass

# Create a file with name: file0 and write a text inside to the file0
file_handler = open('file0', 'w')
file_handler.write("some  text goes here")
file_handler.close()

# read file and close file0
read_file_handler = open('file0', 'r')
content = read_file_handler.readlines()
read_file_handler.close()

# Print content of file0
print(content)
