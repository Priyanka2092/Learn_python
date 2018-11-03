import random

print('\nCalculator function starts below\n')


def add(num1, num2):
    print('Adding...\n')
    z = num1 + num2
    print('The sum of two numbers is: ' + str(z))


def sub(num1, num2):
    print('Subtracting...\n')
    z = num1 - num2
    print('The difference of two numbers is: ' + str(z))


def mult(num1, num2):
    print('Multiplying...\n')
    z = num1 * num2
    print('The multiplication of two numbers is: ' + str(z))


def div(num1, num2):
    print('Dividing...\n')
    z = num1 / num2
    print('The Division of two numbers is: ' + str(z))


def main():
    cond1 = 1
    while cond1 == 1:
        cond = 1
        while cond == 1:
            try:
                x = int(input('The first no is X = '))
                y = int(input('\nThe second no is Y = '))
                # oper=random.randint(1,4)
                oper = int(input('\nwhich operation do you want to perform?\n'))
                # print(oper)
                cond = 0
            except:
                print("\ninvalid data type. Try again")

        if (oper == 1):
            add(x, y)

        elif (oper == 2):
            sub(x, y)

        elif (oper == 3):
            mult(x, y)

        elif (oper == 4):
            div(x, y)

        else:
            print("\nwrong operation")
        oper1 = input('\nDo you want run it once more?')

        if (oper1 == y):
            cond1 = 1
        else:
            print('end of the program!')
            cond1 = 0


if __name__ == "__main__":
    main()

