from art import text2art
from pathlib import Path


character_list = ['1','2','3','4','5','6','7','8','9','0','q','w','e','r','t','a','s','d','f','g','z','x','c','v','b','y','u','i','o','p','h','j','k','l',';','n','m',',','.','/',]

def ascii_gen(character_list):

    ascii_characters = {}
    for i in range(len(character_list)):
        ascii_characters[character_list[i]] = text2art(character_list[i])

    cwd = Path.cwd()
    path = cwd / 'ascii' / 'ascii_characters.py'
    path.resolve()

    path.write_text(f"ascii_characters = {str(ascii_characters)}")
