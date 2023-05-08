class Math:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        return x / y

    def power(self, x, y):
        return x ** y


class Physics:
    def velocity(self, distance, time):
        return distance / time

    def acceleration(self, velocity_final, velocity_initial, time):
        return (velocity_final - velocity_initial) / time

    def force(self, mass, acceleration):
        return mass * acceleration

    def work(self, force, distance):
        return force * distance

    def power(self, work, time):
        return work / time


# Ask user for class and operation
class_name = input("Enter 'math' or 'physics': ")
operation_name = input(
    "Enter operation (add, subtract, multiply, divide, power for math; velocity, acceleration, force, work, power for physics): ")

# Create instance of selected class
if class_name == 'math':
    calc = Math()
elif class_name == 'physics':
    calc = Physics()
else:
    print("Invalid class name")
    exit()

# Call selected operation and print result
if hasattr(calc, operation_name):
    operation = getattr(calc, operation_name)
    if operation_name == 'power':
        x = float(input("Enter base: "))
        y = float(input("Enter exponent: "))
        result = operation(x, y)
    else:
        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        result = operation(x, y)
    print(f"Result: {result}")
else:
    print("Invalid operation name")
