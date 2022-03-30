class Subtract:

    def finddifference(self, a, b):
        s = a - b
        return s

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))

obj = Subtract()
s = obj.finddifference(a, b)

print("Difference is:", s)