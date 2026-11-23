# Temperature Converter Project

def c_to_f(c):
    return (c * 9/5) + 32


def f_to_c(f):
    return (f - 32) * 5/9


def c_to_k(c):
    return c + 273.15


# Main program
print("===== TEMPERATURE CONVERTER =====")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Celsius to Kelvin")

choice = int(input("Enter your choice: "))

if choice == 1:
    c = float(input("Enter Celsius: "))
    print("Result:", c_to_f(c), "Fahrenheit")

elif choice == 2:
    f = float(input("Enter Fahrenheit: "))
    print("Result:", f_to_c(f), "Celsius")

elif choice == 3:
    c = float(input("Enter Celsius: "))
    print("Result:", c_to_k(c), "Kelvin")

else:
    print("Invalid choice!")