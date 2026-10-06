def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


if __name__ == "__main__":
    celsius = 25
    fahrenheit = celsius_to_fahrenheit(celsius)

    print(f"{celsius}°C is {fahrenheit:.1f}°F")
    print(f"{fahrenheit}°F is {fahrenheit_to_celsius(fahrenheit):.1f}°C")
