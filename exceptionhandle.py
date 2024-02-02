x = 5
y = 0
# y = 2

try:
    result = x/y
    print(result)
except Exception as e :
    print("Exceptions ",e)

finally:
    print("Exception Handled.")