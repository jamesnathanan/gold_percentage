




def turn_965_to_750():

    alloy_factor_965_to_750 = (9.65 / 7.5) - 1.0 #turn 96.5 % gold to 18K (75%) gold
    user_amount = input("Amount of your 96.5% gold : (gram)") #ask user amount of their gold
    alloy_to_add = alloy_factor_965_to_750 * float(user_amount)
    print("You need to add more alloy: \n", alloy_to_add)
    total_amount = float(user_amount) + float(alloy_to_add)
    print("\n And your total amount of your 18K gold will be : \n", total_amount)

def turn_965_to_583():

    alloy_factor_965_to_583 = (9.65/ 5.83) - 1.0
    user_amount = input("Amount of your 96.5% gold : (gram)")
    alloy_to_add = alloy_factor_965_to_583 * float(user_amount)
    print("You need to add more alloy: \n", alloy_to_add)
    total_amount = float(user_amount) + float(alloy_to_add)
    print("\n And your total amount of your 14K gold will be : \n", total_amount)


def turn_900_to_750():

    alloy_factor_900_to_750 = (9.00/ 7.50) - 1.00
    user_amount = input("Amount of your 90% gold : (gram)")
    alloy_to_add = alloy_factor_900_to_750 * float(user_amount)
    print("You need to add more alloy: \n", alloy_to_add)
    total_amount = float(user_amount) + float(alloy_to_add)
    print("\n And your total amount of your 18K gold will be : \n", total_amount)

def turn_900_to_583():

    alloy_factor_900_to_583 = (9.00/ 5.83) - 1.0
    user_amount = input("Amount of your 90% gold : (gram)")
    alloy_to_add = alloy_factor_900_to_583 * float(user_amount)
    print("You need to add more alloy: \n", alloy_to_add)
    total_amount = float(user_amount) + float(alloy_to_add)
    print("\n And your total amount of your 14K gold will be : \n", total_amount)


turn_900_to_583()

#turn_965_to_750()
#turn_965_to_583()

