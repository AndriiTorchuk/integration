"""
ex5
"""
one = 1
two = 2
num = 3
text = "One is {0} and two is {1}".format(one, two)

def clice_test(text, num):
    """
    slise_text function taskes string parameter `text` and integer `num` 
    """
    return text[0:num]

print(clice_test(text, num))
