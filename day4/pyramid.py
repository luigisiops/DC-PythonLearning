
def pyramid(n,char):
    ##need something to monitor spacing 
    ## 2n + 1 gives you number of starts
    ## n is number of rows we want which refers to left side spacing
    for i in range(0, 9):
        formula = 2*(i) + 1
        print(" " * (n-i) + (formula * char))

pyramid(9,"*")