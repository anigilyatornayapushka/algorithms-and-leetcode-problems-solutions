answers = set()
answers_count = 0


def calc(ex, sol, ex_length, n, oper):
    global answers, answers_count

    if len(answers) >= answers_count:
        return
    try:
        if eval(ex) == sol:
            answers.add(ex)
            return
    except:
        ZeroDivisionError, SyntaxError
        
    
    for i in range(n, ex_length):
        new_ex = ex[:i] + oper + ex[i:]
        calc(new_ex, sol, len(new_ex), i+2, "+")
        calc(new_ex, sol, len(new_ex), i+2, "-")
        calc(new_ex, sol, len(new_ex), i+2, "*")
        calc(new_ex, sol, len(new_ex), i+2, "/")


def main():
    global answers_count

    ex = input('expression : ')
    sol = int(input('equalize to : '))
    answers_count = int(input('maximum count of answers : '))

    calc(ex, sol, len(ex), 1, "+")
    calc(ex, sol, len(ex), 1, "-")
    calc(ex, sol, len(ex), 1, "*")
    calc(ex, sol, len(ex), 1, "/")

    return list(answers)


print(main())