

from math import floor
from random import randint


def find_a_number(lowest, highest, answer):
    
    guess = lowest + floor((highest - lowest) / 2)
    
    while (guess != answer):
        
        print({
            "lowest": lowest, 
            "highest": highest, 
            "answer": answer,
            "guess": guess
        })

        if guess > answer:
            highest = guess
            guess = lowest + floor((highest - lowest) / 2)

        if guess < answer:
            lowest = guess
            guess = lowest + floor((highest - lowest) / 2)

    print({
        "lowest": lowest, 
        "highest": highest, 
        "answer": answer,
        "guess": guess
    })

find_a_number(-100000, 100000, randint(-100000, 100000))