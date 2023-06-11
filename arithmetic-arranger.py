"""
SECTION: FUNCTIONS
"""

# FUNCTION: Arithmetic Arranger
def arithmetic_arranger(problems, displayAnswers = False):
    if validationCheck(problems):
        equationLine1 = ""
        equationLine2 = ""
        dashLine = ""
        total = ""

        for index, problem in enumerate(problems):
            try:
                # Variable declarations
                equation = problem.split()
                num1 = int(equation[0])
                num1Length = len(equation[0])
                num2 = int(equation[2])
                num2Length = len(equation[2])
                operator = equation[1]
            except:
                print("ERROR: Numbers must only contain digits.")
                return ""

            extraSpaceLine1 = ""
            extraSpaceLine2 = ""
            extraSpaceTotal = ""
            dashes = ""
            spaceBetweenEquations = ""

            # Compare the length of each number
            if num2Length > num1Length:
                totalLength = num2Length - num1Length
                extraSpaceLine1 = " " * totalLength
                dashes = "-" * (num2Length + 2)
            else:
                totalLength = num1Length - num2Length
                extraSpaceLine2 = " " * totalLength
                dashes = "-" * (num1Length + 2)

            if (index >= 0) and index < (len(problems) - 1):
                spaceBetweenEquations = " " * 4
            elif index == (len(problems) - 1):
                spaceBetweenEquations = "\n"
            else:
                spaceBetweenEquations = " " * 0

            # Construct strings that, when combined, will result in arranged output
            equationLine1 += "  " + extraSpaceLine1 + str(num1) + spaceBetweenEquations
            equationLine2 += operator + " " + extraSpaceLine2 + str(num2) + spaceBetweenEquations
            dashLine += dashes + spaceBetweenEquations

            if displayAnswers:
                # Perform operation
                match operator:
                    case "+":
                        totalAmount = str(add(num1, num2))
                    case "-":
                        totalAmount = str(subtract(num1, num2))
                
                extraSpaceTotal = " " * (len(dashes) - len(totalAmount))
                total += extraSpaceTotal + totalAmount + spaceBetweenEquations

        # Append combined strings to return variable
        # arranged_problems = equationLine1 + equationLine2 + dashLine + total
        arranged_problems = f"{equationLine1}{equationLine2}{dashLine}{total}"

        return arranged_problems
    
    else:
        return ""

#FUNCTION: Validation check
def validationCheck(problems):
    # Validation to check if 'problems' list contains up to 5 equations
    if len(problems) > 0 and len(problems) <= 5:
        # Validation to check if 'problems' list contains equations with invalid operators
        for problem in problems:
            equation = problem.split()

            # Validation to check if an equation has the correct operator
            if len(equation) == 3 and (equation[1] == "+" or equation[1] == "-"):
                if (len(equation[0]) > 0 and len(equation[0]) <= 4) and (len(equation[2]) > 0 and len(equation[2]) <= 4):
                    continue
                else:
                    print("ERROR: Numbers cannot be more than four (4) digits.")
                    return False
            elif len(equation) != 3:
                print("ERROR: Missing part of equation.")
                return False
            else:
                print("ERROR: Invalid operator. Operator must be '+' or '-'.")
                return False

        return True

    elif len(problems) > 5:
        print("ERROR: Too many problems. Limit of five (5) equations only.")

    else:
        print("ERROR: Not enough problems. Limit of five (5) equations only.")

    return False

#FUNCTIONS: Add & Subtract
def add(num1, num2):
  return num1 + num2

def subtract(num1, num2):
  return num1 - num2

"""
SECTION: MAIN
"""

# print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 + 491"], True))
# print(arithmetic_arranger(["32 + 698"]))