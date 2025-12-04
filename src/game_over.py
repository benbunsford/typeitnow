
def game_over(key, pressed_key, score):
    print(f"You typed '{pressed_key}'.")
    print(f"The right answer was '{key}'.")
    if score == 1:
        print(f"You survived {score} round.")
    else:
        print(f"You survived {score} rounds.")
    if 50 < score < 100:
        print("Bet you can't make it to 100. :)")
    elif score > 100:
        print(f"Bet you can't make it to {score + 1}. ;)")
