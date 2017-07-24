"""
exersise3
"""
ii = 6

def myfactorial(i):
    """
    My factorial
    """
    if i == 0:
        return 1
    else:
        return i*myfactorial(i-1)

print (myfactorial(ii))

# teorema Pifagora
