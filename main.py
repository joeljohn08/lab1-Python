Temperature = input ("Enter Temperature:")
Temperature = float(Temperature)
unit = input ("Enter the Unit as F/f or C/c:")
if unit == "F" or unit == "f":
 F = (Temperature-32) * 1.8
 print(f"{Temperature}°Celsius is {F}° Fahrenheit.")
 
elif unit == "C" or unit == "c": 
 C = Temperature*1.8 + 32
 print(f"{Temperature}°Fahrenheit is {C}° Celsius.")
  
else:
   print(f"Invalid Unit({unit})")