
try:
    result = 1 / 0
except ZeroDivisionError:
    print ("wow, an error happened!")
except OSError:
    pass


file_handler = open('filename','w')
file_handler.write("some  text goes here")
file_handler.close()

read_file_handler = open('filename','r')
content = read_file_handler.readlines()
read_file_handler.close()

print(content)
