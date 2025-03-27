#use sets fo find:
#common words found in two files
#number of unique words used by both files
#number of unique words used in each file

def main():
   hare_and_tortoise_set = set()
   three_little_pigs_set = set()
   hare_and_tortoise_file = open('hare_and_tortoise.txt')
   three_little_pigs_file = open('three_little_pigs.txt')

   for line in hare_and_tortoise_file:
       process_line(line, hare_and_tortoise_set)

   for line in three_little_pigs_file:
       process_line(line, three_little_pigs_set)

   pretty_print(hare_and_tortoise_set, three_little_pigs_set)

   def pretty_print(word_count_dict):
    print(len(my_dict))
    print("{:12s} : {:12s}".format("word","count"))
    for word, frequency in word_count_dict.items():
        print("{:12s} : {:12s".format(word,frequency))
