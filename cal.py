first_num = input("enter first number:")
second_num = input("enter second number:") 
first = float(first_num)
second = float(second_num)
operation = input("which one do you want[add/subtract/multiply/divide]")
if operation == 'add':
    final = first + second 

elif operation == 'subtract':
    final = first - second

elif operation == 'multiply':
    final = first * second

elif operation == 'divide':
    final = first / second

else : print("check your your spelling dumbass")   

print(final)