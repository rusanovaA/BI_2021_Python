print("Hello! This is the best Unit Converter of grams to various units of mass")
print("You can choose the following units: ")
print("Drachma", "Mina", "Talent", "Shekel", "Uns", "Berkovets", "Dyne")
unit = input("Please, enter the unit: ")
gramm_value = int(input("Enter the value of grams: "))
if unit == 'Drachma':
    print(gramm_value * 0.29411764705882)
    print("Drachma is an ancient Greek unit of weight")
elif unit == 'Mina':
    print(gramm_value * 0.0023201856148492)
    print("Mina is an ancient Greek unit of mass")
elif unit == 'Talent':
    print(gramm_value * 0.000049019607843137)
    print("It is an ancient Greek unit of mass")
elif unit == 'Shekel':
    print(gramm_value * 0.087565674255692)
    print("It is an ancient Near Eastern unit of weight")
elif unit == 'Uns':
    print(gramm_value * 0.035838440311078)
    print("Uns is one of the oldest Swedish weight measurement units")
elif unit == 'Berkovets':
    print(gramm_value * 0.0000061050061050061)
    print("Berkovets is one of the oldest Russian weight measurement units")
elif unit == 'Dyne':
    print(gramm_value * 980.67)
    print("Dyne is a unit of measurement for weight as well as force." +
          "One dyne is equal to 0.00001 newtons.")
print("Bye!")    
    
