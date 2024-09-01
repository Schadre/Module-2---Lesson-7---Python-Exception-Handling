"""
Exceptional Weather Forecast

Objective: The aim of this assignment is to enhance your 
understanding of exception handling by creating a weather 
forecast application that gracefully handles unexpected user 
input and provides user-friendly error messages.

Task 1: Start Begin by asking the user to enter the temperature in Fahrenheit.

Task 2: Temperature Conversion Write a function that converts the Fahrenheit 
temperature to Celsius. Remember that the formula is (Fahrenheit - 32) * 5/9.

Use a try block to catch any potential errors during the conversion process. 
What happens if they type out "thirty" instead of doing 30?

Task 3: User Experience Implement an else block that prints the converted 
temperature in a user-friendly format. 

Example: "100 degrees Fahrenheit is 37.78 degrees Celsius."

Task 4: Finally Add a finally block that thanks the user for using the weather 
forecast application, ensuring that this message is displayed regardless of 
whether an exception was caught or not.
"""

def temperature_conversion(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

while True:
    try: 
        fahrenheit_input = int(input("Please enter the temperature in Fahrenheit(2 decimals max or whole numbers): "))
        temperature_celsius = round(temperature_conversion(fahrenheit_input), 2)
        print(f"The conversion of Fahrenheit to Celsius is {temperature_celsius}")
    except ValueError:
        print("Please only use integers or floats when entering the Fahrenheit.")
    finally:
        print("Thank you for using the weather forecast application")
    try: 
        fahrenheit_input_float = float(input("Please enter the temperature in Fahrenheit(2 decimals max or whole numbers): "))
        temperature_celsius = round(temperature_conversion(fahrenheit_input_float), 2)
        print(f"The conversion of Fahrenheit to Celsius is {temperature_celsius}")
    except ValueError:
        print("Please only use integers or floats when entering the Fahrenheit.")
    finally:
        print("Thank you for using the weather forecast application")

    continue_input = input("Would you like to continue? (yes/no)")
    if continue_input != 'yes':
        break
    