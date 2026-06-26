def celcius_para_fahrenheit(celsius):
    fahrenheit = (celsius * 1,8 ) + 32
    return fahrenheit
print("--- CONVESOR DE TEMPERATURA ---")
c = float(input("DIGITE a temperatura em C: "))
print(F" A temperatura correspondente é: {celcius_para_fahrenheit(c)}")