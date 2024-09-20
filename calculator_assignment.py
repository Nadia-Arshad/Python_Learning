

print("************Calculator************")

def add(x, y):
  return int(x + y)

def subtract(x, y):
  return int(x - y)

def multiply(x, y):
  return int(x * y)

def divide(x, y):
  if y == 0:
    return "Division not possible with zero."
  return int(x // y)

def my_calculator():
  
  print("""Options:
            1. Add
            2. Subtract
            3. Multiply
            4. Divide""")

  option = input("Enter your option (1 / 2 / 3 / 4): ")

  num1 = float(input("Enter the first number: "))
  num2 = float(input("Enter the second number: "))

  if option == '1':
    print(int(add(num1, num2)))
  elif option == '2':
    print(int(subtract(num1, num2)))
  elif option == '3':
    print(int(multiply(num1, num2)))
  elif option == '4':
    print(int(divide(num1, num2)))
  else:
    print("Choose an option to run the calculator")

my_calculator()