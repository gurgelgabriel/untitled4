menu = int(input("press 1 for quick Pytagoras, 2 for tip calculator, 3 for temperature converter?")) # ask you what of the functions you want to use
if menu == 1:  # in case you choose function "quick Pytagoras"
    side_1 = int(input("first side"))  # ask you the size of yor first side in numbers
    side_2 = int(input("second side")) # ask you the size of the second side in numbers
    lengh_h = (side_1 ** 2 + side_2 ** 2) ** (1 / 2) # formula to discover your hypotenuse size
    print(round(lengh_h, 2))  # prints for you your hypotenuse size, round it for two decimal places
if menu == 2:  # in case you choose function "tip calculator"
    bill_amount = int(input("whats the bill?"))  # asks you what is your bill in number
    tip_percentage = int(input("whats the percentage?")) # ask you the tip percentage in number
    tip_amount = (bill_amount * (1 + tip_percentage / 100)) % bill_amount  # formula to discover your tip price
    print(tip_amount) # print your tip price
if menu == 3:  # in case you choose function "temperature converter"
    temperature_type = int(input("if you have celsius type 1/ if fahrenheit type 2?"))  # ask what scale do you already have
    temperature_magnitude = int(input("whats your temperature magnitude?"))  # ask you what the numeric value you already have
    if temperature_type == 1:  # if you already had celsius
        print((temperature_magnitude * 1.8 + 32))  # formula to convert celsius to fahrenheit
    if temperature_type == 2:  # if you already have fahrenheit
        print((temperature_magnitude - 32) / 1.8) # formula to convert fahrenheit to celsius
