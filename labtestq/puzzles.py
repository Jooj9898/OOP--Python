import string

def get_word_list(file_name):
    """ Read the word_list.txt file and returns a list with one word per element.
        Each word in the list is in lower case.
        For example: [aarhus, aaron, ababa, aback, ...]. """

    try:
        data_file = open(file_name, "r")
    except IOError:
        print("File could not be opened.")
        exit()

    word_list = []  # start with an empty word list
    for word in data_file:  # for every word (line) in the file
        # strip off end−of−line characters and make each word lowercase
        # then append the word to the word list
        word_list.append(word.strip().lower())
    return word_list

def puzzle_a(words):
    """ Find 5 uncapitalized, unhyphenated words that contain 9
        of the letters of the alphabet from l to v ("lmnopqrstuv"). """
    
    i = 0
    while i < 5:
        new_str = []
        for word in word_list:
            if '-' in word_list:
                continue
            j = 0
            for letter in 'lmnopqrstuv':
                if letter in word:
                    j +=1
                    new_str.append(word)
            if j !=9:
                continue
            print(word)
            i+=1


def puzzle_b(words):
    """ What words consist of two consecutive pronouns? """
    pronouns = ['thou', 'thee', 'thine', 'thy', 'i', 'me', 'mine', 'my',
                'we', 'us', 'ours', 'our', 'you', 'yours', 'your', 'he', 'him',
                'his', 'she', 'her', 'hers', 'it', 'its', 'they', 'them',
                'theirs', 'their']
    new_str = []
    i = 0
    for word in word_list:
        i = 0
        for letter in pronouns:
            if letter in word_list:
                print(word)
    


def puzzle_c(words):
    """ Find all uncapitalized, seven-letter words, containing just
        a single vowel that does not have the letter s anywhere within it. """
    i = 0
    while i<7:
        new_str = []
        for word in word_list:
            j = 0
            for letter in 'aeiou':
                if letter in word:
                    j+=1
                if j>1:
                    continue
                print(word)
                i+=1


def puzzle_d(words):
    """ When you are writing in script, there are four letters of the
        alphabet that cannot be completed in one stroke: i and j (which require dots)
        and t and x (which require crosses). Find a word that uses each of
        these letters exactly once. """


# Main code
word_list = get_word_list("labtestq\\word_list.txt")
print("*Puzzle a*")
puzzle_a(word_list)

print("\n*Puzzle b*")
puzzle_b(word_list)

print("\n*Puzzle c*")
puzzle_c(word_list)

print("\n*Puzzle d*")
puzzle_d(word_list)

##
def get_word_list(word_list):
    """ Read the word_list.txt file and returns a list with one word per element. Each word in the list is in lower case. For example: [aarhus, aaron, ababa, aback, ...]. """


    try:
        data_file = open(word_list, "r")
    except IOError:
        print("File could not be opened.")
        exit()


    word_list = []  # start with an empty word list
    for word in data_file:  # for every word (line) in the file
        # strip off end−of−line characters and make each word lowercase
        # then append the word to the word list
        word_list.append(word.strip().lower())
    return word_list






def puzzle_a(words) -> None:
    """ Find 5 uncapitalized, unhyphenated words that contain 9 of the letters of the alphabet from l to v ("lmnopqrstuv"). """
    a_puzzle = []


    for word in words:
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
        else:
            a_puzzle.append(word)


        if len(a_puzzle) == 5:
            print(a_puzzle)
            return






def puzzle_b(words) -> None:
    """ What words consist of two consecutive pronouns? """
    pronouns = ['thou', 'thee', 'thine', 'thy', 'i', 'me', 'mine', 'my',
                'we', 'us', 'ours', 'our', 'you', 'yours', 'your', 'he', 'him',
                'his', 'she', 'her', 'hers', 'it', 'its', 'they', 'them',
                'theirs', 'their']
    
    pro_word_list = []


    for word in words:
        for pro1 in pronouns:
            for pro2 in pronouns:
                if pro1 + pro2 in word:
                    pro_word_list.append(word)
                
                if len(pro_word_list) == 2:
                    print(pro_word_list)
                    return






def puzzle_c(words) -> None:
    """ Find all uncapitalized, seven-letter words, containing just a single vowel that does not have the letter s anywhere within it. """
    word_list = []


    for word in words:
        if word == word.lower() and len(word) == 7 and 's' not in word:
            vow_occur = 0
            index = 0
            while index < len(word):
                if word[index] in 'aeiou':
                    vow_occur += 1
                index += 1


            if vow_occur == 1:
                word_list.append(word)
    
    print(word_list)






def puzzle_d(words) -> None:
    """ Find words that use each of the letters i, j, t, and x exactly once. """
    word_list = []


    for word in words:
        # Initialize counters for each target letter
        i_count = j_count = t_count = x_count = 0


        for char in word:
            if char == 'i':
                i_count += 1
            elif char == 'j':
                j_count += 1
            elif char == 't':
                t_count += 1
            elif char == 'x':
                x_count += 1


        # Check if each letter appears exactly once
        if i_count == 1 and j_count == 1 and t_count == 1 and x_count == 1:
            word_list.append(word)


    print(word_list)






# Main code
word_list = get_word_list("Week 5/Notes/word_list.txt")
print("*Puzzle a*")
puzzle_a(word_list)


print("\n*Puzzle b*")
puzzle_b(word_list)


print("\n*Puzzle c*")
puzzle_c(word_list)


print("\n*Puzzle d*")
puzzle_d(word_list)
