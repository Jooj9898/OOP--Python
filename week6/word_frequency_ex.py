import string

def main():
   word_count_dict = {}
   file = open("hare_and_tortoise.txt")
   for line in file:
       process_line(line, word_count_dict)
   print("Length of the dictionary:", len(word_count_dict))
   pretty_print(word_count_dict)


main()

def process_line(line, word_count_dict):
    line = line.strip().split()
    for word in line:
        word = word.lower().strip(string.punctuation)

def pretty_print(word_count_dict):
    print(len(my_dict))
    print("{:12s} : {:12s}".format("word","count"))
    for word, frequency in word_count_dict.items():
        print("{:12s} : {:12s".format(word,frequency))
    
    word_frequency = []  