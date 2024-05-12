import random
def rollDice():
    dice_one = random.randint(1, 6)
    dice_two = random.randint(1, 6)
    sum = dice_one + dice_two
    if dice_one == dice_two:
        return str(sum * 2) + " double"
    return str(sum) + " sum"
        
print(rollDice())