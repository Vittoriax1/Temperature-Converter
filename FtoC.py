def convert_f_to_c(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return round(celsius, 2)

def convert_c_to_f(celsius):
    fah = (cel *9/5) + 32
    return round(fah, 2)

def convert_f_to_k(fahrenheit):
    kelvin = (fahrenheit + 459.67) * 5/9
    return round(kelvin, 2)

def convert_c_to_k(celsius):
    kelvin = celsius + 273.15
    return round(kelvin, 2)

def convert_k_to_f(kelvin):
    fahrenheit = (kelvin * 9/5) - 459.67
    return round(fahrenheit, 2)

def convert_k_to_c(kelvin):
    celsius = kelvin - 273.15
    return round(celsius, 2)

while True:
    print("")
    print("Temp Converter  ")
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenheit")
    print("3. Fahrenheit to Kelvin")
    print("4. Kelvin to Fahrenheit")
    print("5. Celsius to Kelvin")
    print("6. Kelvin to Celsius")
    print("0. Exit")
    print("")
    selection = input("Which would you like to convert?  ")

    try:
        selection = int(selection)
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        continue

    if selection == 1:
        try:
            fahrenheit = float(input("Please enter the temperature in Fahrenheit:  "))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            continue
        if fahrenheit < -459.67:
            print("Invalid input. Fahrenheit temperatures must be greater than -459.67.")
            continue
        temp_in_cels = convert_f_to_c(fahrenheit)
        print(f"{fahrenheit} degrees Fahrenheit is equivalent to {temp_in_cels} degrees Celsius.")
            
    elif selection == 2:
        try:
            cel = float(input("Please enter the temperature in Celsius:  "))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            continue
        if cel < -273.15:
            print("Invalid input. Celsius temperatures must be greater than -273.15.")
            continue
        temp_in_fah = convert_c_to_f(cel)
        print(f"{cel} degrees Celsius is equivalent to {temp_in_fah} degrees Fahrenheit.")

    elif selection == 3:
        try:
            fahrenheit = float(input("Please enter the temperature in Fahrenheit:  "))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            continue
        if fahrenheit < -459.67:
            print("Invalid input. Fahrenheit temperatures must be greater than -459.67.")
            continue
        temp_in_kelvin = convert_f_to_k(fahrenheit)
        print(f"{fahrenheit} degrees Fahrenheit is equivalent to {temp_in_kelvin} degrees Kelvin.")
        
    elif selection == 4:
        try:
            kelvin = float(input("Please enter the temperature in Kelvin:  "))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            continue
        if kelvin < 0:
            print("Invalid input. Kelvin temperature must be greater than 0.")
            continue
        temp_in_fahrenheit = convert_k_to_f(kelvin)
        print(f"{kelvin} degrees Kelvin is equivalent to {temp_in_fahrenheit} degrees Fahrenheit.")

    elif selection == 5:
        try:
            celsius = float(input("Please enter the temperature in Celsius:  "))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            continue
        if celsius < -273.15:
            print("Invalid input. Celsius temperatures must be greater than -273.15.")
            continue
        temp_in_kelvin = convert_c_to_k(celsius)
        print(f"{celsius} degrees Celsius is equivalent to {temp_in_kelvin} degrees Kelvin.")

    elif selection == 6:
        try:
            kelvin = float(input("Please enter the temperature in Kelvin:  "))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            continue
        if kelvin < 0:
            print("Invalid input. Kelvin temperature must be greater than 0.")
            continue    
        temp_in_celsius = convert_k_to_c(kelvin)
        print(f"{kelvin} degrees Kelvin is equivalent to {temp_in_celsius} degrees Celsius.")

    elif selection == 0:
        break    
            
    else:
        print("This was an invalid response. Please try again")

        response = input("Do you want to continue converting temperatures? (Y/N)  ")

        if response != "Y":
            break
