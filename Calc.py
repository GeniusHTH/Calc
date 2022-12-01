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

info = '''

    +	 Addition	      = x + y	
    -	 Subtraction	      = x - y	
    *	 Multiplication       = x * y	
    /	 Division	      = x / y	
    %	 Modulus	      = x % y	
    ** Exponentiation	      = x ** y	
    // Floor division	      = x // y
  MODULUS: Remainder of a number after Division.
  FLOOR DIVISION: The floor division // rounds the result down to the nearest whole number.
  EXPONENTIATION: If x=2 and y=5, the exponent of 2**5 is the same as 2*2*2*2*2, which is equals to 32.

'''

print(message)
print('You can type Help for tips or Stop to exist The program')

while True:  
  selecting_operator = input('Select Operator: ')
  if selecting_operator.lower() == 'help':
    print(info)
    print('You can visit https://www.w3schools.com/python/python_operators.asp To learn more about Python Operators.')
  elif selecting_operator == "+":
    def addition(num1,num2):
      add = num1 + num2
      return add
    num1 = input('[+] num: ')
    num2 = input('[+] num: ')
    print(addition(num1=float(num1),num2=float(num2)))
  elif selecting_operator == "-":
    def substraction(num1,num2):
      sub = num1 - num2
      return sub
    num1 = input('[-] num: ')
    num2 = input('[-] num: ')
    print(substraction(num1=float(num1),num2=float(num2)))
  elif selecting_operator == "*":
    def multiply(num1,num2):
      mult = num1 * num2
      return mult
    num1 = input('[*] num: ')
    num2 = input('[*] num: ')
    print(multiply(num1=float(num1),num2=float(num2)))
  elif selecting_operator == "/":
    def division(num1,num2):
      dev = num1 / num2
      return dev
    num1 = input('[/] num: ')
    num2 = input('[/] num: ')
    print(division(num1=float(num1),num2=float(num2)))
  elif selecting_operator == "%":
    def modulus(num1,num2):
      mod = num1 % num2
      return mod
    num1 = input('[%] num: ')
    num2 = input('[%] num: ')
    print(modulus(num1=float(num1),num2=float(num2)))
  elif selecting_operator == "**":
    def exponet(num1,num2):
      exp = num1 ** num2
      return exp
    num1 = input('[**] num: ')
    num2 = input('[**] num: ')
    print(exponet(num1=float(num1),num2=float(num2)))
  elif selecting_operator == "//":
    def floor_division(num1,num2):
      f_div = num1 // num2
      return f_div 
    num1 = input('[//] num: ')
    num2 = input('[//] num: ')
    print(floor_division(num1=float(num1),num2=float(num2)))
  elif selecting_operator.lower() == 'stop':
      break
