# Ai Assignment 41 - Construct Asterisk Pattern, Using a Nested For Loop
def c(a):
    for b in range(a):
        print ('* ', end='')
    print('')
for a in range(5):
    c(a)
for a in range(5, 0, -1):
    c(a)