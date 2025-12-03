from user_prompt import select_difficulty, select_random_key, key_to_art
from ascii_gen import ascii_gen, character_list
from music import MusicPlayer
from game_over import game_over
from gametimer import GameTimer
import readchar
import sys

def main():
    print("Welcome to type-it! Press the correct key/button when prompted to score.\n")
    ascii_gen(character_list)
    difficulty = select_difficulty()


    player = MusicPlayer()
    player.play_async()
    player.speed_up()
    print(".\n" * 60)

    print(
"""
---------------------------------------
            !!! START !!!
---------------------------------------
"""
    )
    score = 0
    timer_length = 10
    while True:
        key = select_random_key(difficulty)
        ascii_key = key_to_art(key)
        print(ascii_key)

        pressed_key = None
        timer = GameTimer(timer_length, game_over, args=[key,pressed_key,score])
        timer.start()
        pressed_key = readchar.readkey()

        if pressed_key == key:
            timer.cancel()
            score += 1
            player.speed_up()
            timer_length -= .05
        else:
            game_over(key, pressed_key, score)
            player.stop()
            sys.exit()



if __name__ == "__main__":
    main()
