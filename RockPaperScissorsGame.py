import random

def display():
    print("Rock Paper Scissors Game")
    print('1. Rock')
    print("2. Paper")
    print("3. Scissors")
    print("4. Exit")
    
def game_logic(user, com):
    if user == com:
        return "Its a Tie"
    elif user == 1 and com == 2:
        return "Computer Win"
    elif user == 1 and com == 3:
        return "You Win"
    elif user == 2 and com == 1:
        return "Computer Win"
    elif user == 2 and com == 3:
        return "You Win"
    elif user == 3 and com == 1:
        return "Computer Win"
    elif user == 3 and com == 2:
        return "You Win"
    else:
        return "Invalid input"

def define_input(input):
    if input == 1:
        return "Rock"
    elif input == 2:
        return "Paper"
    elif input == 3:
        return "Scissors"
    else:
        return "Invalid"

user_score = 0
com_score = 0        
while True:
    print(f"Score: user: {user_score}  computer: {com_score}")
    display()
    user = int(input('Option: '))
    com = random.randint(1, 3)
    if user == 4:
        break
    print(f"User: {define_input(user)}  Computer: {define_input(com)}")
    result = game_logic(user, com)
    if result == "Computer Win":
        com_score += 1
    elif result == "You Win":
        user_score += 1
    print(result)
    print()
    