operations = ['3801 - 2', '123 + 49']

def arithmetic_arranger(problems, showResult=False):
    # Checking the lenght of the problems
    if len(problems) > 5:
        return "Error: Too many problems."
    else:
        firstLine = ''
        secondLine= ''
        dashes = ''
        results = ''
        for operation in range(0, len(problems)):
            [firstItem, operator, secondItem] = problems[operation].split(" ")
            # Checking if the numbers has the max of 4 digits
            if len(firstItem) > 4 or len(secondItem) > 4:
                return "Error: Numbers cannot be more than four digits."
            # Checking if the numbers are numerics
            elif firstItem.isnumeric() == False or secondItem.isnumeric() == False:
                return "Error: Numbers must only contain digits."
            # Checking if the operator is equal to '+' or '-'
            elif operator != '+' and operator != '-':
                return "Error: Operator must be '+' or '-'."
            # Adding the spaces
            # If the length of the first and second operand are equal
            if len(firstItem) == len(secondItem):
                firstItem = firstItem.rjust(len(firstItem) + 2, " ")
                secondItem = secondItem.rjust(len(secondItem) + 1, " ")
            # If the first operand is greatter than the second operand
            elif len(firstItem) > len(secondItem):
                space = len(secondItem) + 1 + (len(firstItem) - len(secondItem))
                secondItem = secondItem.rjust(space, " ")
                firstItem = firstItem.rjust(len(firstItem) + 2, " ")
            # If the second operand is greatter than the first operand
            elif len(secondItem) > len(firstItem):
                space = len(firstItem) + 2 + (len(secondItem) - len(firstItem))
                firstItem = firstItem.rjust(space, " ")
                secondItem = secondItem.rjust(len(secondItem) + 1, " ")
            # Creating the dashes line
            dash = ''
            while len(dash) != len(firstItem):
                dash = dash + "-"
            # Calculating the result
            if operator == "+":
                result = str(int(firstItem) + int(secondItem))
            elif operator == "-":
                result = str(int(firstItem) - int(secondItem))
            # Adding the spaces to the result
            space = len(result) + (len(firstItem) - len(result))
            result = result.rjust(space, " ")
            secondItem = operator + secondItem
            # Adding to the strings
            if (operation + 1) != len(problems):
                firstLine += firstItem  + "    "
                secondLine += secondItem  + "    "
                dashes += dash + "    "
                results += result + "    "
            else: 
                firstLine += firstItem 
                secondLine += secondItem 
                dashes += dash
                results += result
        # Returning the result
        firstLine.rstrip()
        secondLine.rstrip()
        dashes.rstrip()
        results.rstrip()
        if showResult==False:
            finalResult = firstLine + "\n" + secondLine + "\n" + dashes
        elif showResult==True:
            finalResult = firstLine + "\n" + secondLine + "\n" + dashes + "\n" + results
    return finalResult
                
result = arithmetic_arranger(operations, True)
print(result)