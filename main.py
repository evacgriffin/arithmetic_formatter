# Program to arrange a list of arithmetic problems

def arithmetic_arranger(problems, solns=False):
    # Check for problem limit: 5 problems max
    if len(problems) > 5:
        return 'Error: Too many problems.'

    # Check for operators: only + or - allowed, each operand contains only digits,
    # and numbers contain at most 4 digits
    split_problems = []
    for problem in problems:
        split_problems.append(problem.split())

    for split_problem in split_problems:
        if '*' in split_problem or '/' in split_problem:
            return "Error: Operator must be '+' or '-'."
        if not split_problem[0].isdigit() or not split_problem[2].isdigit():
            return 'Error: Numbers must only contain digits.'
        if len(split_problem[0]) > 4 or len(split_problem[2]) > 4:
            return 'Error: Numbers cannot be more than four digits.'

    # Create the arranged return string
    line1 = ''
    line2 = ''
    line3 = ''
    # If solutions parameter passed in, create 4th line showing solutions
    if solns is True:
        line4 = ''
    for split_problem in split_problems:
        diff = abs(len(split_problem[2]) - len(split_problem[0]))
        if solns is True:
            if split_problem[1] == '+':
                soln = int(split_problem[0]) + int(split_problem[2])
            elif split_problem[1] == '-':
                soln = int(split_problem[0]) - int(split_problem[2])
            soln = str(soln)
            num_soln_digits = len(soln)
        line1 += '  '
        line2 += split_problem[1] + ' '

        if len(split_problem[0]) >= len(split_problem[2]):
            line1 += split_problem[0]
            for x in range(diff):
                line2 += ' '
            line2 += split_problem[2]
            for y in range(len(split_problem[0]) + 2):
                line3 += '-'
            if solns is True:
                soln_spaces = len(split_problem[0]) + 2 - num_soln_digits
                for z in range(soln_spaces):
                    line4 += ' '
                line4 += soln
        else:
            for x in range(diff):
                line1 += ' '
            line1 += split_problem[0]
            line2 += split_problem[2]
            for y in range(len(split_problem[2]) + 2):
                line3 += '-'
            if solns is True:
                soln_spaces = len(split_problem[2]) + 2 - num_soln_digits
                for z in range(soln_spaces):
                    line4 += ' '
                line4 += soln

        if split_problem != split_problems[-1]:
            line1 += '    '
            line2 += '    '
            line3 += '    '
            if solns is True:
                line4 += '    '

    line1 += '\n'
    line2 += '\n'
    if solns is True:
        line3 += '\n'

    arranged_problems = line1 + line2 + line3
    if solns is True:
        arranged_problems += line4

    return arranged_problems


if __name__ == '__main__':
    print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
    print(arithmetic_arranger(['3801 - 2', '123 + 49']))
    print(arithmetic_arranger(['1 + 2', '1 - 9380']))
    print(arithmetic_arranger(['3 + 855', '3801 - 2', '45 + 43', '123 + 49']))
    print(arithmetic_arranger(['11 + 4', '3801 - 2999', '1 + 2', '123 + 49', '1 - 9380']))
    print(arithmetic_arranger(['44 + 815', '909 - 2', '45 + 43', '123 + 49',
          '888 + 40', '653 + 87']))
    print(arithmetic_arranger(['3 / 855', '3801 - 2', '45 + 43', '123 + 49']))
    print(arithmetic_arranger(['24 + 85215', '3801 - 2', '45 + 43', '123 + 49']))
    print(arithmetic_arranger(['98 + 3g5', '3801 - 2', '45 + 43', '123 + 49']))
    print(arithmetic_arranger(['3 + 855', '988 + 40'], True))
    print(arithmetic_arranger(['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40'], True))
