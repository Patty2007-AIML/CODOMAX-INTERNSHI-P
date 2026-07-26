name = input("Enter your name: ")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

def add(x, y):
    return x + y

print("Hello,", name)
print("Addition:", add(a, b))
print("Subtraction:", a - b)
print("Multiplication:", a * b)

for i in range(1, 6):
    print(i)
