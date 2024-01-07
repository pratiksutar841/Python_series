num1 = int(input("Enter number 1 : "))
num2 = int(input("Enter number 2 : "))

operator = input("Enter operator : ")

match operator:
          case "+":
                print("Sum is ",num1+num2)
          case "-":
                print("Subis ",num1-num2)
          case "*":
                print("Mul is ",num1*num2)
          case "/":
                print("Div is ",num1/num2)      
          case _ :
                print("Invalid Operator")                  