def check_parentheses(expression :
str, openskob : chr = '(' , closeskob : chr = ')' ) :

    close = 0
    open = 0
    ans = True

    for char in expression :
            if char == openskob :
                open += 1
            elif char == closeskob :
                close -= 1
            if (close + open) < 0 :
                ans = False
                break

    if (close + open != 0) :
        ans = False

    print(ans)
    return(ans)

z = ''
check_parentheses(z, '<' , '>')


