Q6
# Many word puzzles can be solved by iterating through a list of words while checking for characteristics specified by the puzzle.
# A list of words word_list.txt is provided in Brightspace. The file has one word per line.
#
# A blueprint file is also provided in the file puzzles.py.
# Your overall goal is to implement the functions in this file and achieve the same output as below.
# You MUST NOT change the code in the main scope or the functions’ headers.

words = []

for word in words:
    """Find 5 uncapitalized, unhyphenated words that contain 9 of the letters of the alphabet from l to v ("lmnopqrstuv"). """
    result = []

    if word != word.lower():
        continue
    if "-" in word:
        continue

    count = 0
    for char in "lmnopqrstuv":
        if char in word:
            count += 1

    if count != 9:
        continue

    result.append(word)

print(result)

def puzzle_b(words):
    """What words consist of two consecutive pronouns?"""
    pronouns = ['thou', 'thee', 'thine', 'thy', 'i', 'me', 'mine', 'my', 'we', 'us', 'ours', 'our', 'you', 'yours',
                'your', 'he', 'him', 'his', 'she', 'her', 'hers', 'it', 'its', 'they', 'them', 'theirs', 'their']

    for word in words:
        for p1 in pronouns:
            for p2 in pronouns:
                if p1 + p2 == word:
                    print(word)

def puzzle_c(words):
    """Find all uncapitalized, seven-letter words, containing just a single vowel that does not have the letter s anywhere within it. """
    for word in words:
        if word != word.lower():
            continue

        if len(word) != 7:
            continue

        count = 0
        for char in "aeiou":
            if char in word:
                count += 1

        if count != 1:
            continue

        if "s" in word:
            continue

#Q7 
def square(number: int) -> int:

    number_str = str(number)

    sum = 0
    for digit in number_str:
        sum += int(digit) ** 2

    return sum

def is_happy(number: int) -> bool:

    while True:
        number_squared = square(number)
        if number_squared == 1:
            return True
        if number_squared == 4:
            return False

        number = number_squared

def all_happy(upper_limit: int) -> None:
    for i in range(1, upper_limit):
        if is_happy(i):
            print(i, end = " ")

print(square(19))
print(is_happy(19))
all_happy(100)
Q8 
import random

def get_input():

    guess = input("Please enter a 3 digit number")

    while True:
        if len(guess) != 3:
            guess = input("Please enter a 3 digit number")
        else:
            return guess

def tips(secret_code, guess):

    for i, digit in enumerate(guess):
        if digit not in secret_code:
            print("Null")
            continue

        if guess[i] == secret_code[i]:
            print("Bullseye")
            continue

        if digit in guess:
            print("Offtarget")


secret_number = str(random.randint(1, 100))

while len(secret_number) < 3:
    secret_number = "0" + str(secret_number)

print(secret_number)

guess = get_input()
tips(secret_number, guess)
