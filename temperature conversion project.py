# Temperature Conversion Program (Loop with Auto-Detection)

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def kelvin_to_celsius(k):
    return k - 273.15

print("--- Temperature Conversion Tool ---")
print("Enter temperature with unit (e.g., 25C, 77F, 300K)")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("Enter temperature: ").strip().upper()
    
    if user_input == "EXIT":
        print("Goodbye! 👋")
        break

    # Extract value and unit
    try:
        temp_value = float(user_input[:-1])  # all except last char
        unit = user_input[-1]  # last char is the unit
    except ValueError:
        print("❌ Invalid input format. Use like 25C, 77F, or 300K.")
        continue

    # Conversion logic
    if unit == "C":
        f = celsius_to_fahrenheit(temp_value)
        k = celsius_to_kelvin(temp_value)
        print(f"{temp_value}°C = {f:.2f}°F = {k:.2f}K")

    elif unit == "F":
        c = fahrenheit_to_celsius(temp_value)
        k = celsius_to_kelvin(c)
        print(f"{temp_value}°F = {c:.2f}°C = {k:.2f}K")

    elif unit == "K":
        c = kelvin_to_celsius(temp_value)
        f = celsius_to_fahrenheit(c)
        print(f"{temp_value}K = {c:.2f}°C = {f:.2f}°F")

    else:
        print("❌ Invalid unit. Use C for Celsius, F for Fahrenheit, or K for Kelvin.")