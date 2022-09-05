
def f_to_c(f):
    return (float(f) - 32) * 5/9

def c_to_f(c):
    return float(c) * 9/5 + 32

def c_to_k(c):
    return float(c) + 273.15

def k_to_c(k):
    return float(k) - 273.15

input_type = input("Is your temperature measured in celcius, fahrenheit, or kelvin?\n" )
temp = input("What is the temperature?\n")
output_type = input("Would you like to convert to celcius, fahrenheit, or kelvin?\n")

if input_type == "celcius" and output_type == "fahrenheit":
    print(f"Your new temperature is {c_to_f(temp)} degrees fahrenheit.")
elif input_type == "fahrenheit" and output_type == "celcius":
    print(f"Your new temperature is {f_to_c(temp)} degrees celcius.")
elif input_type == "celcius" and output_type == "kelvin":
    print(f"Your new temperature is {c_to_k(temp)} degrees kelvin.")
elif input_type == "kelvin" and output_type == "celcius":
    print(f"Your new temperature is {k_to_c(temp)} degrees celcius.")
else:
    print("The requested converter is currently unavailable :(")