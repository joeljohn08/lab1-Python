Temperature = input ("Enter temperature:")
Temperature = float(Temperature)
unit = input (" Enter unit in F/f or C/c:")

if unit == "F" or unit == "f":
 C = (Temperature-32)*5/9
 print(f"{Temperature}° in Celsius is {C}° Fahrenheit.")
 
elif unit == "C" or unit == "c": 
 F = (Temperature*1.8)+32
 print(f"{Temperature}° in Celsius is {F}° Fahrenheit.")
  
else:
   print(f"Invalid Unit({unit})")