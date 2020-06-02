water = int(input("Write how many ml of water the coffee machine has:"))
milk = int(input("Write how many ml of milk the coffee machine has:"))
beans = int(input("Write how many grams of coffee beans the coffee machine has:"))
cups = int(input("Write how many cups of coffee you will need:"))

water_needed = water//400
milk_needed = milk//540
beans_needed = beans//120
cups_needed= cups//9

max_cups = min([water_needed, milk_needed, beans_needed])

extra = max_cups - cups
if max_cups == cups:
    print("Yes, I can make that amount of coffee")
elif max_cups > cups:
    print(f"Yes, I can make that amount of coffee and even {extra} more than that")
elif max_cups < cups:
    print(f"No, I can make only {max_cups} cups of coffee")
    
    
    *the code is not finished. i am working on the rest and will submit the rest of the code
