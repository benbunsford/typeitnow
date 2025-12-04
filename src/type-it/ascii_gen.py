from art import text2art
from pathlib import Path
from ascii.words import long_words, medium_words, short_words

#character_list = ['1','2','3','4','5','6','7','8','9','0','q','w','e','r','t','a','s','d','f','g','z','x','c','v','b','y','u','i','o','p','h','j','k','l',';','n','m',',','.','/',]

def ascii_gen(*args):

    ascii_characters = {}
    for arg in args:
        for i in range(len(arg)):
            ascii_characters[arg[i]] = text2art(arg[i])

    cwd = Path.cwd()
    path = cwd / 'ascii' / 'ascii_characters.py'
    path.resolve()

    path.write_text(f"ascii_characters = {str(ascii_characters)}")

ascii_gen(long_words, medium_words, short_words)
