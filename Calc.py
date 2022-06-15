
#Asking User For Their Input
from numpy import double


message = """
                          *
                        *   *
                       *     *
                      *       *
                     *         *
                    *           *
                   *             *
                  *               *
                  *               *
                   *             *
                    *           *   |    | ----- |    |
                     *         *    |    |   |   |    |
                      *       *     |----|   |   |----|
                        *   *       |    |   |   |    |
                          *         |    |   |   |    |
                      
"""
print(message)
while True:
    user_input = input("Please input the operator you want to use (Input'Stop' without the '' to Quit the program): ")
    if user_input == "+":
#Asking for their first number(int() converting it to int numbers )
      firstadd_num= input("num: ")
      secondadd_num = input("num: ")
    #adding the number
      Total = double(firstadd_num) + double(secondadd_num)
      print(Total)
    elif user_input == "-":
    #firstmin_num = first minus number 
      firstmin_num = input("num: ")
      secondmin_num = input("num: ")
    #minusing numbers
      result1 = double(firstmin_num) - double(secondmin_num)
      print(result1)
    elif user_input == "*":
      firstmulti_number = input("num: ")
      secondmulti_number = input("num: ")
      total2 = double(firstmulti_number) * double(secondmulti_number)
      print(total2)
    elif user_input == "/":
      print('Answers In This Operator Are Rounded Up')
      firstdiv_number = input("num: ")
      seconddiv_number = input("num: ")
      total3 = double(firstdiv_number) / double(seconddiv_number)
      print(round(total3))
    elif user_input == 'Stop' or 'stop':
      break
    else:
      print("Wrong input Entered...\n Try Again.")