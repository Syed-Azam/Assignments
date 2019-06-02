# Ai Assignment 42 - Construct Numbers Pattern-1, Using a Nested For Loop
def c(a):
    for b in range(a):
        print (str(b + 1)+" ", end='')
    print('')
for a in range(5):
    c(a)
for a in range(5, 0, -1):
    c(a)